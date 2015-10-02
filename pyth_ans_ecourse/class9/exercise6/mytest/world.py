'''
Python class on writing reusable code
'''
def func1():
    '''Simple test function'''
    print "Hello world"

class MyClass(object):
    '''Simple test class'''
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        '''Simple test method'''
        print "Hello World: {} {} {}".format(self.var1, self.var2, self.var3)

    def not_hello(self):
        '''Simple test method'''
        print "Goodbye: {} {} {}".format(self.var1, self.var2, self.var3)

class MyChildClass(MyClass):
    '''
    Test class augmenting __init__

    Could use super() also
    '''
    def __init__(self, var1, var2, var3):
        print "Do something more in __init__()"
        MyClass.__init__(self, var1, var2, var3)

    def hello(self):
        '''Simple test method'''
        print "Something else: {} {} {}".format(self.var1, self.var2, self.var3)

if __name__ == "__main__":

    print "\nMain program - world"

    print "\nTesting MyClass:"
    my_obj = MyClass('SF', 'NYC', 'LA')
    print my_obj.var1, my_obj.var2, my_obj.var3
    my_obj.hello()
    my_obj.not_hello()

    print "\nTesting MyChildClass:"
    new_obj = MyChildClass('X', 'Y', 'Z')
    new_obj.hello()
    new_obj.not_hello()
    print
