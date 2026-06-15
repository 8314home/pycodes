def detect_dup(k, k_list):
    k_set = set()

    #check length

    for i in k_list: #timem O(n) space O(n)
        if i in k_set:
            return i
        else:
            k_set.add(i)
    return -1

# 3. Are there ways to optimize this?
# 4. What if we are heavily limited on memory?
# Say for example the array is 1.5GB long in memory and we only have 2GB memory. 
# This doesn't have to be as time performant as the prior answers.

# Counter 

def detect_dup_2(k, k_list):
    k_list.sort() # Time O(nlogn)

    print(f'k_list={k_list}')
    len_k_list = len(k_list) #k+1

    #prev = k_list[0] # first item of list
    for i in range(1,len_k_list):
        if k_list[i-1] == k_list[i]:
            return k_list[i]
    return -1


if __name__ == '__main__':
    k = 5
    nums = [3, 1, 4, 2, 5, 3] #k+1

    print(detect_dup(k, nums))

    print(f'----')

    print(detect_dup_2(k, nums))

