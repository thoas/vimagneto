#fab -f fabfile.py <command>

from __future__ import with_statement

import os
from fabric.api import *
from fabric.contrib import project

# I have entries in /etc/hosts which make these names work. 
# If I didn't, I'd just use IP addresses.
env.hosts = ['kaltorak']
env.user = 'webadmin'
env.project_name = 'vimagneto'

#paths
env.root = "/var/www/%s" % env.project_name

# local
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
BUILD_PATH = os.path.join(ROOT_PATH, '_build/')

def build():
    local('run-rstblog build')

def runserver():
    local('run-rstblog serve')

def clean():
    local('rm -rf %s' % BUILD_PATH)

def publish():
    clean()
    build()
    project.rsync_project(
        remote_dir=env.root,
        local_dir=BUILD_PATH,
        delete=True
    )

def init():
    clean()
    build()
    runserver()
