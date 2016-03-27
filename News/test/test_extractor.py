# coding: utf-8

from urlparse import urlparse
import requests
from lxml import etree
from lxml import html
from lxml.html.clean import Cleaner
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-25 17:18"


def get_document(url):
    netloc = urlparse(url).netloc
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
               "host": netloc}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        encoding = r.apparent_encoding
        if encoding.lower() == "gb2312":
            encoding = "GB18030"
        return r.content.decode(encoding).encode("utf-8")
    else:
        print("get document error: %s" % r.status_code)
        return ""


def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0,
                  xcenter=0.5,
                  pos=None, parent=None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent is not None:
        if parent in neighbors:
            neighbors.remove(parent)
    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap,
                                vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                pos=pos,
                                parent=root)
    return pos


def score_tags(root):
    root.score = 0.0
    if len(root) > 0:
        for child in root:
            score_tags(child)
            root.score += child.score
        if root.text is not None:
            root.score += len(root.text)/40 * 2
    else:
        if root.tag == "p":
            root.score = 2.0
            if root.text is not None:
                root.score += len(root.text)/40 * 5
        elif root.tag == "img":
            for p in root.iterancestors():
                if p.tag == "a":
                    root.score = 0.0
                    break
            else:
                root.score = 5.0
        else:
            root.score = 0.0
    parent = root.getparent()
    tail = root.tail
    if tail is not None and parent is not None:
        parent.score += len(tail) / 40 * 2
    root.attrib["score"] = str(int(root.score))


def show_score(root):
    score = int(root.attrib["score"])
    tag = root
    min_score = score
    for child in root.iter(tag=["div", "article"]):
        c_score = int(child.attrib["score"])
        if c_score >= 0.6 * score:
            if c_score < min_score:
                min_score = c_score
                tag = child
    print("tag: %s" % tag.tag)
    print tag.attrib
    return tag


def extract(string):
    G = nx.DiGraph()
    labels = {}
    root = html.document_fromstring(string)
    score_tags(root)
    root = show_score(root)
    G.add_node(root)
    labels[root] = root.tag + ":" + root.attrib["score"]
    _extract(root, G, labels)
    # nx.drawing.nx_pydot.write_dot(G, "tree.dot")
    pos = hierarchy_pos(G, root)
    node_size = max(map(len, labels.values()))*300
    nx.draw(G, pos=pos, with_labels=False, node_size=node_size)
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.show()


def _extract(root, g, labels):
    for child in root.iterchildren():
        g.add_node(child)
        labels[child] = child.tag + ":" + child.attrib["score"]
        p = child.getparent()
        g.add_edge(p, child)
        _extract(child, g, labels)


if __name__ == '__main__':
    string = """
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
            <h2>Hello World</h2>
            <p>hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh</p>
            <a><img src="/test.png"></img></a>
            hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
            <img src="/test.png"></img>
        </body>
    </html>
"""
    string = get_document("http://www.open-open.com/news/view/16b6c3b")
    allow_tags = ("b", "blod", "big", "em", "font", "h1", "h2", "h3", "h4",
                  "h5", "h6", "i", "italic", "small", "strike", "sub",
                  "a", "p", "strong", "div", "img", "tt", "u", "html",
                  "meta", "body", "head", "br", "sup", "title", "article")
    cleaner = Cleaner(scripts=True, javascript=True, comments=True,
                      style=True, links=True, meta=False,
                      add_nofollow=False, page_structure=False,
                      processing_instructions=True, embedded=False,
                      frames=False, forms=False, annoying_tags=False,
                      remove_tags=None, remove_unknown_tags=False,
                      safe_attrs_only=False, allow_tags=allow_tags)
    string = cleaner.clean_html(string)
    extract(string=string)



