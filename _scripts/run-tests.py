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
                    problemFile = os.path.relpath(os.path.join(projDir, 'Upverter exports', name), TOP_DIR)
                    print('*', 'Not found:', problemFile)
            #upverterExportsCheck('3d model.stl')
            upverterExportsCheck('Gerbers')
            upverterExportsCheck('Schematic.asc')
            upverterExportsCheck('Schematic.pdf')
            upverterExportsCheck('Schematic.png')
            upverterExportsCheck('Schematic.svg')
            upverterExportsCheck('Upverter project.upv')


def checkPcbsIoExports(targetDirs):
    print()
    print('## Checking pcbs.io export directories')
    print()

    pcbIoDirs = [os.path.join(projDir, 'pcbs.io') for projDir in targetDirs
                if os.path.isdir(os.path.join(projDir, 'pcbs.io'))]

    for pcbsIoDir in pcbIoDirs:
        contents = os.listdir(pcbsIoDir)
        def pcbsIoExportsCheck(name):
            if name not in contents:
                problemFile = os.path.relpath(os.path.join(pcbsIoDir, name), TOP_DIR)
                print('*', 'Not found:', problemFile)
        pcbsIoExportsCheck('README.md')
        pcbsIoExportsCheck('top.svg')
        pcbsIoExportsCheck('bottom.svg')

    readmeHashes = [hashFile(dirPath, 'README.md') for dirPath in pcbIoDirs]
    if not all(x == readmeHashes[0] for x in readmeHashes):
        print("* All the pcbs.io/README.md files should be the same ... but they're not:")
        for hashStr, path in zip(readmeHashes, pcbIoDirs):
            print('    *', hashStr, os.path.relpath(path, TOP_DIR))


def checkBoardPhotosOrPlaceHolders(targetDirs):
    print()
    print('## Checking for board photos or placeholders')
    print()

    for projDir in targetDirs:
        contents = os.listdir(projDir)
        boardPhotoPresent = 'board-photo.jpg' in contents
        readmeData = fileContentsOrEmptyStr(projDir, 'README.md')
        boardPhotoInReadme = '![Board photo](./board-photo.jpg)' in readmeData
        placeHolderInReadme = '_common/PlaceholderImage.png' in readmeData

        def bad(msg):
            print('*', msg, 'in', os.path.relpath(projDir, TOP_DIR))

        if boardPhotoPresent and boardPhotoInReadme:
            pass  # Good!
        elif boardPhotoPresent:
            bad("Board photo exist but it isn't mentioned in the README file")
        elif boardPhotoInReadme:
            bad("Board photo is mentioned in the README file but the files doesn't exist")
        elif placeHolderInReadme:
            #bad('Only a place holder image')
            pass  # Good enough
        else:
            bad('No board photo nor place holder image')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        targetDirs = sys.argv[1:]
    else:
        targetDirs = list(projectDirectories())

    checkReadmeFiles(targetDirs)
    checkLicenceFiles(targetDirs)
    checkTODOEntries(targetDirs)
    checkUpverterExports(targetDirs)
    checkPcbsIoExports(targetDirs)
    checkBoardPhotosOrPlaceHolders(targetDirs)
