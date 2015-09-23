#!/usr/bin/env python

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

def new_secret_key():
  return get_random_string(50, chars)

if __name__ == "__main__":
  print(new_secret_key())
