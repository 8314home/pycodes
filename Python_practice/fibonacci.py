# 

def fibonacci_recursion(n):
    # base case 
    # fibonacci_recursion(0) = 1, fibonacci_recursion(1) = 1
    # fibonacci_recursion(n) = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    if n ==0 or n == 1:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_dp_top_down_mem(n,hash_table):
    # if fib(n) in hash table , return from hash table
    # hash_table has fibonacci_dp_top_down_mem(0)=1 fibonacci_dp_top_down_mem(1)=1 already
    if n in hash_table:
        return hash_table[n]
    # else calculate fib(n) and store in has table and  return hash_table[n]
    else:
        hash_table[n] = fibonacci_dp_top_down_mem(n-1,hash_table) + fibonacci_dp_top_down_mem(n-2,hash_table)
        return hash_table[n]
    
def fibonacci_dp_bottom_up_mem(n,hash_table):

    for i in range(2,n+1):
        hash_table[i] = hash_table[i-1] + hash_table[i-2] 
    return hash_table[n]


if __name__ == '__main__':
    n = 5
    print(f'fibonacci_recursion({n}) = {fibonacci_recursion(n)}')

    hash_table = {0: 1, 1: 1}
    print(f'fibonacci_dp_top_down_mem({n},hash_table) = {fibonacci_dp_top_down_mem(n,hash_table)}')

    hash_tabl2 = {0: 1, 1: 1}
    print(f'fibonacci_dp_bottom_up_mem({n},hash_tabl2) = {fibonacci_dp_bottom_up_mem(n,hash_tabl2)}')
    

