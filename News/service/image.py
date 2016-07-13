# coding: utf-8

import hashlib
from StringIO import StringIO
from PIL import Image
import logging
import zbarlight

from News.utils.cache import Cache
from News.utils import http

_logger = logging.getLogger(__file__)

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-05-06 11:19"


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36"
           }
image_service_key = "service:news:image:md5"


def download_image(url):
    r = http.get(url, headers=headers)
    if not r:
        return None
    if r.status_code >= 400:
        _logger.warn("download image error: %s" % r.status_code)
        return None
    else:
        return r.content


def is_qr_image(fd):
    qrs = list()
    try:
        image = Image.open(fd)
        image.load()
    except IOError as e:
        _logger.warn("qr %s" % e.message)
    else:
        qrs = zbarlight.scan_codes("qrcode", image)
        if qrs is None:
            return False
    return len(qrs) > 0


def is_ad_image(raw):
    value = hashlib.md5(raw).hexdigest()
    return Cache.sismember(image_service_key, value)


def is_ad_image_url(url):
    return Cache.sismember(image_service_key, url)


def is_dirty_image(url):
    if is_ad_image_url(url):
        return True
    raw = download_image(url)
    if raw is None:
        return False
    else:
        return is_qr_image(StringIO(raw)) or is_ad_image(raw)
