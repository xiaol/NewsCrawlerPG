# coding: utf-8

import api

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-11 14:32"


NODES = {
    "local": "http://localhost:6800/",
}


def list_nodes():
    for name, domain in NODES.items():
        print(name)


def list_projects(node_name):
    domain = NODES[node_name]
    r = api.list_projects(domain)
    if r.get("status") != "ok":
        print("list projects error: %s" % node_name)
        return []
    else:
        return r["projects"]


def list_spiders(node_name, project_name):
    domain = NODES[node_name]
    r = api.list_spiders(domain, project=project_name)
    if r.get("status") != "ok":
        print("list spiders error: %s.%s" % (node_name, project_name))
        return []
    else:
        return r["spiders"]


def list_jobs(node_name, project_name):
    domain = NODES[node_name]
    r = api.list_jobs(domain, project=project_name)
    if r.get("status") != "ok":
        print("list jobs error: %s.%s" % (node_name, project_name))
        return [], [], []
    else:
        pendings = r["pending"]
        runnings = r["running"]
        finisheds = r["finished"]
        return pendings, runnings, finisheds


def run_spider(node_name, project_name, spider):
    domain = NODES[node_name]
    r = api.schedule(domain, project_name, spider)
    if r.get("status") != "ok":
        print("run spider %s failed" % spider)
    else:
        print("run spider %s success, jobid is %s" % (spider, r["jobid"]))


def run_spiders(node_name, project_name, spiders):
    for spider in spiders:
        run_spider(node_name, project_name, spider)


def stop_spider(node_name, project_name, jobid):
    domain = NODES[node_name]
    r = api.cancel(domain, project_name, jobid)
    if r.get("status") != "ok":
        print("stop spider %s failed" % jobid)
    else:
        print("stop spider %s success" % jobid)


def stop_spiders(node_name, project_name, jobids):
    for jobid in jobids:
        stop_spider(node_name, project_name, jobid)


def show_header():
    start_string = "*" * 25 + "scrapyd schedule" + "*" * 25
    print(start_string)


def show_nodes(nodes):
    print("\nNodes:")
    for name, domain in nodes.items():
        print("\tName: %s \tDomain: %s" % (name, domain))


def show_projects(projects):
    print("\nProjects:")
    for project in projects:
        print("\tName: %s" % project)


def show_spiders(spiders):
    print("\nSpiders:")
    for index, spider in enumerate(spiders):
        print("\t%s. %s" % (index, spider))


def show_spider_command():
    print("\nSpider Commands:")
    print("""
        1. job status
        2. run spiders
        3. run all spiders
        4. stop spider
        5. stop all spiders
        """)


def show_jobs(pendings, runnings, finisheds):
    print("\tPending %s:" % len(pendings))
    for pending in pendings:
        print("\t\tName: %s Id: %s" % (pending["spider"], pending["id"]))
    print("\tRunning %s:" % len(runnings))
    for running in runnings:
        print("\t\tName: %s Id: %s Start: %s" % (running["spider"],
                                                 running["id"],
                                                 running["start_time"]))
    print("\tFinished %s:" % len(finisheds))
    for finished in finisheds:
        print("\t\tName: %s Id: %s Start: %s, End: %s" % (finished["spider"],
                                                          finished["id"],
                                                          finished["start_time"],
                                                          finished["end_time"]))


def show_job_command():
    print("\nJob Commands:")
    print("""
        1. stop spiders
        2. stop all spiders
        """)


if __name__ == '__main__':
    while True:
        show_header()
        show_nodes(NODES)
        node_name = raw_input("please input node name: ").strip()
        if node_name not in NODES:
            break
        projects = list_projects(node_name)
        show_projects(projects)
        project_name = raw_input("please input project name: ").strip()
        if project_name not in projects:
            break
        spiders = list_spiders(node_name, project_name)
        show_spiders(spiders)
        while True:
            show_spider_command()
            cmd = int(raw_input("please input command index: ").strip())
            if cmd == 0:
                break
            elif cmd == 1:
                ps, rs, fs = list_jobs(node_name, project_name)
                show_jobs(ps, rs, fs)
                show_job_command()
                job_cmd = int(raw_input("please input job command index: ").strip())
                if job_cmd == 1:
                    job_ids = raw_input("please input job ids(split by ','):").strip().split(",")
                    stop_spiders(node_name, project_name, job_ids)
                elif job_cmd == 2:
                    job_ids = []
                    job_ids.extend([job["id"] for job in ps])
                    job_ids.extend([job["id"] for job in rs])
                    stop_spiders(node_name, project_name, job_ids)
                else:
                    continue
            elif cmd == 2:
                indexes = raw_input("please input spider index(split by ','): ").strip().split(",")
                spider_names = [spiders[int(i)] for i in indexes]
                run_spiders(node_name, project_name, spider_names)
            elif cmd == 3:
                pass
            elif cmd == 4:
                indexes = raw_input("please input spider index(split by ','): ").strip().split(",")
                spider_names = [spiders[int(i)] for i in indexes]
                stop_spiders(node_name, project_name, spider_names)
            else:
                break







