#!/usr/bin/env python

import os, sys
from setuptools import setup

if(sys.version_info.major < 3):
    print("You must be running python 3 for the setup to work")
    exit(1)

libFolder = os.path.dirname(os.path.realpath(__file__))
reqPath = libFolder + './requirements.txt'
install_requires=[]

if(os.path.isfile(reqPath)):
    with open(reqPath) as f:
        install_requires = f.read().splitlines()

setup(name='Email Scraper',
      version='1.0',
      description='Email scraper',
      author='danielmcnz',
      #packages=['email', 'dotenv'],
      install_requires=install_requires)