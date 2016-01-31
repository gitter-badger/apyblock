#!/usr/bin/env python3
#
# A Shell Blocker, Python3 Port!
# Block annoying ADs with a single script.
#
# Copyright (C) 2016 Federico Damián Schonborn <federicodamians@gmail.com>
#
# This file is part of A Shell Blocker.
#
# A Shell Blocker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# A Shell Blocker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with A Shell Blocker. If not, see <http://www.gnu.org/licenses/>.

import os
import sys

class color:
   bold = '\033[1m'
   undl = '\033[4m'
   endc = '\033[0m'

print("\n" + color.bold + "Port is not already done, thus... This is a skeleton!" + color.endc + "\n")
if sys.platform.startswith('linux'):
  print("You're using " + color.bold + "Linux" + color.endc + " (or GNU/Linux, name it as you want)!" + "\n")
elif sys.platform.startswith('freebsd'):
  print("You're using " + color.bold + "FreeBSD" + color.endc + " (or a derivated proyect)!" + "\n")
elif sys.platform.startswith('darwin'):
  print("You're using " + color.bold + "OS X" + color.endc + " (you lucky)!" + "\n")
elif sys.platform.startswith('cygwin'):
  print("You're using " + color.bold + "Cygwin" + color.endc + " on Windows ('cause it makes it better)!" + "\n")
elif sys.platform.startswith('win32'):
  print("You're using " + color.bold + "Windows" + color.endc + " (it's not funny)!" + "\n")
