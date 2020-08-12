

# 1. Write a Python program for BINARY SEARCH .
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target
# value within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search
# algorithm and executes in logarithmic time. O(log n)
# Test Data :
# binary_search([1,2,3,5,8], 6) -> False
# binary_search([1,2,3,5,8], 5) -> True

def binary_search(input_list, input_value) -> bool:
    midpoint = int(len(input_list)/2)
    # print(f"midpoint - {midpoint}")
    # print(f" input list - {input_list}")
    if not input_list: # means if input_list is empty
        print("NOT FOUND item. ")
        return False
    if input_list[midpoint] == input_value:
        # print(f"input_list[midpoint] = {input_list[midpoint]} and input_value = {input_value}")
        print("value present in list")
        return True
    if input_value < input_list[midpoint]:
        # print(f"set-1 input_list = {input_list} and input_value = {input_value}")
        # print(f" rec call with {input_list[:midpoint]} {input_value}")
        return binary_search(input_list[:midpoint], input_value)   # list[INCLUSIVE : EXCLUSIVE] - list(0 to midpoint-1)
    if input_value > input_list[midpoint]:
        # print(f"set -2 input_list = {input_list} and input_value = {input_value}")
        # print(f" rec call with {input_list[midpoint+1:]} {input_value}")
        return binary_search(input_list[midpoint+1:], input_value)


#  IMPORTANT -> list[start_pos:end_pos] === list[INCLUSIVE : EXCLUSIVE]
# 2.  Merge sort - O(n log n) comparison-based sorting algorithm - DIVIDE & CONQUER algo -  stable sort

# 1. divide part - divide till one element is pending, then return
# 2. conquer part 1- both sub list has items
# 3. conquer part 2- add remaining items from both list


def merge_sort(nums):
    # divide part -- divide element till 1 element
    if len(nums) == 1:
        return

    middle_index = len(nums)//2
    left_half = nums[:middle_index]  # takes till nums[middle_index -1]
    right_half = nums[middle_index:]  # LIST[INCLUSIVE: EXCLUSIVE]

    merge_sort(left_half)
    merge_sort(right_half)

    # conquer part -PART-1 both sub array has data
    i = 0
    j = 0
    k = 0
    # here we are overwriting the original array iteslf
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    # once we have exhausted at least one array-left or right half
    # copy the remaining items PART-2

    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


def selection_sort(nums):

    # SELECT minimum element in each iteration and PUT at increasing index pos
    # take from first to (last_elem -1 pos) in outer loop as we can PUT till last but 1 pos
    # each iteration set min_index to the element and check against all elements right of it
    # if any element is less than index then set min_index to that index
    # at the end of inner iteration swap elements
    # O(n2) but good with low memory req, flash memory

    for i in range(len(nums)-1):
        # print(f"intermediate - {i} - nums - {nums}")
        min_item_index = i
        for j in range(i+1, len(nums)):
            if nums[min_item_index] > nums[j]:
                min_item_index = j
        if min_item_index != i:
            tmp = nums[min_item_index]
            nums[min_item_index] = nums[i]
            nums[i] = tmp
    return nums


if __name__ == "__main__":

    # binary_search([1,2,3,5,8,9,10,11,12,16], 5)
    # binary_search([1,2,3,5,8,9,10,11,12,16], 6)

    numbers = [8,2,-1,56,-5,12,7,4]
    merge_sort(numbers)
    print(f"merge sort o/p - {numbers}")

    numbers_2 = [8,2,-1,56,-5,12,7,4]
    print(f"\nselection sort algo")
    selection_sort(numbers_2)
    print(f"selection sort - {numbers_2}")
