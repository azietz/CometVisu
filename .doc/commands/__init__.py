#!/usr/bin/python
# -*- coding: utf-8 -*-

# copyright (c) 2010-2016, Christian Mayer and the CometVisu contributers.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA
import os
import ConfigParser


class Command(object):

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join('.doc', 'config.ini'))
        self.root_dir = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..', '..'))

    def process_output(self, line):
        print(line.rstrip())