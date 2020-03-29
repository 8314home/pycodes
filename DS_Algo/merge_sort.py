def merge_sort(nums):
    # divide part
    if len(nums) == 1:
        return

    middle_index = len(nums)//2
    left_half = nums[:middle_index]  # takes till nums[middle_index -1]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # conquer part
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
    # copy the remaining items

    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [8,2,-1,56,-5,12,7,4]
    merge_sort(arr)
    print(arr)










