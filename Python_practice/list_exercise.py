#  List exercise :
#  https://www.w3resource.com/python-exercises/list/#EDITOR

# 5.
#  Write a Python program to count the number of strings where the string length is 2 or more
#  and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list = ['abc', 'xyz', 'aba', '1221']

sample_list_2 = list(
    filter(lambda x: len(x) > 2 and x[0] == x[-1], sample_list))

print(sample_list_2)

# 6.
# Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_2_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# sorted return new list
sample_3_list = sorted(sample_2_list, key=lambda t: t[1], reverse=True)
print(f"\nprogram-6 - {sample_3_list}")

# 7. Write a Python program to remove duplicates from a list.

sample_list_with_dups = ['abc', 'xyz', 'aba', '1221', 'xyz']

sample_list_with_dups_to_set = set(sample_list_with_dups)
print(sample_list_with_dups_to_set)

sample_list_without_dups = list(sample_list_with_dups_to_set)
print(f"\nprogram -7 - {sample_list_without_dups}")

# 12.
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sample_12_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list_after_exclusion = [
    x for (i, x) in enumerate(sample_12_list) if i not in (0, 4, 5)
]
print(f"\nprogram -12 - {list_after_exclusion}")

#  13.
# Write a Python program to generate a 3*4*6 3D array whose each element is *.

array_3d = [[[(i, j, k) for k in range(6)] for j in range(4)]
            for i in range(3)]
print(f"\nprogram -13 - {array_3d}")

#  17. Write a Python program to generate and print a list except for the first 5 elements
#  , where the values are square of numbers between 1 and 30 (both included).

square_list = [i ** 2 for i in range(1, 31)]
print(f"\nprogram -17 - {square_list}")
print(f"\nprogram -17 - {square_list[5:-5]}")

#  23. Write a Python program to flatten a shallow list.

# 27. Write a Python program to find the second smallest number in a list.28. Write a Python
# program to find the second largest number in a list.

sample_list_27_28 = [1, 4, 5, 2, 56, 93, -2, 10, 91]

sample_list_27_28.sort()
print(f"\nprogram -27_28 - {sample_list_27_28}")
print(f"2nd smallest no - {sample_list_27_28[1]}")
print(f"2nd largest no - {sample_list_27_28[-2]}")

# 30. Write a Python program to get the frequency of the elements in a list.

print(f"\nprogram -30-")
l_30 = [1,2,'True', 1,2,'False', True, 'False', False]

d_30 = {}
for i in l_30:
    print(i)
    if i in d_30:
        d_30[i] += 1
    else:
        d_30[i] = 1
print(f"\n program -30 - {d_30}")

from collections import Counter
print(Counter(l_30))

d_31 ={}
d_31[True] = 1
print(d_31)

# 32. Write a Python program to check whether a list contains a sublist.


def contain_sublist(list_32, list_32_sub_list ):
    flag = False

    if list_32_sub_list == [] or len(list_32_sub_list) > len(list_32):
        flag = False
    elif list_32_sub_list == list_32:
        flag = True
    else:
        for i in range(len(list_32)):
            if list_32[i] == list_32_sub_list[0]:
                k = 1
                while k < len(list_32_sub_list):
                    # print(f"k = {k} i+k = {i + k}")
                    if list_32_sub_list[k] == list_32[i + k]:
                        k += 1
                    else:
                        break
                if k == len(list_32_sub_list):
                    flag = True
    return flag


list_A_32 = ['b','a','c','e','f','i','j']
list_B_32_sub_list = ['e','f','i']

if contain_sublist(list_A_32, list_B_32_sub_list):
    print("program -32 - sublist is there")
else:
    print("program -32 - no sublist present")
