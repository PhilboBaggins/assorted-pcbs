#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
import re
import hashlib

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TOP_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))

upverterUrlRegex = re.compile(r'https?:\/\/upverter.com\/(.*)\/')


def realBaseName(dirPath):
    return os.path.basename(os.path.realpath(dirPath))


def projectDirectories():
    for item in os.listdir(TOP_DIR):
        if item in ['.git', '_scripts', '_common']:
            continue
        item = os.path.join(TOP_DIR, item)       
        if os.path.isdir(item):
            yield item


def getUpverterUrl(projDir):
    readmeFile = os.path.join(projDir, 'README.md')
    if os.path.isfile(readmeFile):
        readmeData = open(readmeFile, 'r').read()
        matches = upverterUrlRegex.search(readmeData)
        if matches:
            return matches.group(0)


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


def fileContentsOrEmptyStr(*args):
    filePath = os.path.join(*args)
    try:
        return open(filePath).read()
    except IOError:
        return ''


def pathRelToRepo(inputPath):
    return os.path.relpath(inputPath, TOP_DIR)


def filesInDir(dirName):
    return [f for f in os.listdir(dirName) if os.path.isfile(os.path.join(dirName, f))]
