# coding: utf-8

from datetime import datetime
import unittest
from News.extractor import GeneralExtractor

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 16:26"


class TestCleanPostDate(unittest.TestCase):

    def setUp(self):
        now = datetime.now()
        self.year_now = now.strftime("%Y")
        self.hour_now = now.strftime("%H")
        self.minute_now = now.strftime("%M")

    def test_normal_datetime(self):
        string = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(string, cleaned)

    def test_normal_second(self):
        string = "2016-07-30 15:14"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(string, cleaned)

    def test_normal_time(self):
        string = "2016-07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(string, cleaned)

    def test_normal_year_time(self):
        string = "07-30"
        expect = self.year_now + "-" + string
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_dot_datetime(self):
        string = "2016.07.30 15:14:20"
        expect = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_dot_second(self):
        string = "2016.07.30 15:14"
        expect = "2016-07-30 15:14"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_dot_time(self):
        string = "2016.07.30"
        expect = "2016-07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_dot_year_time(self):
        string = "07.30"
        expect = self.year_now + "-" + "07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_p_datetime(self):
        string = "2016/07/30 15:14:20"
        expect = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_p_second(self):
        string = "2016/07/30 15:14"
        expect = "2016-07-30 15:14"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_p_time(self):
        string = "2016/07/30"
        expect = "2016-07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_p_year_time(self):
        string = "07/30"
        expect = self.year_now + "-" + "07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_chinese_datetime(self):
        string = "2016年07月30日 15:14:20"
        expect = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_chinese_second(self):
        string = "2016年07月30日 15:14"
        expect = "2016-07-30 15:14"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_chinese_time(self):
        string = "2016年07月30日"
        expect = "2016-07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_chinese_year_time(self):
        string = "07月30"
        expect = self.year_now + "-" + "07-30"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_one_digit_month_chinese_datetime(self):
        string = "2016年7月30日 15:14:20"
        expect = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_day_chinese_datetime(self):
        string = "2016年07月1日 15:14:20"
        expect = "2016-07-01 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_month_day_chinese_datetime(self):
        string = "2016年7月1日 15:14:20"
        expect = "2016-07-01 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_month_normal_datetime(self):
        string = "2016-7-30 15:14:20"
        expect = "2016-07-30 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_day_normal_datetime(self):
        string = "2016-12-3 15:14:20"
        expect = "2016-12-03 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_month_day_chinese_year(self):
        string = "7月1日 15:14:20"
        expect = "2016-07-01 15:14:20"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertEqual(expect, cleaned)

    def test_one_digit_month_day_chinese_datetime_year(self):
        string = "7月1日"
        expect = self.year_now + "-" + "07-01"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_one_digit_month_day_datetime_year_two_month(self):
        string = "12-1"
        expect = self.year_now + "-" + "12-01"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_one_digit_month_datetime_year(self):
        string = "1-12"
        expect = self.year_now + "-" + "01-12"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

    def test_one_digit_month_day_datetime_year(self):
        string = "1-1"
        expect = self.year_now + "-" + "01-01"
        cleaned = GeneralExtractor.clean_post_date(string)
        self.assertIn(expect, cleaned)

if __name__ == '__main__':
    unittest.main()
