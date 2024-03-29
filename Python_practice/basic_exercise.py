# 87.
# Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits.
# Return True if the employee code is valid and False if it's not.


def valid_employee_code(emp_num):
    return len(emp_num) in [8, 12] and emp_num.isdigit()


# 88. Write a Python program that accept two strings and test if the letters in the second
# string are present in the first string.


def presence_in_first_str(list_data):
    list_of_validity = [c in list_data[0].lower() for c in list_data[1].lower()]
    return all(list_of_validity)

# list OUT top 3 +ve numbers from list in descending order


def top_3_positive_numbers(input_list: list):
    tmp_list = [x for x in input_list if x > 0]
    sorted_list = sorted(tmp_list, reverse=True)
    return sorted_list[:3]


# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
# nums = [10,20,30,40,50,60,70,80,90]

def remove_numbers(input_list: list):
    position = 2
    length_of_list = len(input_list)
    while length_of_list > 0:
        # print(f"position - {position} list - {input_list}")
        print(input_list.pop(position))
        length_of_list -= 1
        if length_of_list >= 1:
            position = (position + 2) % length_of_list


# 80. Write a Python program to count number of substrings with same first and last characters of a given string.
# Click me to see the sample solution

# 81. Write a Python program to find the index of a given string at which a given substring starts.
# If the substring is not found in the given string return 'Not found'. Go to the editor
# Click me to see the sample solution

# 82. Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.
# Click me to see the sample solution


# 49. Write a Python program to count and display the vowels of a given text.

# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.

# 69. Write a Python program to find the longest common sub-string from two given strings.

# 25. Write a Python program to create a Caesar encryption. Go to the editor
#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example,
# with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.



# 2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import itertools
import random


def all_possible_strings(char_list: list):
    list_of_permutations = itertools.permutations(char_list, 5)
    list_of_permutations = ["".join(x) for x in list_of_permutations]
    print(list_of_permutations)
    print(f"len of list_of_permutations - {len(list_of_permutations)}")


if __name__ == "__main__":
    print("valid_employee_code function: ")
    print(valid_employee_code('12345678'))
    print(valid_employee_code('12345678a'))

    print("\npresence_in_first_str:")
    print(presence_in_first_str(['female', 'male']))
    print(presence_in_first_str(['aloo', 'male']))

    print("\ntop_3_positive_numbers:")
    l1 = [-1, -2, 10, 2, 13, 104, 87, -39, 100]
    print(f"list -1 :{l1}")
    print(top_3_positive_numbers(l1))

    print("\nremove_numbers:")
    remove_numbers([10,20,30,40,50,60,70,80,90])

    print("\n all_possible_strings:")
    all_possible_strings(['a', 'e', 'i', 'o', 'u'])
