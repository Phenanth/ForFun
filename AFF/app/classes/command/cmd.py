# -*- coding: utf-8 -*-
import subprocess
from setuptools import Command

from ..downloader import common

"""
cmd.py
~~~~~~~~~~~~~~~~~~~~~~~~

Classes about extended commands for setup.py

command_server: python setup.py run
command_docker: python setup.py docker

"""


# For directly running the server from the command line.
class command_server(Command):

    user_options = []

    def initialize_options(self):

        common.init_folder()

    def finalize_options(self):
        pass

    def run(self):
        
        cmd = "python -m api.__main__"
        returncode = subprocess.call(cmd)

# For BUILD & START a docker container.
class command_docker(Command):

    user_options = []

    def initialize_options(self):

        common.init_folder()
        
        cmd = "docker build ./ -t pythonapi"
        returncode = subprocess.call(cmd)

    def finalize_options(self):
        pass

    def run(self):

        cmd = "docker run --name test -d -it -p 8210:8210 pythonapi"
        returncode = subprocess.call(cmd)
