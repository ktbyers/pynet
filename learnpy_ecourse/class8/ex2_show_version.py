#!/usr/bin/env python
'''
II. On GitHub, there is the following show version output:

https://github.com/ktbyers/pynet/blob/master/learnpy_ecourse/class8/show_version.txt

    A. Create three functions in three separate modules and put
them in a show_version directory (in practice you wouldn't do
this--you would just have them all in one file, but this will let
you experiment with packages).

        1. Function1 = obtain_os_version -- process the show
version output and return the OS version (Version 15.0(1)M4) else
return None.

        2. Function2 = obtain_uptime -- process the show
version output and return the network device's uptime string
(uptime is 12 weeks, 5 days, 1 hour, 4 minutes) else return None.

        3. Function3 = obtain_model -- process the show version
output and return the model (881) else return None.


    B. Make a package out of this 'show_version' directory using a
blank __init__.py file.

        1. Now that this package has been created, test
importing each of the modules individually from the parent
directory.  In other words, you have a parent directory that
contains the following:

.
./show_version
./show_version/__init__.py
./show_version/os_version.py
./show_version/model.py
./show_version/uptime.py

Python interpreter shell demonstrating this (with blank __init__.py)
>>> import show_version.os_version
>>> import show_version.model
>>> import show_version.uptime
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'show_version']
>>> f = open("show_version.txt")
>>> show_ver = f.read()
>>> show_version.os_version.obtain_os_version(show_ver)
'15.0(1)M4'
>>> show_version.model.obtain_model(show_ver)
'881'
>>> show_version.uptime.obtain_uptime(show_ver)
'12 weeks, 5 days, 1 hour, 4 minutes'


        2. Now edit the __init__.py file such that it
automatically loads each of the modules.  In other words, you
should be able to type:

>>> import show_version

Python interpreter shell demonstrating this (with __init__.py as shown in GitHub)
>>> import show_version
>>> dir(show_version)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 
'model', 'obtain_model', 'obtain_os_version', 'obtain_uptime', 'os_version', 
'uptime']
>>> f = open("show_version.txt")
>>> show_ver = f.read()
>>> show_version.obtain_model(show_ver)
'881'
>>> show_version.obtain_os_version(show_ver)
'15.0(1)M4'
>>> show_version.obtain_uptime(show_ver)
'12 weeks, 5 days, 1 hour, 4 minutes'


    C. Write a script that processes the show_version output using
this package.  It should return something similar to the following:

        model:        881
        os_version:   Version 15.0(1)M4
        uptime:       uptime is 12 weeks, 5 days, 1 hour, 4 minutes

'''

import show_version

if __name__ == "__main__":

    f = open("show_version.txt")

    show_ver = f.read()

    model = show_version.obtain_model(show_ver)
    os_version =  show_version.obtain_os_version(show_ver)
    uptime = show_version.obtain_uptime(show_ver)

    print 
    print "%15s: %-50s" % ("model", model)
    print "%15s: %-50s" % ("os_version", os_version)
    print "%15s: %-50s" % ("uptime", uptime)
    print 

