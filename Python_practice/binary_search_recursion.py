def binary_search(sorted_array,search_number, left_index,right_index):
    # base case of recursion
    if left_index > right_index:
        print(f'we did not find search_number = {search_number}')
        return -1
    mid_index = (left_index+right_index)//2
    
    if sorted_array[mid_index] == search_number:
        print(f'item found {sorted_array[mid_index]}')
        return mid_index
    elif sorted_array[mid_index]< search_number:
        # move left index to mid_index+1
        return binary_search(sorted_array,search_number, mid_index+1,right_index)
    else: # search_number < sorted_array[mid_index] move right index to mid_index -1
        return binary_search(sorted_array,search_number, left_index,mid_index -1)


if __name__ == '__main__':
    nums = [-5,-2,-1,0,3,4,100,500,760]
    search_number=500
    left_index = 0 
    right_index = len(nums)-1
    print(f'binary_search({nums},{search_number}, {left_index},{right_index}): {binary_search(nums,search_number, left_index,right_index):}')