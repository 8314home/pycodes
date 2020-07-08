def merge_sort_fn(nums):
    # divide part -- divide element till 1 element
    if len(nums) == 1:
        return

    middle_index = len(nums)//2
    left_half = nums[:middle_index]  # takes till nums[middle_index -1]
    right_half = nums[middle_index:]  # LIST[INCLUSIVE: EXCLUSIVE]

    merge_sort_fn(left_half)
    merge_sort_fn(right_half)

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


if __name__ == "__main__":

    # binary_search([1,2,3,5,8,9,10,11,12,16], 5)
    # binary_search([1,2,3,5,8,9,10,11,12,16], 6)

    list_of_array = [8,2,-1,56,-5,12,7,4]
    merge_sort_fn(list_of_array)
    print(f"merge sort o/p - {list_of_array}")
