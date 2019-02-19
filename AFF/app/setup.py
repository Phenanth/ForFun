# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import docs
import api

from classes.downloader import common
from classes.command.cmd import command_server, command_docker

"""
setup.py
~~~~~~~~~~~~~~~~~~~~~~~~

The command line interface of the project.
For usage, you can run `python setup.py --long_description` in the command line, or check the `README.md`
"""


def main():

    readme = common.readfile(docs.config.README)

    setup(
        name='affapi',
        version='1.0.0',
        description='API for wrapped fan fic API',
        long_description=readme,
        # author='Kenneth Reitz',
        # author_email='me@kennethreitz.com',
        # url='https://github.com/kennethreitz/samplemod',
        # license=license,
        install_requires=["flask", "requests"],
        packages=find_packages(exclude=('tests', 'docs')),
        cmdclass={"run": command_server, "docker": command_docker}
    )

if __name__ == "__main__":
    main()
