#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

2. Write a function that converts a list to a dictionary where the
index of the list is used as the key to the new dictionary (the
function should return the new dictionary).

'''

def list_to_dict(a_list):

    new_dict = {}

    for i,v in enumerate(a_list):
        new_dict[i] = v

    return new_dict



# Create a simple test list
test_list = range(100,110)
test_list.append('whatever')

# Call the function
test_dict = list_to_dict(test_list)

# Display the results
print  
print "List: %s" % str(test_list)
print "Dict: %s" % str(test_dict)
print
