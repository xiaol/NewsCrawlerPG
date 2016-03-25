# coding: utf-8

from urlparse import urlparse
import requests
from lxml import etree
from lxml import html

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


def extract(string):
    root = html.document_fromstring(string)
    for child in root.iter():
        print(child.tag)


if __name__ == '__main__':
    string = """<html><head><title>Test</title></head><body><h2>Hello World</h2></body></html>"""
    # string = get_document("")
    extract(string=string)

# coding: utf-8

#set($MYNAME = "Sven Lee")
__author__ = "${MYNAME}"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["${MYNAME}"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "${YEAR}-${MONTH}-${DAY} ${HOUR}:${MINUTE}"


