import DS_Algo.linked_list as linked_list
import DS_Algo.Stack as Stack_py_file

# Interview Question #1 REVERSING ARRAY
# The problem is that we want to reverse a T[] array in O(N) linear time complexity
# and we want the algorithm to be in-place as well!
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]


# Done using start_index & end_index and swapping the elements untill we reach middle.

def reverse_array(nums):
    start_index = 0
    end_index = len(nums) -1

    while start_index <= end_index:
        nums[end_index], nums[start_index] = nums[start_index], nums[end_index]
        start_index += 1
        end_index -= 1
    return nums

# Interview Question #2
# plaindrome = madam/radar


def is_palindrome(input):
    original = input
    reversed_string = input[::-1]

    if original == reversed_string:
        return True
    return False


def is_palindrome_better(input):
    return input == ''.join(input[::-1])

# Interview question - 3 : Reversing an integer


def reverse_integer(n):
    remainder = 0
    reversed_number = 0

    while n > 0:
        remainder = n % 10
        n = n // 10
        reversed_number = reversed_number * 10 + remainder
    return reversed_number

# Interview Question - 4
# The problem is that we want to find duplicates in a one-dimensional array
# of integers in O(N) running time where the integer values are smaller than the length of the array!

# we can think of counting sort operation


def duplicates_in_array(nums):

    # implementation can done in place as well, in below form we take item from arr[i] -> item
    # and mark arr[item] to -ve , so that if we get same item 2nd time ,when we go ahead and try to mark negative
    # if we see it is already negative, it means that is duplicate
    # instead of arr[item] we take arr[ absolute value of item]

    for n in nums:
        abs_val = abs(n)
        if nums[abs_val] < 0:
            print("{}".format(abs_val))
        nums[abs_val] *= -1

# Anagram problem: Interview Question - 5
# Construct an algorithm to check whether two words (or phrases) are anagrams or not!
# subject & anagram - a word or phase is called anagram if that word consists of same alphabets with same no of
# occurrence for each alphabet

def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)  # sorted of a string (a sequence) returns a sorted list
    str2 = sorted(str2)

    print(str1)
    print(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False  # after sorting if any char is not matching
    return True

# Dynamic programming
# largest sum sub-array

# middle node from linked list
#Need two pointers, one slow_pointer which will traverse 1 at a time, fast_pointe which will travel 2 ata time

# O(n) complexity
def middle_node_ll(ll_par):
    slow_pointer = ll_par.head
    fast_pointer = ll_par.head

    while fast_pointer.nextNode and fast_pointer.nextNode.nextNode: # and usd to brk the loop when fastpointer reach end
        slow_pointer = slow_pointer.nextNode
        fast_pointer = fast_pointer.nextNode.nextNode
    return slow_pointer


# Reversing a linked list in O(n) time complexity with no extra memory
def reverse_linked_list(ll_par):

    prev_node = None
    current_node = ll_par.head

    while current_node:
        tmp_node = current_node.nextNode
        current_node.nextNode = prev_node
        prev_node = current_node
        current_node = tmp_node
    ll_par.head = prev_node
    return ll_par


if __name__ == "__main__":
    print("reversing array\n")
    a = [1,2,3,4,5]
    print(reverse_array(a))

    print("Palindrome check")

    b = 'madam'

    if is_palindrome_better(b):
        print("string is palindrome")
    else:
        print("string is NOT palindrome")

    c = 2349
    print("Reversed number of {} is {}".format(c, reverse_integer(c)))

    d = [1,4,5,6,5,3,2,3,4,7]
    print("duplicates in array {}".format(d))
    duplicates_in_array(d)

    e1 = "fluster"
    e2 = "restful"
    if anagram(e1,e2):
        print("e1,e2 are anagram".format(e1,e2))
    else:
        print("e1,e2 are NOT anagram".format(e1,e2))

    ll = linked_list.LinkedList()
    ll.insert_at_head(14)
    ll.insert_at_head(10)
    ll.insert_at_head(1)
    ll.insert_at_head(15)
    ll.insert_at_head(7)
    ll.insert_at_head(9)
    ll.insert_at_head(11)
    ll.print_all()
    ll_mid = middle_node_ll(ll)
    print("middle node data {}".format(ll_mid.data))
    print("original linked list")
    ll.print_all()
    ll_r = reverse_linked_list(ll)
    print("reversed linked list")
    ll_r.print_all()

    st = Stack_py_file.MyStack()
    max_st = Stack_py_file.MyStack()
    st.push(10)


