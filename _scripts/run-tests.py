#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
import sys
from common import *


def checkReadmeFiles(targetDirs):
    print()
    print('## Checking README.md files')
    print()

    for projDir in targetDirs:
        readmeFile = os.path.join(projDir, 'README.md')

        if not os.path.isfile(readmeFile):
            print('* No README.md file in', os.path.relpath(projDir, TOP_DIR))
            continue

        if not fileContains(readmeFile, '## Licence'):
            print('* No \"Licence\" heading in', os.path.relpath(readmeFile, TOP_DIR))

        if not fileContains(readmeFile, 'Copyright ©'):
            #print('*', os.path.relpath(readmeFile, TOP_DIR), 'does not contains a copyright symbol')
            #print('* "', os.path.relpath(readmeFile, TOP_DIR), '" does not contains a copyright symbol', sep='')
            #print('* No copyright symbol in "', os.path.relpath(readmeFile, TOP_DIR), '"', sep='')
            print('* No copyright symbol in', os.path.relpath(readmeFile, TOP_DIR))


def checkLicenceFiles(targetDirs):
    print()
    print('## Checking LICENCE.txt files')
    print()

    for projDir in targetDirs:
        licenceFile = os.path.join(projDir, 'LICENCE.txt')

        if not os.path.isfile(licenceFile):
            print('* No LICENCE.txt file in', os.path.relpath(projDir, TOP_DIR))
            continue

        if os.path.getsize(licenceFile) == 0:
            print('* LICENCE.txt in', os.path.relpath(projDir, TOP_DIR), 'is empty')


def checkTODOEntries(targetDirs):
    print()
    print('## Checking for TODO entries in README files')
    print()

    for projDir in targetDirs:
        readmeFile = os.path.join(projDir, 'README.md')
        if os.path.isfile(readmeFile):
            data = open(readmeFile, 'r').read()
            if 'TODO' in data:
                print('* TODO  entry in', os.path.relpath(readmeFile, TOP_DIR))
            if '???' in data:
                print('*  ???  entry in', os.path.relpath(readmeFile, TOP_DIR))
            if '.....' in data:
                print('* ..... entry in', os.path.relpath(readmeFile, TOP_DIR))
            elif '...' in data:
                print('*  ...  entry in', os.path.relpath(readmeFile, TOP_DIR))


def checkUpverterExports(targetDirs):
    print()
    print('## Checking Upverter exports directories')
    print()

    for projDir in targetDirs:
        upverterExportDir = os.path.join(projDir, 'Upverter exports')
        if os.path.isdir(upverterExportDir):
            contents = os.listdir(upverterExportDir)
            def upverterExportsCheck(name):
                if name not in contents:
                    problemDir = os.path.relpath(os.path.join(projDir, 'Upverter exports', name), TOP_DIR)
                    print('*', 'Not found:', problemDir)
            #upverterExportsCheck('3d model.stl')
            upverterExportsCheck('Gerbers')
            upverterExportsCheck('Schematic.asc')
            upverterExportsCheck('Schematic.pdf')
            upverterExportsCheck('Schematic.png')
            upverterExportsCheck('Schematic.svg')
            upverterExportsCheck('Upverter project.upv')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        targetDirs = sys.argv[1:]
    else:
        targetDirs = list(projectDirectories())

    checkReadmeFiles(targetDirs)
    checkLicenceFiles(targetDirs)
    checkTODOEntries(targetDirs)
    checkUpverterExports(targetDirs)
