#!/usr/bin/env python3

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'multipurpose matrix bot'
# Setting up
setup(
    name="dessertbot",
    version=VERSION,
    author="no-budy",
    author_email="<nobudy@nobudy.xyz>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['simplematrixbotlib', 'pyyaml', 'urlextract', 'beautifulsoup4', 'requests', 'urlextract' ],
    keywords=['python', 'matrix', 'bot', 'web scraper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
