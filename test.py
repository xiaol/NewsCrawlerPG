# coding: utf-8

import sys
from News.test.extractor import test_extractor


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python test.py [ge, re, we] url")
        print("ge: general extractor")
        print("re: regular extractor")
        print("we: wechat extractor")
    else:
        key = sys.argv[1]
        url = sys.argv[2]
        test_extractor(key, url)

