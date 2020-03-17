# Selection sort -simple - O(n2)
# - selection of minimum value at every iteration and put it in front of array,
# take index pos - compare it with all elements from right side right side of array
# check from next position --good for flash memory as less mem requirement


def selection_sort(nums):
    print("Array length : {}".format(len(nums)))
    for i in range(len(nums)-1): # loop till last but one item
        index = i
        for j in range(i+1, len(nums)): # i+1 start from next item
            if nums[index] > nums[j]:
                index = j # storing just the index value which has that minimum value
        if index != i:
            temp = nums[i]
            nums[i] = nums[index]
            nums[index] = temp
    return nums


if __name__ == "__main__":
    print("Selection sort:")
    arr = [8,2,-1,56,-5,12,7,4]
    print(selection_sort(arr))
