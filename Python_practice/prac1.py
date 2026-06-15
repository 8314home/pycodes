# 1. Log Parsing:
# You have a log entry string:
# log_line = "2023-10-01|ERROR|Database connection failed" 
# How do you extract just the status (ERROR) and the message (Database connection failed) 
# into two separate variables using a single string method?

log_line = "2023-10-01|ERROR|Database connection failed" 
ans = log_line.split('|')[1]
print(ans)


# 1. The Identity vs. Equality Challenge
# Based on your notes about is and ==, what will be the output of this snippet?
# python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("\n\n problem-2 ")
print(list_a == list_b)
print(list_a is list_b)
print(list_a is list_c)

# 2. Lists vs. Tuples (Immutability)
# You mentioned String is immutable. Tuple is also a sequence type and is immutable.
# Problem: You have a record from a database: user = ("ID101", "John", "Admin").
# If you try to execute user[2] = "SuperUser", what happens?
# If you needed to change that value, how would you "update" that tuple (hint: think about your notes on creating new objects)?




parrot="Norwegian Blue"
print(parrot[-4:-2])

# 2. Lists vs. Tuples (Immutability)
#  my answer
user = ("ID101", "John", "Admin")
user = (user[0],"SuperUser",user[2])
print(user)

#3. Dictionary Basics (Hash Maps) -dict(), set() - O(1) operation
d = {'A': 1, 'B': 2 }
print(d.get('C',0))

#4. List Comprehension (Modern Loop) My answer
number = "9,123,234,345,456"
p4 = ''.join([x for x in number if x in '1234567890'])
print(int(p4))

# Problem 5: Data Reconciliation
# Intersection: Find IDs that exist in both (to perform updates).
# Difference: Find IDs in source_ids that are missing from target_ids (to perform inserts).
# Symmetric Difference: Find IDs that are in one or the other, but not both.

source_ids = ["ID1", "ID2", "ID3", "ID5"]
target_ids = ["ID3", "ID4", "ID5", "ID6"]

# Problem-6
fruit={"apple":"A for apple","orange":"O for orange" ,"lemon":"l for lemon"}


# dict -> tuple using below we can convert them to tuple.
f_tuple=tuple(fruit.items()) 
print(f_tuple)
# tuple -> dict

print(dict(f_tuple))

#frozenset - immutable set - can be used as keys 


testString="This is MAX"
testSet=set(testString)
vowelSet={'a','e','i','o','u','A','E','I','O','U'}
conjunctionSet={' ','.',';'}

finalSet=(testSet.difference(vowelSet)).difference(conjunctionSet)
print("All the consonants in text are: {}".format(finalSet))
print("All the consonants in text are: {}".format(finalSet))    


# Problem 5: Data Reconciliation
# You have two lists of IDs from different databases:
# python

def problem5():
    source_ids = ["ID1", "ID2", "ID3", "ID5"]
    target_ids = ["ID3", "ID4", "ID5", "ID6"]

    source_ids_set = set(source_ids)
    target_ids_set = set(target_ids)
    #Intersection: Find IDs that exist in both (to perform updates).
    print(source_ids_set.intersection(target_ids_set))
    # Difference: Find IDs in source_ids that are missing from target_ids (to perform inserts).
    print(source_ids_set.difference(target_ids_set))
    print(target_ids_set.difference(source_ids_set))
    # Symmetric Difference: Find IDs that are in one or the other, but not both.
    print((source_ids_set.difference(target_ids_set)).union(target_ids_set.difference(source_ids_set)))
    print(source_ids_set.symmetric_difference(target_ids_set))

problem5()

# Problem 8: File Reading
# Write a snippet to read a file named data.txt line by line and print only the lines that contain the word "ERROR".

# with open('file1.txt','r') as data_txt:
#     contents = data_txt.readlines()
#     for line in contents:
#         if 'ERROR' in line:
#             print(line)
# In your code, data_txt.readlines() reads the entire file into memory 
# and stores it as a list of strings before the loop even starts.
# The Risk: If your log file is 20GB, your script will crash with an OutOfMemory error.
# The DE Approach: Iterate over the file object directly. This creates a "generator" that only loads one line at a time into memory.
# Refactored for Big Data:

def problem8():
    with open('file1.txt', 'r') as data_txt:
        for line in data_txt:
            if 'ERROR' in line:
                print(line.rstrip()) # strip() removes the extra newline from the file
print("\nproblem8\n")
problem8()


# Problem 9: The Lambda Filter
# You have a list of dictionary records:
# python
# logs = [
#     {"level": "INFO", "msg": "Started"},
#     {"level": "ERROR", "msg": "Failed connection"},
#     {"level": "DEBUG", "msg": "Checking port"},
#     {"level": "ERROR", "msg": "Out of memory"}
# ]
# Use code with caution.

# Use filter() and a lambda to get only the records where the level is "ERROR".
# Use map() and a lambda to create a list of just the messages (msg)

def problem9():
    logs = [
        {"level": "INFO", "msg": "Started"},
        {"level": "ERROR", "msg": "Failed connection"},
        {"level": "DEBUG", "msg": "Checking port"},
        {"level": "ERROR", "msg": "Out of memory"}
    ]
    filtered_list = list(filter(lambda log: log['level'] == 'ERROR', logs))
    print(filtered_list)
    msg_list = list(map(lambda log: log['msg'], logs))
    print(msg_list)

print('\nproblem-9\n')
problem9()

# Problem 10: Sorting Complex Structures
# Given this list of tuples:
# data = [("apple", 5), ("banana", 2), ("orange", 8), ("almond", 2)]
# Task: Use the sorted() function with a lambda as the key to sort this list 
# by the numeric value (the second item) in descending order.

# .sort(): Modifies the original list in place. It returns None.
# sorted(): Leaves the original list alone and returns a brand new sorted list.


# Bonus: If two items have the same numeric value (like banana and grapes),
# how would you ensure they are then sorted alphabetically by the name?

# Regarding the Bonus (sorting by value descending, then name ascending for ties):
# Since Python's sorted() is stable, you could sort twice, but the professional way is to use a tuple in the lambda:

def problem10():
    data = [("apple", 5), ("banana", 2), ("orange", 8), ("almond", 2)]
    sorted_list = sorted(data,key=lambda x: x[1], reverse=True)
    print(sorted_list)

    sorted_list2 = sorted(data, key=lambda x: (-x[1], x[0]))
    print(sorted_list2)
print('\nproblem-9\n')
problem10()


# (The negative sign flips the numeric sort to descending, while the name remains ascending).

# Problem 11: The "Lazy" Map/Filter
# If you run result = map(lambda x: x*2, [1, 2, 3]) and then print(result), 
# why does it show something like <map object at 0x...> instead of the list [2, 4, 6]? How do you get the actual list?
# The Lazy Object
# You get <map object> because map and filter are iterators (lazy evaluation). 
# They don't compute the values until you ask for them (e.g., by looping or converting to a list()).
# This saves memory in data engineering pipelines.


# Problem 12:
# You need to scrape 50 different websites. Each request takes 2 seconds of waiting.
# Which should you use: Threading or Multiprocessing?
# Why? (Mention the GIL - Global Interpreter Lock in your answer).


# Problem 13:
# You have a 1GB CSV file and you need to calculate the complex mathematical hash of every single row.
# Which should you use? Why?


# Generator vs Decorator

def print_one_by_one(n):
    i=1
    while i <=n:
        yield i
        i += 1

iter_var = print_one_by_one(10)
print(iter_var.__next__())
print(iter_var.__next__())
print(iter_var.__next__())
print(iter_var.__next__())

from datetime import datetime

def log_call(func):
    def wrapper(*args,**kwargs):
        ## statements
        print(f'print in wrapper: {datetime.today()}')
        return func(*args,**kwargs)
    return wrapper

@log_call
def say_hi():
    print('Hi')

say_hi()


#Problem -13 .1  Generator Practice Problem
# In Data Engineering, we use generators to process Large Files or Infinite Streams. 
# Scenario:
# You have a simulated sensor that generates a reading every second. You want to process these readings without creating a massive list.
# The Task:
# Write a Generator Function called get_readings(n) that uses yield to return n random integers (between 1 and 100).
# Write a for loop that iterates over this generator and prints only the readings that are greater than 80.


# Bonus: Why is this better than returning a list of n numbers if n = 10,000,000? 
# If N = 10,000,000, the generator uses constant memory (only the space for one integer at a time).
import random

def get_readings(n):
    for x in range(n):
        yield random.randint(0,100)
N=10
iter_step = get_readings(N)

for t in iter_step:
    if t > 50:
        print(t, end=' ')

# Decorator Practice Problem
# Since you are a Data Engineer, you often need to measure the execution time of your data ingestion functions.
# The Task:
# Write a decorator called @time_it.
# It should print: Function <name> took <X> seconds to run.
# Apply it to a simple function that uses time.sleep(2).
# How would you write the code for this?

print(f'\nproblem -Decorator\n')
import time
import functools

def timeit(func):
    print(f'function_name_timeit = {func.__name__}')

    @functools.wraps(func) # This ensures sample_function.__name__ stays 'sample_function'
    def funcwrap(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f' T1={t1} , T2 = {t2} , {func.__name__} executed in T2-T1 = {t2-t1} seconds')
        return result
    return funcwrap

@timeit
def sample_function():
    print(f'function_name_sample_function = {sample_function.__name__}')
    time.sleep(2)

sample_function()

# @functools.wraps(func) 
# is so important—it "copies" the name from the original function to the wrapper so your logs stay clean.


# Problem 12 & 13: Concurrency (The Final Refresh)

# Scenario A: You are downloading 500 CSV files from an S3 bucket. Each file is small, but the network latency is high.
# Scenario B: You have a massive list of strings and you need to perform heavy Regex cleaning on every string.
# Which scenario is I/O-bound and which is CPU-bound?
# Which one should use the threading module and which should use multiprocessing?
# The "Why": Explain what the GIL (Global Interpreter Lock) does when 4 threads try to perform heavy math at the same time.

# Concurrency (Threads vs. Processes)
# This is a high-level interview favorite for experienced engineers.
# The Theory:
# Threading: Shares memory. Good for I/O (Waiting for a database or API).
# Multiprocessing: Separate memory. Good for CPU (Heavy math, data parsing, image processing).


# The Answer to 3: The Global Interpreter Lock (GIL)
# In a senior interview, this is the "make or break" technical concept.
# The Theory:
# The GIL is a mutex (a lock) that allows only one thread to hold control of the
# Python interpreter at any given time. This means that even if you have a CPU with 16 cores, a single Python process can only execute one line of bytecode at a time.
# How it affects your scenarios:
# In Scenario A (I/O - Threads): When Thread 1 starts downloading a file from S3, 
# it "waits" for the network. While it waits, it releases the GIL. 
# This allows Thread 2 to start its download immediately. 
# This is why threading works great for API calls—you are "concurrently waiting."

# In Scenario B (CPU - Multi-processing): If you try to use 4 threads to do heavy Regex or Math, Thread 1 will grab the GIL and start calculating. Thread 2, 3, and 4 will sit idle, fighting to grab the lock. They end up running sequentially, not in parallel. In fact, it might even be slower due to the overhead of switching between threads.
# The Solution:
# multiprocessing bypasses the GIL by creating entirely separate Python instances (interpreters) for each core. Since each process has its own GIL, they can truly run in parallel on separate CPU cores.

# A Threading Example

import threading
import requests
import time

# A public API that doesn't require authentication

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
pokemon_to_fetch = ["pikachu", "charizard", "bulbasaur", "squirtle", "mewtwo"]

def inside_thread_call_api(pname):
    try:
        response = requests.get(url=BASE_URL+ pname + '/', timeout=5)
        if response.status_code == 200:
            weight = response.json().get('weight')
            print(f"[Result] {pname.capitalize()} weighs {weight}\n")
        else:
            print(f'ERROR - fetcing data for {pname}')
    except Exception as e:
        print(f"[Exception] Request failed for {pname}: {e}")
        raise e

def run_threads_parallel():
    #create threads
    thread_list = []
    start_time = time.time()

    #call thread - in loop
    for pname in pokemon_to_fetch:
        t = threading.Thread(target=inside_thread_call_api,name=f't_{pname}', args=(pname,))
        thread_list.append(t)
        t.start()

    # merge threads
    for t in thread_list:
        t.join()
    end_time = time.time()
    print(f"\nFinished all API calls in {end_time - start_time:.2f} seconds.")

run_threads_parallel()


# Problem 14: The "Two-Pointer" / "Sliding Window" Pattern
# You are given an array of integers nums and an integer target.
# Task: Return the indices of the two numbers such that they add up to target.
# Constraint: Can you do it in 
#  time? (Hint: Use a Dictionary to store the numbers you have already seen).
# Example:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (because 2 + 7 = 9)


# Problem 15: Grouping & Aggregation (The "SQL-on-Python" Test)
# In DE, we often "group by" without using Pandas.
# The Input: A list of dictionaries representing transactions:
# data = [{"user": "A", "amt": 10}, {"user": "B", "amt": 5}, {"user": "A", "amt": 20}]
# The Task: Create a dictionary that sums the amt for each user.
# Target Output: {"A": 30, "B": 5}
# Python Concept: Dictionary membership, dict.get(), or collections.defaultdict.
# Problem 16: List of Intervals (The "Overlapping Data" Test)
# This is a common "Log Analysis" problem.
# The Input: A list of tuples representing start/end times: intervals = [(1, 3), (2, 4), (6, 8)]
# The Task: Merge overlapping intervals.
# Target Output: [(1, 4), (6, 8)] (Because 1-3 and 2-4 overlap).
# Python Concept: Sorting lists, list slicing, and conditional logic.
# Problem 17: Flattening Nested Structures (The "JSON Cleanup" Test)
# DEs often deal with "messy" JSON.
# The Input: A nested list that can have any depth: nested = [1, [2, [3, 4], 5], 6]
# The Task: Write a function to flatten this into a single list.
# Target Output: [1, 2, 3, 4, 5, 6]
# Python Concept: Recursion, type checking (isinstance()), and list extending.
