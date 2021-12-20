# Collections module implements specialized container datatypes providing alternatives to Python's general purpose
# built-in containers, dict, list, set, and tuple.

# Ex-1
# Write a Python program that iterate over elements repeating each as many times as its count.

from collections import Counter
c = Counter(p=2, q=4, s=1, t=-1)
print(list(c.elements()))
# elements(self) method returns :  '''Iterator over elements repeating each as many times as its count.

d = ['a', 'b', 'b', 1]
d2 = Counter(d)
print(d2)


# deque
# Returns a new deque object initialized left-to-right (using append()) with data from iterable.
# If iterable is not specified, the new deque is empty.
# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for
# “double-ended queue”).
# Deques support t appends and pops from either side of the deque with approximately the same O(1) performance
# in either direction.
# They are also useful for tracking transactions and other pools of data where only the most recent activity is of
# interest.
# pop() - pops from right side & append add element to right side

from collections import deque

# 4 Write a Python program to find the occurrences of 10 most common words in a given text.



given_text = "If maxlen is not specified or is None, deques may grow to an arbitrary length."
l = given_text.split(" ")
cl = Counter(l)
print(cl.most_common(3))

## IMPROVED

import re
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
words = re.findall('\w+', text)
print(Counter(words).most_common(10))

# Write a Python program that accept name of given subject and marks.
# Input number of subjects in first line and subject name, marks separated by a space in next line.
# Print subject name and marks in order of its first occurrence.
#
# Number of subjects:  3
# Input Subject name and marks:  Bengali 58
# Input Subject name and marks:  English 62
# Input Subject name and marks:  Math 68
# Bengali 58
# English 62
# Math 68



# 9. Write a Python program to add more number of elements to a deque object from an iterable object.



# 11. Write a Python program to copy of a deque object and verify the shallow copying process.



# Data Structures
# Ex-1
# Write a Python program to create an Enum object and display a member name and value.

# Enum is a class in python for creating enumerations.
# enumerations are a set of symbolic names (members) bound to unique, constant values.

from enum import Enum, IntEnum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


for i in Country:
    print(i)

print(Country.Antarctica.name)
print(Country.Antarctica.value)

# get all names from Enum object sorted by their numeric values
class Country2(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


for c in sorted(Country2):
    print(c.name)

# get all values from Enum object in a list

print(list(map(lambda x: x.value, Country2)))


# Ex-10 Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
# class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
# output
# [('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]

from collections import defaultdict

# Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
# The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never
# raises a KeyError. It provides a default value for the key that does not exists.

# Using List as default_factory

# When the list class is passed as the default_factory argument, then a defaultdict is created with
# the values that are list.

print("default dict exercise")

class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]

dd_ex_10 = defaultdict(list)

for k, v in class_roll:
    dd_ex_10[k].append(v)

print(dict(dd_ex_10))






