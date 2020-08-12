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





