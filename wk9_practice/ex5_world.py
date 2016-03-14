#!/usr/bin/env python
"""
5. Write a child class MyChildClass of MyClass. This child class should override the 'hello' method and print a different statement.
"""


class MyClass(object):

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def Hello(self):
        print ("Hello MyClass: var1: %s, var2: %s, var3: %s\n" %
              (self.var1, self.var2, self.var3))

    def NonHello(self):
        print ("NonHello - var1: %s not, var2: %s not, var3: %s not\n" %
              (self.var1, self.var2, self.var3))

class ChildMyClass(MyClass):
    def Hello(self):
        print ("Hello - ChildMyClass: var1: %s, var2: %s, var3: %s\n" %
              (self.var1, self.var2, self.var3))

def main():
    childMyClassObj = ChildMyClass("I", "am", "the Child")

    childMyClassObj.Hello()


if __name__ == "__main__":
    main()
