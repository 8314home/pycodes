# Knapsack problem is to maximize revenue V with constraint weight M. for this we need to take any no of item from N items.
# N items are individual with their individual weight and value => <v_i, w_i > 
# default complexity O(2^N) ie exponential => we need to use dynamic prog
# usual implementation - Recursion

# No of item
N = 4

# 0 in WEIGHTS and 0 in VALUES is a base case , we add it for easier undesrating of backtracking DP
WEIGHTS = [0,1,3,4,5]
VALUES = [0,1,4,5,7]

# knapsack capacity 6 kg
CONSTRAINT_WEIGHT = 7

# target_weight = total weight of individual items taken 
# n = no of items to be considerted
def knapsack_problem(target_weight,n): # recursion TREE
    # Base condition => if no more items to consider or no capacity remaining in bag
    if target_weight==0 or n==0:
        return 0
    # what if n th item individual weight is more than total capacity=> reject item , call function with (target_weight, n-1 )
    if WEIGHTS[n-1] > target_weight:
        return knapsack_problem(target_weight,n-1)
    else:
        n_inlcuded = VALUES[n-1] + knapsack_problem(target_weight - WEIGHTS[n-1],n-1) # Meet (target_weight - WEIGHTS[n th item ]) with (n-1) no of items
        print(f'n={n} n_inlcuded value = {n_inlcuded}')
        n_exculded = knapsack_problem(target_weight,n-1)
        print(f'n={n} n_exculded value = {n_exculded} \n')

        return max(n_inlcuded , n_exculded)

def knapsack_problem_dp(target_weight,n):

    # define 2D matrix 
    # no of rows n+1 , no of items + 1 , 0th row where we do not take any item, 1st row where we take 1 item, 2nd row where we take first 2 items
    # columns = (target_weight+1), from 0 kg to target_weight kg 
    # initialize with 0
    S=[[0 for _ in range(target_weight+1)] for _ in range(n+1)]
    print(S)
    # O(n * target_weight) = pseudo polynomial runtiem complex
    
    for item in range(1,n+1):
        for w in range(1,target_weight+1):
            # print(f'item = {item} weight w = {w}')
            # ie we need to reach weight w, by not taking item i so consider max value of i-1 no of items
            item_excluded = S[item-1][w]
            item_included = 0
            
            if WEIGHTS[item] <= w: # So we are taking the item, hence value_of_item + max_value_of_previous_items_considering_their_total_weight
                item_included = VALUES[item] + S[item-1][w - WEIGHTS[item]]
            S[item][w] = max(item_included, item_excluded)

    knapsack_problem_dp_show(target_weight,n,S)
    return S[n][target_weight]

def knapsack_problem_dp_show(target_weight,n,S):
    # print Solution 2-D matrix
    print('print Solution 2-D matrix')
    for i in range(n+1):
        for j in range(target_weight+1):
            print(S[i][j], end=' ')
        print('\n')

    # which items we take ?
    # when vertically we see a value increment while weight remain same , start from END side ie [n][target_weight]
    # we decrement weight by weight of item 

    target_weight = CONSTRAINT_WEIGHT
    n = N
    for i in range (n,0,-1):
        print(f'S[{i-1}][{target_weight}] = {S[i-1][target_weight]} S[{i}][{target_weight}]={S[i][target_weight]}')
        if (S[i][target_weight]>0) and (S[i-1][target_weight] < S[i][target_weight]):
            print(f'        we include item #{i}\n')
            target_weight = target_weight - WEIGHTS[i]

if __name__ == '__main__':
    print('KNAPSACK PROBLEM - (0,1)')
    print(f'WEIGHTS - {WEIGHTS}')
    print(f'VALUES - {VALUES}')
    print(f'CONSTRAINT_WEIGHT (MAX CAPCITY )= {CONSTRAINT_WEIGHT}')
    print(f'Max Value = {knapsack_problem(target_weight = CONSTRAINT_WEIGHT, n = N)}')

    print(f'\nknapsack_problem_dp(target_weight = {CONSTRAINT_WEIGHT}, no of item = {N}) = {knapsack_problem_dp(target_weight = CONSTRAINT_WEIGHT, n = N)}')
