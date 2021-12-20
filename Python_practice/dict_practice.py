# Important

# Python | Merge Python key values to list
# while working with Python, we might have a problem in which we need to get the values of dictionary
# from several dictionaries to be encapsulated into one dictionary

# Input
# test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
#              {'it' : 5, 'is' : 7, 'best' : 8},
#              {'CS' : 10}]

# Output
# {‘is’: [4, 7], ‘it’: [5], ‘gfg’: [2], ‘CS’: [10], ‘best’: [6, 8]}

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
             {'it' : 5, 'is' : 7, 'best' : 8},
             {'CS' : 10}]

result_dict = dict()

for sub in test_list:
    for key, value in sub.items():
        result_dict.setdefault(key, []).append(value)
        print(result_dict)

print(f"result_dict - {result_dict}")


# OPTION-2 use a default_dict from collections

from collections import defaultdict
result_dict_2 = defaultdict(list)

for sub in test_list:
    for key, value in sub.items():
        result_dict_2[key].append(value)

print(f"result_dict_2 - {dict(result_dict_2)}")



# setdefault(key,default_value) - Insert key with a value of default_value if key is not in the dictionary.
# Return the value for key if key is in the dictionary,
# else default.
# here if present it is resturing a list like this
# 'is': [4]
# so that 7 can be appended
# 'is': [4, 7]


print(f"original list of dicts: {test_list}")
print(f"output dict: {result_dict}")

# 1. Write a Python program to sort (ascending and descending) a dictionary by value.
print("program -1")
d = {1: 2, 10: 4, 4: 4, 3: 3}
print(d)
ds = dict(sorted(d.items(), key=lambda x: x[0]))
print(ds)
ds_2 = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
print(ds_2)


# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# 4. Write a Python script to check whether a given key already exists in a dictionary.
print("\n\n program -3,4")

dic1={1: 10, 2: 20}
dic2={3: 30, 4: 40}
dic3={5: 50, 6: 60}

dic_p34 = dict()

for d in [dic1, dic2, dic3]:
    dic_p34.update(d)
print(dic_p34)

check_key = 2
if check_key in dic_p34.keys():
    print(f"{check_key} exists in {dic_p34}")


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print("\n\n program -7")
dic_p7 = dict()
for i in range(1, 16):
    dic_p7[i] = i**2
print(dic_p7)


# 19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
print("\n\n program -19")

""" USING collections module """
from collections import Counter

""" Counter module - Dict subclass for counting hashable items.  Sometimes called a bag
    or multiset.  Elements are stored as dictionary keys and their counts
    are stored as dictionary values. supports ops like subtract, __add__, elements (for iteration) etc"""

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(Counter(d1))
print(Counter(d2))

dic19_counter = Counter(d1) + Counter(d2)
print(dic19_counter)

""" using loops """

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'd': 400, 'b': 200}

for i in zip(d1.items(), d2.items()):
    print(i)

dic19 = dict()
d1k = d1.keys()
d2k = d2.keys()
for k1 in d1k:
    if k1 in d2k:
        dic19[k1] = d1[k1] + d2[k1]
    else:
        dic19[k1] = d1[k1]

dic19_keys = dic19.keys()

for k2 in d2k:
    if k2 not in dic19_keys:
        dic19[k2] = d2[k2]

print(dic19)

# 20 Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data :
# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
print("\n\n program -20")


Sample_Data_20 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# set_20 = set()
# for i in Sample_Data_20:
#     for v in i.values():
#         set_20.add(v)

set_20 = set(v for i in Sample_Data_20 for v in i.values())
print(set_20)


# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different
# key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
import itertools

sample_data_21 = {'1':['a','b'], '2':['c','d']}

print(sample_data_21.values())
print(*sample_data_21.values())  # --> use * to get values out of dict_values() view
dl = [sample_data_21[k] for k in sorted(sample_data_21.keys())]
print(*dl)

# itertool.product works like --> cartesian product of two or more iterators

for k in itertools.product(*sample_data_21.values()):
    print(''.join(k))


# 22. Write a Python program to find the highest 3 values in a dictionary. Go to the editor
# Click me to see the sample solution

sample_dict_22 = {'a': 10, 'b': 8, 'c': 101, 'd': 30, 'e': 70}

print(f"Top 3 va;ues from dict: - prog - 22")
print(sorted(list(sample_dict_22.values()), reverse=True)[:3])

print("->".join(list(map(lambda x: str(x), sorted(list(sample_dict_22.values()), reverse=True)[:3]))))


# 23. Write a Python program to combine values in python list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

Sample_data_23 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

c = Counter()
for d in Sample_data_23:
    c += Counter({d['item']: d['amount']})
print(c)


#  DICT SUPPORT += operation
# IMPORTANT -> a technique to use values from one dict to be used a keys in another dict

result = Counter()
for d in Sample_data_23:
    result[d['item']] += d['amount']
print(result)


# 24. Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

print("\nprogram -24")
c = Counter('w3resource')
print(dict(c))


# 25. Write a Python program to print a dictionary in table format. Go to the editor
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# expected o/p
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

# ------------------------------------------------
# Use of *

# zip wants a bunch of arguments to zip together, but what you have is a single argument
# (a list, whose elements are also lists). The * in a function call "unpacks" a list
# (or other iterable), making each of its elements a separate argument.
# So without the *, you're doing zip( [ [1,2,3],[4,5,6] ] ). With the *, you're doing zip([1,2,3], [4,5,6])

# ------------------------------------------------

print("\nprogram -25")
my_dict_25 = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# defining a list with key, [key] & adding value
for key, value in sorted(my_dict_25.items()):
    print([key] + value)

# The * in a function call "unpacks" a list(or other iterable), making each of its elements a separate argument.

l2 = list([key] + value for key, value in my_dict_25.items())
print(l2)

for row in zip(*([key] + value for key, value in my_dict_25.items())):
    print(*row)



# 26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True




# 27. Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# {1: {2: {3: {4: {}}}}}
