
my_list = [1, 2, 9, 'whatever', True, []]

# anti-pattern don't do this
for i in range(len(my_list)):
    print i, my_list[i]
print

# use enumerate instead
for i, value in enumerate(my_list):
    print i, value
print

