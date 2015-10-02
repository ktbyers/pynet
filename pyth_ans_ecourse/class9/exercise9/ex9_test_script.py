#!/usr/bin/env python
'''
Write a Python script in a different directory (not the one containing mytest).
a. Verify that you can import mytest and call the three functions func1(),
   func2(), and func3().
b. Create an object that uses MyClass. Verify that you call the hello() and
   not_hello() methods.
'''

from mytest import func1, func2, func3, MyClass

def main():
    '''Main func'''
    print
    print "Testing func1...",
    func1()
    print "Testing func2...",
    func2()
    print "Testing func3...",
    func3()

    print "\nTesting MyClass..."
    my_obj = MyClass('a', 'b', 'c')
    my_obj.hello()
    my_obj.not_hello()
    print

if __name__ == "__main__":
    main()
