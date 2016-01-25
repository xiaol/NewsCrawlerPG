import json
from time import strftime, localtime


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
