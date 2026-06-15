

# Here are the most common interview problems categorized by their "pointer movement" style:

# 1. The "Squeeze" (Opposite Ends)
# Pointers start at 0 and n-1 and move toward each other.
# Medium: 3Sum
# The Goal: Find all unique triplets in an array that sum to zero.

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Expected Output: [[-1, -1, 2], [-1, 0, 1]]

# Example 2: No Possible Triplets
# Input: nums = [0, 1, 1]
# Expected Output: []

# Example 3: All Zeros
# Input: nums = [0, 0, 0, 0]
# Expected Output: [[0, 0, 0]]

# Example 4: Multiple Positives and Negatives
# Input: nums = [-2, 0, 0, 2, 2]
# Expected Output: [[-2, 0, 2]]

# Why Two Pointers?
#  You sort the array, fix one number, and then use two pointers on the remaining part to find the other two numbers (similar to the 2Sum II problem).


def fn_3Sum0_brute_force(nums):
    # [-1, 0, 1, 2, -1, -4]
    # -4 -1 -1 0 1 2
    print('BRUTE FORCE APPROACH START ------------')
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum_of_3 = nums[i]+nums[j]+nums[k]
                # print(f'{nums[i]}+{nums[j]}+{nums[k]} = {sum_of_3}')
                if sum_of_3 == 0:
                    print(f'[ {nums[i]}, {nums[j]}, {nums[k]} ]')
    print('BRUTE FORCE APPROACH END ------------')

def fn_3Sum0(nums):
    #  You sort the array, 
    # fix one pointer [i] , and then use two pointers on the remaining part to find the other two numbers.
    # keep i fixed , now check left ,right pointers, Leave last 2 items as they will be middle and right pointer
    # start 
    # i = position 0 ie nums[0]= -4  left = position 1 right position 5
    # -4 -1 -1 0 1 2
    # [i]left->  <-right

    # next iteration i = position 1 ie nums[1]= -1
    nums = sorted(nums)
    for i in range(len(nums)-2):  
        print(f'nums[{i}]={nums[i]}')
        left = i + 1
        right = len(nums) - 1
        while left<right:
            current_sum = nums[i]+nums[left]+nums[right]
            print(f'comparing : {nums[i]} , {nums[left]} ,  {nums[right]} Total sum =  {current_sum}')
            if current_sum == 0 :
                print(f'MATCH FOUND: {nums[i]} , {nums[left]} ,  {nums[right]} ')
                left += 1
                right-= 1
            elif current_sum < 0 : # to reach remaining_sum, move right# think like keeping all people in a photo frame
                left += 1
            else: # current_sum>0
                right -= 1
        print(f'----')   

input_array= [-1, 0, 1, 2, -1, -4]
fn_3Sum0_brute_force(nums=input_array)
fn_3Sum0(nums=input_array)


def fn_2sum(nums, target):
    print(nums) 
    left = 0
    right = len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum>target:
            right -= 1 
        elif current_sum<target:
            left +=1  
        else: # match
            print(f'{nums[left]} + {nums[right]} = {target}')
            left += 1
            right-= 1

input_array2= [4,11,15,2, 7,5]
fn_2sum(sorted(input_array2),9)


def fn_2sum_unsorted(nums, target):
    d = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        
        # 1. Check if the "partner" is already in the dictionary
        if complement in d:
            print(f'Match found! Indices: {d[complement]}, {i}')
        
        # 2. If not found, "remember" the current number and its index
        d[nums[i]] = i

print(f'\n---fn_2sum_unsorted ----\n')
fn_2sum_unsorted(input_array2,9)



# Medium: Container With Most Water
# The Goal: Given an array of heights, find two lines that form a container that holds the most water.
# Why Two Pointers? You start at the ends and always move the pointer pointing to the shorter line to see if you can find a taller one that compensates for the lost width.

# Why your "shorter pointer" logic is correct:
# The Constraint: The amount of water is always limited by the shorter line.
# The Gamble: If you move the taller line, the width decreases, but the height stays limited by the same short line (or an even shorter one). You can never get a larger area that way.
# The Only Way Up: By moving the shorter line, you are gambling that you might find a much taller line that compensates for the loss in width.


# O(N)
def container_with_most_water(nums):
    max_water = 0 
    left = 0 
    right = len(nums) - 1

    while left< right:
        #area formula (right index - left index) * min( height of nums[left], height of nums[right])
        area_water = (right - left)* min(nums[left],nums[right])
        if area_water > max_water:
            max_water = area_water
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water

print(f'\n---container_with_most_water ----\n')
input_array3 = [1,8,3,2,5,4,8,3,7]
print(f'container_with_most_water  = {container_with_most_water(input_array3)}')

# 2. The "Fast & Slow" (Hare and Tortoise)
# Pointers move at different speeds or start at different times.
# Medium: Linked List Cycle II
# The Goal: Detect if a cycle exists in a linked list and return the node where the cycle begins.
# Why Two Pointers? A fast pointer (2 steps) will eventually lap a slow pointer (1 step) if there is a loop.
# Advanced: Find the Duplicate Number
# The Goal: Given an array of n + 1 integers where each integer is between 1 and n, find the one duplicate number without modifying the array or using extra space.
# Why Two Pointers? You treat the array as a linked list (where nums[i] is the "next" pointer) and use the cycle detection logic above. This is a very common "trick" question.


# 3. The "Sliding Window"
# Pointers maintain a "window" of elements that grows or shrinks.
# Medium: Longest Substring Without Repeating Characters
# The Goal: Find the length of the longest substring without any duplicate characters.
# Why Two Pointers? The right pointer expands the window. If you hit a duplicate, the left pointer "shrinks" the window until the duplicate is gone.
# Advanced: Minimum Window Substring
# The Goal: Given two strings S and T, find the minimum window in S which contains all the characters in T.
# Why Two Pointers? This is the "boss level" of sliding windows. You expand until you have a "valid" window, then shrink from the left to find the absolute smallest version of it.


# 4. The "Partition" (Same Direction)
# One pointer marks the boundary of "processed" items, the other explores.
# Medium: Dutch National Flag Problem (Sort Colors)
# The Goal: Sort an array of 0s, 1s, and 2s in-place.
# Why Two Pointers? You actually use three pointers here: one for the 0s boundary, one for the 2s boundary, and one to iterate. It’s a variation of the logic used in QuickSort's partition.
