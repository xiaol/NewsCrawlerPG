# coding: utf-8

"""
单元测试
"""

import unittest
from News.test.static_or_class_methods import TestCleanPostDate

from scrapy import cmdline


def unit_test():
    unittest.main()


def debug_spider():
    argv = "scrapy crawl spider:news:www_jrj_com_cn".split()
    cmdline.execute(argv)


if __name__ == '__main__':
    debug_spider()

