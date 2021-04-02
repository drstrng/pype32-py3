#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Nahuel Riva
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__revision__ = "$Id$"

__all__ = ['metadata', 'setup']

from distutils.core import setup
from distutils import version
from warnings import warn

import re
import os
import sys
import glob

if sys.version_info < (3,):
    sys.exit('Sorry, Python 3 is required.  For python2 version see https://github.com/crackinglandia/pype32')

# Get the base directory
here = os.path.dirname(__file__)
if not here:
    here = os.path.curdir

long_description = """pype32 is python library to read and write PE/PE+ binary files."""

# Get the list of scripts in the "tools" folder
scripts = glob.glob(os.path.join('tools', '*.py'))

# Set the parameters for the setup script
metadata = {

    # Setup instructions
    'provides'          : ['pype32'],
    'packages'          : ['pype32'],
    'scripts'           : scripts,

    # Metadata
    'name'              : 'pype32-py3',
    'version'           : 'v0.2',
    'description'       : 'Yet another Python library to read and write PE/PE+ files.',
    'long_description'  : long_description,
    'url'               : 'https://github.com/drstrng/pype32-py3',
    'download_url'      : 'https://github.com/drstrng/pype32-py3/archive/v0.2.tar.gz',
    'keywords'          : ['pecoff', 'x86', 'x64', '.net', 'parser'],
    }

# Execute the setup script
if __name__ == '__main__':
    setup(**metadata)
