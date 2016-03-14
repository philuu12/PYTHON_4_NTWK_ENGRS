#!/usr/bin/env python
"""
4. Create a class MyClass in world.py. 
    a. This class should require that three variables be passed in upon initialization. 

    b. Write two methods associated with this class 'hello' and 'not_hello'. Have both these methods print a statement that uses all three of the initialization variables.
"""

class MyClass(object):

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def Hello(self):
        print ("Hello - var1: %s, var2: %s, var3: %s\n" %
                (self.var1, self.var2, self.var3))

    def NonHello(self):
        print ("NonHello - var1: %s not, var2: %s not, var3: %s not\n" %
                (self.var1, self.var2, self.var3))

def main():
    classObj = MyClass("Nice", "Little", "World")

    classObj.Hello()
    classObj.NonHello()


if __name__ == "__main__":
    main()
