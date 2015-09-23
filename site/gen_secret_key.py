#!/usr/bin/env python

# Copyright 2015 Oleg Girko <ol@infoserver.lv>
#
# This file is part of ldbox.site Python package.
#
# ldbox.site Python package is free software: 
# you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

def new_secret_key():
  return get_random_string(50, chars)

if __name__ == "__main__":
  print(new_secret_key())
