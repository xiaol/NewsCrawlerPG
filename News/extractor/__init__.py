# coding: utf-8
import re
from datetime import datetime
from urlparse import urljoin
from lxml import html
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup, Comment, Tag, NavigableString
from News.cleaner import BaseCleaner, NewsCleaner


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
    length = len([tag for tag in root.contents if isinstance(tag, Tag)])
    if length > 0:
        for child in root.children:
            if isinstance(child, Tag):
                score_dom_tree_new(child, mapping)
                mapping[root] += mapping[child]
            elif isinstance(child, NavigableString):
                string = unicode(child).strip()
                mapping[root] += len(string)/40 * 2
    else:
        if root.name == "p":
            mapping[root] = 2.0
            string = root.get_text().strip()
            mapping[root] += len(string)/40 * 5
        elif root.name == "img":
            if root.find_parent("a"):
                mapping[root] = 0.0
            else:
                mapping[root] = 5.0
        else:
            mapping[root] = 0.0


def find_content_tag(root):
    if root is None:
        return root
    mapping = dict()
    score_dom_tree_new(root, mapping)
    score = mapping[root]
    tag = root
    min_score = score
    for child in root.find_all(["div", "article"]):
        c_score = mapping[child]
        if c_score >= 0.6 * score:
            if c_score < min_score:
                min_score = c_score
                tag = child
    # mapping = sorted(mapping.items(), key=lambda k: k[1], reverse=True)
    # return None if not mapping else mapping[0][0]
    return tag


class BaseExtractor(object):
    """文章抽取基础类

    子类必须实现　extract_content　方法

    """
    # soup find title param
    title_param = {"name": "title", "attrs": dict()}
    # soup find post date param
    post_date_param = {"name": None, "attrs": dict()}
    # soup find post user param
    post_user_param = {"name": None, "attrs": dict()}
    # soup find content param
    content_param = {"name": None, "attrs": dict()}
    # soup find content param
    summary_param = {"name": "meta", "attrs": {"name": "description"}}

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

    @classmethod
    def exact_extract_tag(cls, root, param):
        tag = cls.exact_find_tag(root, param)
        string = cls.extract_tag_text(tag)
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
        param = {
            "method": "find_all",
            "params": {"name": None, "attrs": dict()},
            "nth": 0,
        }
        return self.exact_extract_post_date(param)

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
        date_time_string = ""
        p_date_list = [
            r"((20\d{2})[/.-])?(\d{2})[/.-](\d{2})",
            r"((20\d{2})?年)?(\d{2})月(\d{2})",
            u"((20\d{2})?\u5e74)?(\d{2})\u6708(\d{2})",

            r"((20\d{2})[/.-])?(\d{1})[/.-](\d{2})",
            r"((20\d{2})?年)?(\d{1})月(\d{2})",
            u"((20\d{2})?\u5e74)?(\d{1})\u6708(\d{2})",

            r"((20\d{2})[/.-])?(\d{2})[/.-](\d{1})",
            r"((20\d{2})?年)?(\d{2})月(\d{1})",
            u"((20\d{2})?\u5e74)?(\d{2})\u6708(\d{1})",

            r"((20\d{2})[/.-])?(\d{1})[/.-](\d{1})",
            r"((20\d{2})?年)?(\d{1})月(\d{1})",
            u"((20\d{2})?\u5e74)?(\d{1})\u6708(\d{1})",
        ]
        for p_date in p_date_list:
            date_match = re.search(p_date, string)
            if date_match is not None:
                break
        else:
            return date_time_string
        p_time = r"(\d{2}):(\d{2})(:(\d{2}))?"
        time_match = re.search(p_time, string)
        now = datetime.now()
        year_now = now.strftime("%Y")
        hour_now = now.strftime("%H")
        minute_now = now.strftime("%M")
        second_now = now.strftime("%S")
        if date_match is None:
            return date_time_string
        else:
            date_groups = date_match.groups()
        if time_match is None:
            time_groups = (hour_now, minute_now, ":"+second_now, second_now)
        else:
            time_groups = time_match.groups()
        year = date_groups[1]
        month = date_groups[2]
        if len(month) == 1:
            month = "0" + month
        day = date_groups[3]
        if len(day) == 1:
            day = "0" + day
        hour = time_groups[0]
        minute = time_groups[1]
        second = time_groups[3]
        if year is None:
            year = year_now
        if second is None:
            second = second_now
        date_string = "-".join([year, month, day])
        time_string = ":".join([hour, minute, second])
        date_time_string = date_string + " " + time_string
        return date_time_string

    def exact_extract_post_source(self, param):
        return self.exact_extract_tag(self.base_soup, param)

    def default_extract_post_source(self):
        param = {
            "method": "find_all",
            "params": {"name": None, "attrs": dict()},
            "nth": 0,
        }
        return self.exact_extract_post_source(param)

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

    @staticmethod
    def find_default_content_tag(root):
        return find_content_tag(root)

    def extract_content(self, param=None, clean_param_list=None):
        content = list()
        if param is None:
            tag = self.find_default_content_tag(self.soup)
        else:
            tag = self.exact_find_tag(self.soup, param)
        if tag is None:
            return content
        if clean_param_list is not None:
            self.content_tag_clean(tag, clean_param_list)
        self.parse_content_tag(tag, content)
        return content

    def parse_content_tag(self, tag, content):
        raise NotImplementedError

    # def extract_content(self, tag, content):
    #     """新闻内容抽取
    #
    #     新闻内容的抽取函数，子类必须重写该方法来实现自己的抽取逻辑
    #
    #     :param tag:bs4.Tag, 包含内容块的 Tag 节点
    #     :param content: list, 返回内容存储在该 list 中
    #     """
    #     raise NotImplementedError
    #
    # def _extract_content(self, param):
    #     """新闻内容抽取
    #
    #     调用 extract_content 函数来实现新闻内容的抽取，子类可通过重写 extract_content 方
    #     法来实现自己的抽取逻辑
    #
    #     :param param:dict, bs4 find method params
    #     :return: list
    #     """
    #     name = param["name"]
    #     attrs = param["attrs"]
    #     tag = self.find_content_tag(name, attrs=attrs)
    #     content = list()
    #     if tag: self.extract_content(tag, content)
    #     return content

    def __call__(
            self,
            title_param=None,
            post_date_param=None,
            post_source_param=None,
            summary_param=None,
            content_param=None,
            clean_param_list=None,
    ):
        """抽取入口

        优先采用传入参数，若无，则使用类的相应成员变量

        :param title_param:dict, {"args": list(), "kwargs": dict()}
        :param post_date_param:dict,
        :param post_source_param:dict,
        :param content_param:dict,
        :return:title, post_date, post_user, content
        """
        title = self.extract_title(title_param)
        post_date = self.extract_post_date(post_date_param)
        post_source = self.extract_post_source(post_source_param)
        summary = self.extract_summary(summary_param)
        content = self.extract_content(content_param, clean_param_list)
        return title, post_date, post_source, summary, content

    # def find_content_tag(self, name, attrs):
    #     """获取包含内容的 Tag 节点
    #
    #     子类可重写该函数，实现精确的内容块定位。默认使用打分方式，定位文章主要内容的 Tag
    #
    #     :param name:list, bs4 find name param
    #     :param attrs:dict, bs4 find param
    #     :return:bs4.Tag, 返回包含内容的 Tag 节点
    #     """
    #     if name or attrs:
    #         return self.soup.find(name, attrs=attrs)
    #     if not self.soup.body:
    #         return None
    #     tag = self.soup.body
    #     mapping = dict()
    #     self.score_tags(tag, mapping)
    #     sorted_mapping = sorted(mapping.items(), key=lambda k: k[1], reverse=True)
    #     # for item in sorted_mapping:
    #     #     tag = item[0]
    #     #     score = item[1]
    #     #     print("tag name: %s" % tag.name)
    #     #     print("tag id: %s" % tag.get("id", ""))
    #     #     # print("tag class: %s" % tag.get("class", ""))
    #     #     print("score: %d" % score)
    #     #     print tag.get("class")
    #     return None if not sorted_mapping else sorted_mapping[0][0]

    # @classmethod
    # def score_tags(cls, tag, mapping):
    #     """为 tag 树打分
    #
    #     :param tag: bs4.Tag, 要打分的 Tag
    #     :param mapping: dict, 整个树的打分值
    #     """
    #     content_tag_names = ["div", "body", "html", "article"]
    #     if not isinstance(tag, Tag): return
    #     if tag.name not in content_tag_names: return
    #     score = 0.0
    #     for child in tag.children:
    #         if isinstance(child, NavigableString):
    #             string = unicode(child).strip()
    #             if len(string) >= 5:
    #                 score += 1 + len(string)/40 * 5
    #         elif child.name == "p":
    #             score += len(child.get_text())/20 * 5
    #         elif child.name == "a":
    #             score += 0.2
    #         elif child.name == "img":
    #             score += 0.5
    #         elif child.name == "div":
    #             score += 0.2
    #         # else:
    #         #     score += 1
    #     mapping[tag] = int(score)
    #     for child in tag.children:
    #         cls.score_tags(child, mapping)

    @staticmethod
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

    def get_img_src(self, tag):
        """获取 img Tag 的 src 属性

        若初始化类中传入 url 参数，则返回 img 的绝对路径

        :param tag:bs4.Tag, 要获取链接的 img Tag
        :return:str, 图片的链接地址
        """
        img_url_name = ["src", "alt-src", "alt_src", "data-src"]
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
                    return url if self.base_url is None else urljoin(self.base_url, url)
            if lower.startswith("/") or lower.startswith("//"):
                return url if self.base_url is None else urljoin(self.base_url, url)
        return ""

    @staticmethod
    def get_content_item(key, value):
        """构造 content 的内容

        :param key:str, 支持 "text", "image", 分别表示文本和图片
        :param value:str, 对应 key 的值
        :return:dict
        """
        keys = {"text": "text", "image": "img"}
        assert key in keys
        return {keys[key]: value.strip()}

    @staticmethod
    def show(content):
        for item in content:
            for key, value in item.items():
                print("%s: %s" % (key, value))

    def get_tag_text(self, name, attrs):
        """获取一个用　bs4 find 定位的 Tag 里的内容

        :param name: list, bs4 find name params
        :param attrs: dict, bs4 find params
        :return:str
        """
        tag = self.base_soup.find(name, attrs=attrs)
        if name == "meta":
            return tag.get("content", "") if tag else ""
        return tag.get_text().strip() if tag else ""


class GeneralExtractor(BaseExtractor):

    # remove tags in content
    remove_tag_name_list = ["p", "article", "span"]

    @staticmethod
    def clean(doc):
        allow_tags = ("b", "blod", "big", "em", "font", "h1", "h2", "h3", "h4",
                      "h5", "h6", "i", "italic", "small", "strike", "sub",
                      "a", "p", "strong", "div", "img", "tt", "u", "html",
                      "meta", "body", "head", "br", "sup", "title", "article",
                      "span")
        encoding = "utf-8"
        cleaner = Cleaner(scripts=True, javascript=True, comments=True,
                          style=True, links=True, meta=False,
                          add_nofollow=False, page_structure=False,
                          processing_instructions=True, embedded=False,
                          frames=False, forms=False, annoying_tags=False,
                          remove_tags=None, remove_unknown_tags=False,
                          safe_attrs_only=False, allow_tags=allow_tags)
        parser = html.HTMLParser(encoding=encoding, remove_comments=True,
                                 remove_blank_text=True)
        document = html.document_fromstring(doc, parser=parser)
        document = cleaner.clean_html(document)
        return html.tostring(document, encoding=encoding)

    def parse_content_tag(self, tag, content):
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child).strip()
                if string:
                    string = "<p>" + string + "</p>"
                    content.append(self.get_content_item("text", string))
            elif isinstance(child, Tag):
                if child.name == "img":
                    src = self.get_img_src(child)
                    if src:
                        content.append(self.get_content_item("image", src))
                elif child.name == "div" or child.img or child.br:
                    self.parse_content_tag(child, content)
                elif child.get_text().strip():
                    string = str(child)
                    if child.name not in self.remove_tag_name_list:
                        string = "<p>" + string + "</p>"
                    content.append(self.get_content_item("text", string))
            else:
                pass
        self.clean_content(content)

    def clean_content(self, content):
        for index, item in enumerate(content):
            for key, value in item.items():
                if key == "text":
                    content[index][key] = self.remove_tag_name(
                        value, self.remove_tag_name_list
                    )


class RegularExtractor(GeneralExtractor):

    def parse_content_tag(self, tag, content):
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child).strip()
                if string:
                    string = "<p>" + string + "</p>"
                    content.append(self.get_content_item("text", string))
            elif isinstance(child, Tag):
                if child.name == "img":
                    src = self.get_img_src(child)
                    if src:
                        content.append(self.get_content_item("image", src))
                elif child.img:
                    self.parse_content_tag(child, content)
                elif child.get_text().strip():
                    string = str(child)
                    if child.name != "p":
                        string = "<p>" + string + "</p>"
                    content.append(self.get_content_item("text", string))
                else:
                    pass
            else:
                pass


class YiDianZiXunExtractor(GeneralExtractor):
    title_param = {"name": "h2", "attrs": dict()}
    post_date_param = {"name": None, "attrs": dict()}
    post_user_param = {"name": "a", "attrs": dict(id="source-name")}
    summary_param = {"name": None, "attrs": dict()}
    content_param = {"name": None, "attrs": dict()}


class TouTiaoExtractor(GeneralExtractor):
    title_param = {"name": "h1", "attrs": dict()}
    post_date_param = {"name": None, "attrs": dict()}
    post_user_param = {"name": None, "attrs": dict()}
    summary_param = {"name": None, "attrs": dict()}
    content_param = {"name": None, "attrs": dict()}



