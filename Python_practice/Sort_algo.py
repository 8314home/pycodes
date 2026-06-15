def merge_sort(nums):
    if len(nums) == 1:
        return

    # divide
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    # conquer
    i = 0
    j = 0
    k = 0
    while (i < len(left_half)) and (j < len(right_half)):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k+=1

    # copy
    while (i < len(left_half)):
        nums[k] = left_half[i]
        i += 1
        k += 1
    while (i < len(left_half)):
        nums[k] = right_half[j]
        j += 1
        k += 1

# partition(index_first, index_last):
#     pivot = len(index_last)//2
#     swap(index_last, pivot)

#     for i = index_first to index_last:
#     if nums[i] < nums[index_last]:
#         swap(i, index_first)
#         index_first += 1
#     swap(index_first, index_last)

def quicksort_partition(data,index_first, index_last):
    pivot_index  = (index_first + index_last) // 2
    data[index_last],data[pivot_index] = data[pivot_index],data[index_last]

    for i in range(index_first, index_last):
        if data[i] <= data[index_last]:
            data[i],data[index_first] = data[index_first],data[i]
            index_first += 1
    data[index_first],data[index_last] = data[index_last],data[index_first]
    return index_first


def quicksort(data,low, high):
    if low >high:
        return 
    pivot = quicksort_partition(low, high)
    quicksort(data,low,pivot-1)
    quicksort(data,pivot+1, high)


if __name__ == '__main__':
    nums = [1,5,9,15,3,2,8,11,10]
    merge_sort(nums)
    print(nums)

    # nums_2 = [1,5,9,15,3,2,8,11,10]
    # quicksort(nums_2,0,len(nums_2)-1)
    # print(nums_2)