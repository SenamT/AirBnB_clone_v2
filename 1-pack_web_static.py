#!/usr/bin/python3
""" this is a fabric script that will generate a .tgz archive """
from fabric.decorators import task
from fabric.api import local
from datetime import datetime


@task
def do_pack():
    """this will generate a .tgz archive from web_static"""
    datestr = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(datestr)
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static/".format(file_name)).succeeded:
        return file_name
    return None
