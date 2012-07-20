#!/usr/bin/env python

import os
from setuptools import setup

def strip_comments(l):
    return l.split("#", 1)[0].strip()

def reqs(f):
    return filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), f)).readlines()])

setup(
    name = "kombu-multibroker",
    version = "0.0.1",
    author = "Rick Branson",
    author_email = "rick@diodeware.com",
    description = ("Support for multiple brokers in Kombu"),
    license = "BSD",
    keywords = "kombu broker amqp",
    url = "http://github.com/rbranson/kombu-multibroker",
    packages = ["kombu_multibroker"],
    long_description = "Support for multiple brokers in Kombu",
    install_requires = reqs("requirements.txt"),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Jython",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
