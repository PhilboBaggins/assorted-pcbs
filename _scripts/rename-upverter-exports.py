#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
from six.moves import range
from six.moves import input
import datetime
import zipfile
import common

__version__ = '0.1.0'


GERBERS_DIR = 'Gerbers'

DESIRED_FILE_NAMES = {
    '3d-model': '3D model.stp',
    'assembly-drawing': 'Assembly drawing.svg',
    'dimension-drawing': 'Dimension drawing.svg',
    'upverter-project': 'Upverter project.upv',
    'schematic-asc': 'Schematic.asc',
    'schematic-pdf': 'Schematic.pdf',
    'schematic-png': 'Schematic.png',
    'schematic-svg': 'Schematic.svg',
}


def rename(oldfile, newName, verbose=0):
    if verbose > 0:
        print('Renaming', file, 'to', newName)
    os.rename(oldfile, newName)


def findFileInList(partOfFileName, fileList):
    for file in fileList:
        if partOfFileName in file:
            return file
    # Not found
    return None


def handleGerberZipFile(gerberZipFile, projName, verbose=0):
    corruptedProjName = projName.replace(' ', '-').lower()

    with zipfile.ZipFile(gerberZipFile, 'r') as zipFile:
        zipFile.extractall(GERBERS_DIR)

    os.chdir(GERBERS_DIR)

    for file in os.listdir('.'):
        if 'design_export' in file:
            _, fileExt = os.path.splitext(file)
            rename(file, corruptedProjName + fileExt)

    with open('layers.cfg', 'r+') as f:
        data = f.read()
        data = data.replace('design_export', corruptedProjName)
        f.seek(0)
        f.write(data)

    os.chdir('..')
    os.remove(gerberZipFile)


def main(dirWithFiles, verbose=0):
    os.chdir(dirWithFiles)

    projName = os.path.basename(os.path.abspath('../'))
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in DESIRED_FILE_NAMES.values()]

    def aaa(partOfOldName, newName):
        file = findFileInList(partOfOldName, files)
        if file:
            rename(file, newName)
            files.remove(file)
        else:
            print('Unable to find file to rename to', newName)

    aaa('populated_step.stp',   DESIRED_FILE_NAMES['3d-model'])
    aaa('assemblydrawing.svg',  DESIRED_FILE_NAMES['assembly-drawing'])
    aaa('dimensiondrawing.svg', DESIRED_FILE_NAMES['dimension-drawing'])
    aaa('openjson.upv',         DESIRED_FILE_NAMES['upverter-project'])
    aaa('pads_netlist.asc',     DESIRED_FILE_NAMES['schematic-asc'])

    assert(len(files) <= 3)
    aaa('.pdf', DESIRED_FILE_NAMES['schematic-pdf'])
    aaa('.png', DESIRED_FILE_NAMES['schematic-png'])
    aaa('.svg', DESIRED_FILE_NAMES['schematic-svg'])

    gerberZipFile = findFileInList('gerber.zip', files)
    if gerberZipFile:
        handleGerberZipFile(gerberZipFile, projName)
        files.remove(gerberZipFile)
    else:
        print('Unable to find gerber zip file')

    print('Unhandled files:')
    for file in files:
        print('*', file)


if __name__ == '__main__':
    import sys
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('-v', '--verbose',
                        action='count',
                        dest='verbose',
                        default=0,
                        help='Verbose output')
    args = parser.parse_args()

    try:
        main(args.path, verbose=args.verbose)
    except KeyboardInterrupt:
        print('Keyboard interrupt received, exiting...', file=sys.stderr)
