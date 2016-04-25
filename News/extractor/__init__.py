# coding: utf-8
import re
from urlparse import urljoin

from bs4 import BeautifulSoup, Comment, Tag, NavigableString
from lxml import html
from lxml.html.clean import Cleaner

from News.extractor.cleaner import BaseCleaner, NewsCleaner
from News.utils.util import clean_date_time


class NewsExtractor(object):

    HARD_TAGS = ["strong", "em", "a"]
    TAGS = ["script", "link"]

    def __init__(self, html, url=None, hard_tags=None, tags=None, news=None):
        self.html = html
        self.cleaned_html = html
        self.url = url
        self.hard_tags = hard_tags if hard_tags is not None else self.HARD_TAGS
        self.tags = tags if tags is not None else self.TAGS
        self._hard_remove_tags()
        self.soup = BeautifulSoup(self.cleaned_html, "lxml")
        self._remove_comments()
        self._remove_tags()
        self.news = news

    def _hard_remove_tags(self):
        """ remove tags in html, notice not remove the inner content """
        if self.hard_tags:
            p = re.compile("|".join(["<{tag}[^>]*>|</{tag}>".format(tag=tag)
                                     for tag in self.hard_tags]))
            self.cleaned_html = re.sub(p, "", self.html)

    def _remove_comments(self):
        """ remove comments in html """
        comments = self.soup.find_all(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

    def _remove_tags(self):
        """ remove tags and inner content in html """
        [tag.extract() for tag in self.soup.find_all(self.tags)]

    @staticmethod
    def _remove_tag(tag, name, **kwargs):
        """
        remove all tags in Tag of BeautifulSoup
        :param tag: Tag Object of BeautifulSoup
        :param name: str, tag name
        :param kwargs: parameters of find_all
        :return: in place, no return
        """
        if tag is None: return
        [t.extract() for t in tag.find_all(name, **kwargs)]

    @staticmethod
    def g_returns(content):
        count = 0
        contents = list()
        for c in content:
            if "img" in c and c["img"]:
                count += 1
                contents.append(c)
            elif "text" in c and c["text"] and c["text"].strip():
                contents.append(c)
        return contents, count

    @classmethod
    def _extract(cls, tag):
        result = list()
        if not tag: return result
        for child in tag.descendants:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append({"img": cls.__get_img_src(child)})
            else:
                pass
        return result

    @classmethod
    def _extract_regular(cls, tag, length=3):
        result = list()
        tag, l = cls._get_content_tag(tag)
        if tag is None or l < length:
            return result
        cls._extract_tag_children(tag, result)
        return result

    @classmethod
    def _extract_tag_children(cls, tag, result):
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append({"img": cls.__get_img_src(child)})
                elif child.img:
                    cls._extract_tag_children(child, result)
                else:
                    result.append({"text": child.get_text().strip()})
            else:
                pass

    @classmethod
    def _get_content_tag(cls, tag):
        mapping = dict()
        cls.__find_content_tag(tag, mapping)
        s_list = sorted(mapping.iteritems(), key=lambda k: k[1], reverse=True)
        if len(s_list) == 0:
            return None, 0
        item = s_list[0]
        tag = item[0]
        length = item[1]
        return tag, length

    @classmethod
    def __find_content_tag(cls, tag, mapping):
        if isinstance(tag, Tag):
            mapping[tag] = len(tag.contents)
            for child in tag.children:
                cls.__find_content_tag(child, mapping)

    @staticmethod
    def __get_img_src(tag):
        img_url_name = ["src", "alt-src", "data-src"]
        for name in img_url_name:
            url = tag.get(name, "").strip()
            if url.startswith("http"):
                return url
        return ""

    @staticmethod
    def _show(content):
        for item in content:
            for key, value in item.items():
                print("%s: %s" % (key, value))


def remove_tag_name(string, name):
    """从字符串中移除名字为 name 的标签名

    若 name 为 list 或 tuple, 则移除包含这些名字的标签

    :param string:str
    :param name:str, list or tuple, 标签名
    :return:str, 移除后的字符串
    """
    if isinstance(name, (list, tuple)):
        p_string = "|".join(["<{tag}[^>]*>|</{tag}>".format(tag=tag) for tag in name])
    else:
        p_string = "<{tag}[^>]*>|</{tag}>".format(tag=name)
    p = re.compile(p_string)
    return re.sub(p, "", string)


def get_img_src(base_url, tag):
    """获取 img Tag 的 src 属性

    若初始化类中传入 url 参数，则返回 img 的绝对路径

    :param tag:bs4.Tag, 要获取链接的 img Tag
    :return:str, 图片的链接地址
    """
    img_url_name = ["src", "alt-src", "alt_src", "data-src", "data-original"]
    urls = []
    img_types = [".jpg", ".png", ".webp", ".gif", ".jpeg"]
    for name in img_url_name:
        url = tag.get(name, "").strip()
        if url.startswith("http"):
            return url
        else:
            urls.append(url)
    for url in urls:
        lower = url.lower()
        for t in img_types:
            if lower.endswith(t):
                return url if base_url is None else urljoin(base_url, url)
        if lower.startswith("/") or lower.startswith("//"):
            return url if base_url is None else urljoin(base_url, url)
    return ""


def get_content_item(key, value):
    """构造 content 的内容

    :param key:str, 支持 "text", "image", 分别表示文本和图片
    :param value:str, 对应 key 的值
    :return:dict
    """
    keys = {"text": "text", "image": "img"}
    assert key in keys
    return {keys[key]: value.strip()}


def show(content):
    for item in content:
        for key, value in item.items():
            print("%s: %s" % (key, value))


def score_dom_tree(root, mapping):
    content_tag_names = ["div", "article", "body", "html"]
    if not isinstance(root, (Tag, BeautifulSoup)):
        return
    if root.name not in content_tag_names:
        return
    score = 0.0
    for child in root.children:
        if isinstance(child, NavigableString):
            string = unicode(child).strip()
            if len(string) >= 5:
                score += 1 + len(string)/40 * 5
            elif child.name == "p":
                score += len(child.get_text())/20 * 5
            elif child.name == "a":
                score += 0.2
            elif child.name == "div":
                score += 0.2
    mapping[root] = int(score)
    for child in root.children:
        score_dom_tree(child, mapping)


def score_dom_tree_new(root, mapping):
    if not isinstance(root, (Tag, BeautifulSoup)):
        return
    mapping[root] = 0.0
    root_child_length = len(root.contents)
    root_p_length = len(root.find_all("p", recursive=False))
    weight = 1 if root_p_length > 0 else root_p_length
    for child in root.children:
        if isinstance(child, Tag):
            mapping[child] = mapping.get(child, 0.0)
            if child.name == "img":
                if child.find_parent("a"):  # 超链接图片
                    pass
                else:
                    mapping[child] += 3.0
            elif child.name == "p":
                if child.img:
                    mapping[child] += 10.0
                l = len(child.get_text().strip())
                mapping[child] += l/40 * 6 * weight
            else:
                score_dom_tree_new(child, mapping)
            mapping[root] += mapping[child]
        elif isinstance(child, NavigableString):
            parent = child.parent
            if child.find_parent(name="a"):     # 超链接文本
                pass
            else:
                mapping[parent] += len(unicode(child).strip())/40 * 3
        else:
            pass


def choose_content_tag(root, mapping):
    score = mapping[root]
    tag = root
    min_score = score
    content_tags = root.find_all(name=["div", "article"])
    for child in content_tags:
        c_score = mapping[child]
        if 0.6 * score < c_score <= min_score:
            min_score = c_score
            tag = child
    return None if tag.name == "body" else tag


def find_content_tag(root):
    if root is None:
        return root
    mapping = dict()
    score_dom_tree_new(root, mapping)
    return choose_content_tag(root, mapping)


class BaseExtractor(object):
    """文章抽取基础类

    子类必须实现　parse_content_tag　方法

    """
    title_param = None
    post_date_param = None
    post_source_param = None
    summary_param = None
    content_param = None
    clean_param_list = None
    clean_content_before_param = None
    clean_content_after_param = None

    def __init__(self, document, url=None, encoding="utf-8"):
        """抽取类初始化

        :param document: str, 新闻原始html页面
        """
        self.document = document
        self.encoding = encoding
        self.base_cleaned_html = self.base_clean(self.document)
        self.base_soup = BeautifulSoup(self.base_cleaned_html, "lxml", from_encoding=self.encoding)
        self.news_cleaned_html = self.news_clean(self.base_cleaned_html)
        self.soup = BeautifulSoup(self.news_cleaned_html, "lxml", from_encoding=self.encoding)
        self.base_url = url
        if self.base_url:
            self.clean_a_tag_attrs(self.soup, self.base_url)

    @staticmethod
    def clean_a_tag_attrs(root, base_url):
        """clean a tag attrs and convert relative link to absolute link

            only keep href attrs

        :param root: bs4 tag or soup
        :param base_url: base url
        """
        for a_tag in root.find_all("a"):
            a_tag.attrs = {"href": urljoin(base_url, a_tag.get("href", ""))}

    @classmethod
    def base_clean(cls, document, cleaner=None):
        """
        clean html document use cleaner default BaseCleaner, remove some tags
        that not needed
        :param document: html document string
        :type document: str
        :param cleaner: cleaner object
        :type cleaner: Cleaner Object | None
        :return: cleaned document string
        :rtype: str
        """
        if cleaner is None:
            cleaner = BaseCleaner()
        return cls.lxml_clean(document, cleaner)

    @classmethod
    def news_clean(cls, document, cleaner=None):
        """
        clean html document for score DOM tree and extract content
        use cleaner default NewsCleaner, only allow some tags that
        news needed
        :param document: html document string
        :type document: str
        :param cleaner: cleaner object
        :type cleaner: Cleaner Object | None
        :return: cleaned document string
        :rtype: str
        """
        if cleaner is None:
            cleaner = NewsCleaner()
        return cls.lxml_clean(document, cleaner)

    @staticmethod
    def lxml_clean(document, cleaner, encoding='utf-8'):
        assert isinstance(cleaner, Cleaner)
        parser = html.HTMLParser(
            encoding=encoding,
            remove_comments=True,
            remove_blank_text=True,
            remove_pis=True,
        )
        root = html.document_fromstring(document, parser=parser)
        root = cleaner.clean_html(root)
        return html.tostring(root, encoding=encoding)

    @staticmethod
    def exact_find_tag(root, param):
        method = param["method"]
        params = param["params"]
        nth = param.get("nth", 0)
        if method == "find_all":
            tags = root.find_all(**params)
            return tags[nth] if len(tags) > nth else None
        elif method == "select":
            tags = root.select(**params)
            return tags[nth] if len(tags) > nth else None
        else:
            raise ValueError("param['method'] only support find_all and select")

    @staticmethod
    def extract_tag_text(tag):
        if tag is None:
            return ""
        assert isinstance(tag, Tag)
        if tag.name == "meta":
            return tag.get("content", "")
        return tag.get_text().strip()

    @staticmethod
    def extract_tag_attribute(tag, name):
        if tag is None:
            return ""
        assert isinstance(tag, Tag)
        return tag.get(name, "")

    @classmethod
    def exact_extract_tag(cls, root, param):
        tag = cls.exact_find_tag(root, param)
        attribute = param.get("attribute", None)
        if attribute is None:
            string = cls.extract_tag_text(tag)
        else:
            string = cls.extract_tag_attribute(tag, attribute)
        return string

    def exact_extract_title(self, param):
        """根据param参数精确抽取新闻标题

        :param param: 自定义格式参数，支持 find_all, select 方法
        :type param: dict
        :return: 新闻标题
        :rtype: str
        """
        return self.exact_extract_tag(self.base_soup, param)

    def default_extract_title(self):
        param = {"method": "find_all", "params": {"name": "title"}, "nth": 0}
        return self.exact_extract_title(param)

    def extract_title(self, param=None):
        if param is None:
            string = self.default_extract_title()
        else:
            string = self.exact_extract_title(param)
        return self.clean_title(string)

    @staticmethod
    def clean_title(string):
        """清洗新闻标题

        子类可重写该方法实现需要的标题清洗，默认不做任何清洗

        :param string:str, 需要清洗的标题字符串
        :return: str
        """
        # words = string.split("|")
        # return words[0]
        return string

    def exact_extract_summary(self, param):
        """根据param参数精确抽取新闻摘要

        :param param: 自定义格式参数，支持 find_all, select 方法
        :type param: dict
        :return: 新闻标题
        :rtype: str
        """
        return self.exact_extract_tag(self.base_soup, param)

    def default_extract_summary(self):
        param = {
            "method": "find_all",
            "params": {"name": "meta", "attrs": {"name": "description"}},
            "nth": 0,
        }
        return self.exact_extract_summary(param)

    def extract_summary(self, param=None):
        """新闻概要抽取

        :param param:dict, bs4 find method params
        :return: str
        """
        if param is None:
            string = self.default_extract_summary()
        else:
            string = self.exact_extract_summary(param)
        return self.clean_summary(string)

    @staticmethod
    def clean_summary(string):
        return string

    def exact_extract_post_date(self, param):
        return self.exact_extract_tag(self.base_soup, param)

    def default_extract_post_date(self):
        # param = {
        #     "method": "find_all",
        #     "params": {"name": None, "attrs": dict()},
        #     "nth": 0,
        # }
        # return self.exact_extract_post_date(param)
        return ""

    def extract_post_date(self, param=None):
        """新闻发布时间抽取

        :param param:dict, bs4 find method params
        :return: str
        """
        if param is None:
            string = self.default_extract_post_date()
        else:
            string = self.exact_extract_post_date(param)
        return self.clean_post_date(string)

    @staticmethod
    def clean_post_date(string):
        """清洗新闻发布时间

        子类可重写该方法实现需要的时间清洗，默认进行简单清洗

        :param string:str, 需要清洗的时间字符串
        :return: str
        """
        return clean_date_time(string)

    def exact_extract_post_source(self, param):
        return self.exact_extract_tag(self.base_soup, param)

    def default_extract_post_source(self):
        # param = {
        #     "method": "find_all",
        #     "params": {"name": None, "attrs": dict()},
        #     "nth": 0,
        # }
        # return self.exact_extract_post_source(param)
        return ""

    def extract_post_source(self, param=None):
        """新闻来源抽取

        :param param:dict, bs4 find method params
        :return: str
        """
        if param is None:
            string = self.default_extract_post_source()
        else:
            string = self.exact_extract_post_source(param)
        return self.clean_post_source(string)

    @staticmethod
    def clean_post_source(string):
        return string

    @classmethod
    def content_tag_clean(cls, root, clean_param_list):
        for param in clean_param_list:
            tag = cls.exact_find_tag(root, param)
            if tag is not None:
                tag.extract()

    @classmethod
    def content_tag_clean_before(cls, root, param):
        tag = cls.exact_find_tag(root, param)
        if tag is not None:
            siblings = []
            for sibling in tag.previous_siblings:
                siblings.append(sibling)
            for sibling in siblings:
                sibling.extract()
            tag.extract()

    @classmethod
    def content_tag_clean_after(cls, root, param):
        tag = cls.exact_find_tag(root, param)
        if tag is not None:
            siblings = []
            for sibling in tag.next_siblings:
                siblings.append(sibling)
            for sibling in siblings:
                sibling.extract()
            tag.extract()

    def extract_content(self, param=None, clean_param_list=None,
                        clean_content_before_param=None,
                        clean_content_after_param=None):
        content = list()
        if param is None:
            tag = find_content_tag(self.soup.body)
        else:
            tag = self.exact_find_tag(self.soup, param)
            if tag is None:
                tag = find_content_tag(self.soup.body)
        if tag is None:
            return content
        if clean_content_before_param is not None:
            self.content_tag_clean_before(tag, clean_content_before_param)
        if clean_content_after_param is not None:
            self.content_tag_clean_after(tag, clean_content_after_param)
        if clean_param_list is not None:
            self.content_tag_clean(tag, clean_param_list)
        self.parse_content_tag(tag, content)
        return self.clean_content(content)

    @staticmethod
    def clean_content(content):
        return content

    def parse_content_tag(self, tag, content):
        raise NotImplementedError

    def __call__(
            self,
            title_param=None,
            post_date_param=None,
            post_source_param=None,
            summary_param=None,
            content_param=None,
            clean_param_list=None,
            clean_content_before_param=None,
            clean_content_after_param=None,
    ):
        if title_param is None:
            title_param = self.title_param
        if post_date_param is None:
            post_date_param = self.post_date_param
        if post_source_param is None:
            post_source_param = self.post_source_param
        if summary_param is None:
            summary_param = self.summary_param
        if content_param is None:
            content_param = self.content_param
        if clean_param_list is None:
            clean_param_list = self.clean_param_list
        if clean_content_before_param is None:
            clean_content_before_param = self.clean_content_before_param
        if clean_content_after_param is None:
            clean_content_after_param = self.clean_content_after_param
        title = self.extract_title(title_param)
        post_date = self.extract_post_date(post_date_param)
        post_source = self.extract_post_source(post_source_param)
        summary = self.extract_summary(summary_param)
        content = self.extract_content(content_param,
                                       clean_param_list,
                                       clean_content_before_param,
                                       clean_content_after_param)
        return title, post_date, post_source, summary, content


class GeneralExtractor(BaseExtractor):

    def parse_content_tag(self, tag, content):
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child).strip()
                if string:
                    content.append(get_content_item("text", string))
            elif isinstance(child, Tag):
                if child.name == "img":
                    src = get_img_src(self.base_url, child)
                    if src:
                        content.append(get_content_item("image", src))
                elif child.name == "div" or child.img or child.br:
                    self.parse_content_tag(child, content)
                elif child.get_text().strip():
                    string = str(child)
                    string = remove_tag_name(string, ["p", "article"])
                    content.append(get_content_item("text", string))


class YiDianZiXunExtractor(GeneralExtractor):
    title_param = {
        "method": "find_all",
        "params": {"name": "h2", "attrs": dict()},
    }
    post_source_param = {
        "method": "find_all",
        "params": {"name": "a", "attrs": dict(id="source-name")},
    }
    content_param = {
        "method": "find_all",
        "params": {"name": "div", "attrs": {"class": "content-bd"}},
    }
    clean_content_after_param = {
        "method": "find_all",
        "params": {"name": "div", "attrs": {"class": "report"}}
    }


class TouTiaoExtractor(GeneralExtractor):
    title_param = {
        "method": "find_all",
        "params": {"name": "h1", "attrs": {"class": "title"}},
    }
    post_date_param = {
        "method": "find_all",
        "params": {"name": "span", "attrs": {"class": "time"}},
    }
    post_source_param = {
        "method": "find_all",
        "params": {"name": "span", "attrs": {"class": "src"}},
    }
    content_param = {
        "method": "find_all",
        "params": {"name": "div", "attrs": {"class": "article-content"}},
    }


class WechatExtractor(GeneralExtractor):
    title_param = {
        "method": "find_all",
        "params": {"name": None, "attrs": dict(id="activity-name")},
    }
    post_date_param = {
        "method": "find_all",
        "params": {"name": None, "attrs": dict(id="post-date")},
    }
    post_source_param = {
        "method": "find_all",
        "params": {"name": None, "attrs": dict(id="post-user")},
    }
    content_param = {
        "method": "find_all",
        "params": {"name": None, "attrs": dict(id="js_content")},
    }


class MovieSoonExtractor(GeneralExtractor):

    DIGITAL_MAPPING = {
        u"一": "01",
        u"二": "02",
        u"三": "03",
        u"四": "04",
        u"五": "05",
        u"六": "06",
        u"七": "07",
        u"八": "08",
        u"九": "09",
        u"十": "10",
        u"十一": "11",
        u"十二": "12",
    }

    def default_extract_post_date(self):
        year_param = {
            "method": "find_all",
            "params": {"name": "span", "attrs": {"class": "year"}},
        }
        month_param = {
            "method": "find_all",
            "params": {"name": "span", "attrs": {"class": "month"}},
        }
        day_param = {
            "method": "find_all",
            "params": {"name": "span", "attrs": {"class": "gun"}},
        }
        year = self.exact_extract_tag(self.base_soup, year_param)
        month = self.exact_extract_tag(self.base_soup, month_param)
        day = self.exact_extract_tag(self.base_soup, day_param)
        if len(year) != 4:
            return ""
        if len(day) == 1:
            day = "0" + day
        if month not in self.DIGITAL_MAPPING:
            return ""
        month = self.DIGITAL_MAPPING[month]
        time_tag = {
            "method": "find_all",
            "params": {"name": "div", "attrs": {"class": "postAyrinti"}},
        }
        time_string = self.exact_extract_tag(self.base_soup, time_tag)
        return "-".join([year, month, day]) + time_string


class News163Extractor(GeneralExtractor):

    pass

