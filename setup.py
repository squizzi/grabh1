#!/usr/bin/env python
import os
import sys
from setuptools import setup

""" Setuptools for install """
with open('requirements.txt') as r:
    required = r.read().splitlines()

setup(
    name='GrabH1',
    version='1.0',
    description="Autokey script which grabs the page title of a web page and inserts it above the selected link text",
    long_description=open('README.md').read(),
    author='Kyle Squizzato',
    author_email='ksquizz@gmail.com',
    license='GNU General Public License Version 3',
    url='https://github.com/squizzi/grabh1',
    setup_requires = required,
    install_requires = required,
)
