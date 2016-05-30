# coding: utf-8

import json
import requests

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-11 11:39"


def get(url, params=None):
    try:
        r = requests.get(url, timeout=30, params=params)
    except Exception as e:
        pass
    else:
        return json.loads(r.content)


def post(url, data=None):
    try:
        r = requests.post(url, timeout=30, data=data)
    except Exception as e:
        pass
    else:
        return json.loads(r.content)


def daemon_status(domain):
    url = domain + "daemonstatus.json"
    return get(url)


def add_version(domain, project, version, egg):
    url = domain + "addversion.json"
    data = {
        "project": project,
        "version": version,
        "egg": egg
    }
    return post(url, data)


def schedule(domain, project, spider, setting=None,
             jobid=None, _version=None, **kwargs):
    url = domain + "schedule.json"
    data = {
        "project": project,
        "spider": spider,
    }
    if setting is not None:
        data["setting"] = setting
    if jobid is not None:
        data["jobid"] = jobid
    if _version is not None:
        data["_version"] = _version
    data.update(kwargs)
    return post(url, data)


def cancel(domain, project, job):
    url = domain + "cancel.json"
    data = {
        "project": project,
        "job": job,
    }
    return post(url, data)


def list_projects(domain):
    url = domain + "listprojects.json"
    return get(url)


def list_versions(domain, project):
    url = domain + "listversions.json"
    params = {
        "project": project,
    }
    return get(url, params)


def list_spiders(domain, project, _version=None):
    url = domain + "listspiders.json"
    params = {
        "project": project,
    }
    if _version is not None:
        params["_version"] = _version
    return get(url, params)


def list_jobs(domain, project):
    url = domain + "listjobs.json"
    params = {
        "project": project,
    }
    return get(url, params)


def del_version(domain, project, version):
    url = domain + "delversion.json"
    data = {
        "project": project,
        "version": version,
    }
    return post(url, data)


def del_project(domain, project):
    url = domain + "delproject.json"
    data = {
        "project": project,
    }
    return post(url, data)




