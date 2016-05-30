import requests


def get(url, params=None, timeout=30, **kwargs):
    try:
        r = requests.get(url, params=params, timeout=timeout, **kwargs)
    except Exception as e:
        r = None
    finally:
        return r


def post(url, params=None, timeout=30, **kwargs):
    try:
        r = requests.post(url, params=params, timeout=timeout, **kwargs)
    except Exception as e:
        r = None
    finally:
        return r

