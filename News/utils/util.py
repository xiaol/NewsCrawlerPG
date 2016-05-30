# coding: utf-8

import json
from datetime import datetime
import re
from urlparse import urlparse, parse_qs
from time import strftime, localtime
import base64
from News.utils import http
from News.utils.cache import Cache
from News.constans.useragent import WEB_USER_AGENT


def load_json_data(data):
    try:
        d = json.loads(data)
    except:
        return None
    else:
        return d


def str_from_timestamp(timestap):
    time_format = "%Y-%m-%d %H:%M:%S"
    return strftime(time_format, localtime(timestap))


def get_query_from_url(url, key):
    string = urlparse(url).query
    params = parse_qs(qs=string)
    values = params.get(key, [])
    if len(values) != 1:
        return None
    else:
        return values[0]


def news_already_exists(key):
    boolean = Cache.exist(key)
    return boolean


def g_cache_key(string):
    return "news:" + base64.urlsafe_b64encode(string).replace("=", "")


def clean_date_time(string):
    """清洗时间

    :param string: 包含要清洗时间的字符串
    :type string: str
    :return: 生成的字符串, 格式为 2016-02-01 12:01:59
    :rtype: str
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
        time_groups = (hour_now, minute_now, ":" + second_now, second_now)
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


def get_document(url):
    netloc = urlparse(url).netloc
    headers = {"user-agent": WEB_USER_AGENT[0],
               "host": netloc}
    r = http.get(url, headers=headers)
    if not r:
        return ''
    if r.status_code == 200:
        encoding = r.apparent_encoding
        if encoding.lower() == "gb2312":
            encoding = "GB18030"
            return r.content.decode(encoding).encode("utf-8")
        else:
            return r.content
    else:
        print("get document error: %s" % r.status_code)
        return ""


_A_PATTERN = r'<a href="([^<]*)">([^<]*)</a>'
_P_A_PATTERN = re.compile(_A_PATTERN)


def replace_a_href_to_ours(string):
    page_words = [u"上一页", u"下一页"]
    for m in _P_A_PATTERN.finditer(string):
        href = m.group(1)
        text = m.group(2)
        if href and text and href.startswith("http"):
            if text.isdigit() or text.startswith("http"):
                continue
            elif text in page_words:
                continue
            else:
                url = "http://deeporiginalx.com/search.html#sw=" + text
                string = string.replace(href, url)
    return string

