from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
INPUT_PATH = env.input_path

# Remote server configuration
production = 'blog@blog.skylines-project.org:23467'
dest_path = '/var/www/skylines-blog'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican {input_path} -s pelicanconf.py'.format(**env))

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican {input_path} -r -s pelicanconf.py'.format(**env))

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican {input_path} -s publishconf.py'.format(**env))

@hosts(production)
def publish():
    local('pelican {input_path} -s publishconf.py'.format(**env))
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='--chmod=Du=rwx,Dg=rx,Do=rx,Fu=rw,Fg=r,Fo=r',
    )
