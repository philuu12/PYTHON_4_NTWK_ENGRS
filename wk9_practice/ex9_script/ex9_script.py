#!/usr/bin/env python
"""
Write a Python script in a different directory (not the one containing mytest).
    a. Verify that you can import mytest and call the three functions func1(),
func2(), and func3().

    b. Create an object that uses MyClass. Verify that you call the hello() and
not_hello() methods.
"""

import mytest
from mytest import *
from mytest import func3

print '*' * 80
print "Print out 3 functions"
print '*' * 80
mytest.simple.func1()   # Work with 'import mytest'
func2()                 # Work with 'from mytest import *'
func3()                 # Work with 'from mytest import func3'

aMyClassObj = MyClass("It", "will", "be a beautiful day tommorrow!")

print
print '*' * 80
print "Print out Hello and NonHello for a MyClass object"
print '*' * 80
aMyClassObj.Hello()
aMyClassObj.NonHello()



