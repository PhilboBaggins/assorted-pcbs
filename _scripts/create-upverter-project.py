#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import os
from six.moves import range
from six.moves import input
import datetime
import shutil
import common

__version__ = '0.1.0'

TEMPLATE = '''
# {name}

<img align="right" src="../_common/PlaceholderImage.png">

{description}

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here]({upverter-url}). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

## Licence

Copyright © {copyright-year} Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
'''


def main(verbose=0):
    commonLicenceFile = os.path.join(common.TOP_DIR, 'Breadboard buttons - 1x5', 'LICENCE.txt')
    commonPcbIOReadme = os.path.join(common.TOP_DIR, 'Breadboard buttons - 1x5', 'pcbs.io', 'README.md')

    projName = input('Project name: ')
    projDesc = input('Project description: ')
    projUpverterURL = input('Upverter URL: ')  # TODO: Check with common.upverterUrlRegex

    projCopyrightYear = str(datetime.datetime.now().year)
    projDir = os.path.join(common.TOP_DIR, projName)
    projUpvExportsDir = os.path.join(projDir, 'Upverter exports')
    projUpvExportsGerbersDir = os.path.join(projDir, 'Upverter exports', 'Gerbers')
    projPcbsIoDir = os.path.join(projDir, 'pcbs.io')
    projReadmeFile = os.path.join(projDir, 'README.md')

    if os.path.exists(projDir):
        print(projDir, 'already exists. Aborting ...')
        return

    os.makedirs(projDir)
    os.makedirs(projUpvExportsDir)
    os.makedirs(projPcbsIoDir)
    os.makedirs(projUpvExportsGerbersDir)

    shutil.copy2(commonLicenceFile, projDir)
    shutil.copy2(commonPcbIOReadme, projPcbsIoDir)

    readmeData = TEMPLATE \
        .replace('{name}', projName) \
        .replace('{description}', projDesc) \
        .replace('{upverter-url}', projUpverterURL) \
        .replace('{copyright-year}', projCopyrightYear) \
        .lstrip()
    with open(projReadmeFile, 'w') as f:
        f.write(readmeData)


if __name__ == '__main__':
    import sys
    from argparse import ArgumentParser
    parser = ArgumentParser()
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
        main(verbose=args.verbose)
    except KeyboardInterrupt:
        print('Keyboard interrupt received, exiting...', file=sys.stderr)
