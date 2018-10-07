#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function
import sys
from six.moves import range
from six.moves import input
import datetime

__version__ = '0.1.0'

TEMPLATE = r'''
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
    projName = 'Project name'  # TODO: Ask user
    projDesc = 'Project description'  # TODO: Ask user
    projUpverterURL = 'URL URL URL'  # TODO: Ask user
    projCopyrightYear = str(datetime.datetime.now().year)
    readmeData = TEMPLATE \
        .replace('{name}', projName) \
        .replace('{description}', projDesc) \
        .replace('{upverter-url}', projUpverterURL) \
        .replace('{copyright-year}', projCopyrightYear)
    print(readmeData)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    #parser.add_argument('path')
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
