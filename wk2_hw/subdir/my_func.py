#!/usr/bin/env python


"""
1. Python Libraries 

    a. Make sure that you have PySNMP and Paramiko installed in the lab (i.e. enter the Python shell and test 'import pysnmp', and 'import paramiko').

    b. Determine which version of PySNMP and Paramiko are installed.  dir(pysnmp) and dir(paramiko) should be helpful here.

    c. Write a simple Python module that contains one function that prints 'hello' (module name = my_func.py). Do a test where you import my_func into a new Python script. Test this using the following contexts:
        * my_func.py is located in the same directory as your script
        * my_func.py is located in some random subdirectory (not the same directory as your script)
        * my_func.py is located in ~/applied_python/lib/python2.7/site-packages/
"""
# 1.a and 1.b
# >>> import pysnmp
# >>> import paramiko
# 1.a and 1.b
# >>> paramiko.__version__
# '1.16.0'
# >>> pysnmp.version
# (4, 3, 1)
# >>> 
# 1.c

def print_hello():
    print "Hello World!"

if __name__ == "__main__":
    print_hello()
