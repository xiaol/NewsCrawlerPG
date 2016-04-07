# coding: utf-8

import networkx as nx
import matplotlib.pyplot as plt
from bs4 import Tag
from News.utils.util import get_document
from News.extractor import GeneralExtractor
from News.extractor import score_dom_tree_new, choose_content_tag

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 18:46"


def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5,
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
                                pos=pos, parent=root)
    return pos


def draw_tree(string):
    g = nx.DiGraph()
    labels = dict()
    extractor = GeneralExtractor(string)
    root = extractor.soup.body
    mapping = dict()
    for child in root.descendants:
        if isinstance(child, Tag):
            mapping[child] = 0.0
    score_dom_tree_new(root, mapping)
    g.add_node(root)
    labels[root] = _g_label(root, mapping)
    _draw_node(root, g, labels, mapping)
    pos = hierarchy_pos(g, root)
    node_size = max(map(len, labels.values())) * 300
    nx.draw(g, pos=pos, with_labels=False, node_size=node_size)
    nx.draw_networkx_labels(g, pos, labels=labels)
    plt.show()


def _draw_node(root, g, labels, mapping):
    for child in root.children:
        if not isinstance(child, Tag) or mapping[child] < 0.1:
            continue
        g.add_node(child)
        labels[child] = _g_label(child, mapping)
        p = child.parent
        g.add_edge(p, child)
        _draw_node(child, g, labels, mapping)


def _g_label(tag, mapping):
    return tag.name + ":" + str(int(mapping[tag]))


if __name__ == '__main__':
    string = """
        <html>
            <head>
                <title>Test</title>
            </head>
            <body>
                hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
                <h2>Hello World</h2>
                <div>
                <p>hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh</p>
                <a><img src="/test.png"></img></a>
                hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
                <img src="/test.png"></img>
                <div>
            </body>
        </html>
    """
    string = get_document("http://mp.weixin.qq.com/s?__biz=MzA3OTU3NjEwOA==&mid=404091998&idx=7&sn=3c4e6718e7bf93f28df04904b33f5830&3rd=MzA3MDU4NTYzMw==&scene=6#rd")
    draw_tree(string)




