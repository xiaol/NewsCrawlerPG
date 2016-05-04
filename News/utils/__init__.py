# coding: utf-8


from importlib import import_module
import urllib
from StringIO import StringIO
from PIL import Image
import logging
import zbarlight

_logger = logging.getLogger(__file__)


def load_object(path):
    """Load an object given its absolute object path, and return it.

    object can be a class, function, variable o instance.
    path ie: 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware'
    """

    try:
        dot = path.rindex('.')
    except ValueError:
        raise ValueError("Error loading object '%s': not a full path" % path)

    module, name = path[:dot], path[dot+1:]
    mod = import_module(module)

    try:
        obj = getattr(mod, name)
    except AttributeError:
        raise NameError("Module '%s' doesn't define any object named '%s'" % (module, name))

    return obj


class QR(object):

    @staticmethod
    def download_image(url):
        try:
            data = urllib.urlopen(url).read()
        except IOError as e:
            _logger.warn("qr %s" % e.message)
            return None
        else:
            return StringIO(data)

    @staticmethod
    def _is_qr_image(fd):
        try:
            image = Image.open(fd)
            image.load()
        except IOError as e:
            _logger.warn("qr %s" % e.message)
            qrs = []
        else:
            qrs = zbarlight.scan_codes("qrcode", image)
            if qrs is None:
                return False
        return len(qrs) > 0

    @classmethod
    def is_qr_image(cls, url):
        fd = cls.download_image(url)
        if fd is None:
            _logger.warn("qr download image error")
            return False
        else:
            return cls._is_qr_image(fd)


