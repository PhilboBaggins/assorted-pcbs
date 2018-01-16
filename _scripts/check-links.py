#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
import sys
import pmap
import requests
from common import *

githubUrlFinder = re.compile(r'https?:\/\/github.com\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')


def checkUrls(projDir):
    upverterUrl = getUpverterUrl(projDir)
    if not upverterUrl:
        return 'No Upverter URL found in documentation for ' + pathRelToRepo(projDir)

    upverterRes = requests.get(upverterUrl)
    if upverterRes.status_code != 200:
        return 'Upverter URL  may not be valid: ' + upverterRes + ' - status code = ' + str(upverterRes.githubRes.status_code)

    htmlData = upverterRes.text
    match = githubUrlFinder.search(htmlData)
    if not match:
        return 'No Github URL found on Upverter page for ' + pathRelToRepo(projDir)

    githubURL = match.group(0)
    githubRes = requests.head(githubURL)
    if githubRes.status_code != 200:
        return 'Github URL may not be valid: ' + githubURL + ' - status code = ' + str(githubRes.status_code)


def main(targetDirs):
    errorMsgs = pmap.pmap(checkUrls, targetDirs)
    for msg in errorMsgs:
        if msg:
            print(msg)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        targetDirs = sys.argv[1:]
    else:
        targetDirs = list(projectDirectories())

    main(targetDirs)
