#!/usr/bin/env python
# Two ways of installing the my_func.py module
# 1) PYTHONPATH = ../subdir
# 2) Put the my_func.py module in "/home/pluu/applied_python/lib/python2.7/site-packages"
# because this is one of the paths that Python searches for.
# To see all the paths that Python searches, do the followings on the interpreter:
# >>> import sys
# >>> from pprint import pprint
# >>> pprint (sys.path)

from my_func import print_hello

print_hello()


