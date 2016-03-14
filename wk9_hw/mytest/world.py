#!/usr/bin/env python

def func3():
    print "world - func3: This is a world function"

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

    def __init__(self, var1, var2, var3, var4):
        super(ChildMyClass, self).__init__(var1, var2, var3)
        self.var4 = var4

    def Hello(self):
        print ("Hello - ChildMyClass: var1: %s, var2: %s, var3: %s, var4: %s\n" %
              (self.var1, self.var2, self.var3, self.var4))

def main():
    # childMyClassObj = ChildMyClass("I", "am", "the beautiful", "child")
    # childMyClassObj.Hello()

    print "From 'world' module - in the main executable code"

if __name__ == "__main__":
    main()
