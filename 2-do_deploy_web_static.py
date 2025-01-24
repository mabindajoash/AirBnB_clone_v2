#!/usr/bin/python3
#distribute the archive to the webservers

from fabric import *
def do_deploy(archive_path):
    if os.path.exists(archive_path) is false:
        return false
    file_name = os.path.splitext(os.path.basename(archive_path))[0]
    env.hosts = ["ubuntu@3.89.146.72", "ubuntu@54.160.100.82"]
    if put("{}, /tmp/".format(archive_path)).failed:
        if run("tar -xzf tmp/{} /data/web_static/releases/{}".format(archive_path, file_name)).failed:
            if run("rm -f {}".format(/tmp/archive_path)).failed:
                return False
    if run("rm -f /data/web_static/current").failed:
        if run("ln -s {} /data/web_static/current /data/web_static/releases/{}".format(file_name)).failed
            return False
    return True
