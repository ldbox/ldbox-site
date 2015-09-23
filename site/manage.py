#!/usr/bin/env python
import os
import sys

path = '/usr/local/lib/python2/site-packages'
if path not in sys.path:
  sys.path.append(path)

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ldbox.site.settings")
  from django.core.management import execute_from_command_line
  execute_from_command_line(sys.argv)
