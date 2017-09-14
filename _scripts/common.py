#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
import hashlib

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TOP_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))


def projectDirectories():
    for item in os.listdir(TOP_DIR):
        if item in ['.git', '_scripts']:
            continue
        item = os.path.join(TOP_DIR, item)       
        if os.path.isdir(item):
            yield item



#
# Helper functions
#

#def pathExists(*args):
#    path = os.path.join(*args)
#    return os.path.exists(path):


def fileContains(file, expectedContents):
    fileContents = open(file, 'r').read()
    return expectedContents in fileContents


def hashFile(*args):
    filePath = os.path.join(*args)
    if not os.path.exists(filePath):
        return None
    hasher = hashlib.md5()
    with open(filePath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()
