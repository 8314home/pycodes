# 3. Sparse Matrix to Flattened Map
# Scenario: Convert a nested dictionary representing a sparse matrix {"row1": {"col1": 5}, "row2": {"col3": 10}} 
# into a flat list of tuples (row, col, value) using a nested list comprehension.


sparse_inventory = {
    "Warehouse_A": {"apples": 50, "oranges": 20},
    "Warehouse_B": {"bananas": 100, "apples": 10},
    "Warehouse_C": {"grapes": 300, "apples": 0},
    "Warehouse_D": {} 
}

expected_outcome = [
    ('Warehouse_A', 'apples', 50),
    ('Warehouse_A', 'oranges', 20),
    ('Warehouse_B', 'bananas', 100),
    ('Warehouse_B', 'apples', 10),
    ('Warehouse_C', 'grapes', 300),
    ('Warehouse_C', 'apples', 0)
]

# Performance: List comprehensions are generally faster than .append()
#  because they are optimized at the C level within Python.
result_list = []

for w_key,v_dict in sparse_inventory.items():
    #v is a dict 
    for k,v in v_dict.items():
        t = (w_key, k, v)
        result_list.append(t)
print(result_list)

# result_list = [
#     (w_key, k, v) 
#     for w_key, v_dict in sparse_inventory.items() 
#     for k, v in v_dict.items()
# ]

# 4. Permission Intersection (RBAC)
# Scenario: A user has multiple roles. Each role is a set of permissions.
# Find the common permissions across all roles (Intersection) and 
# the unique permissions available only to one specific role.

# The roles assigned to a specific user
user_roles = {
    "Analyst": {"view_data", "export_csv", "view_dashboard"},
    "Developer": {"view_data", "query_api", "view_dashboard", "edit_code"},
    "Auditor": {"view_data", "view_dashboard", "read_logs"}
}

common_permissions = {'view_data', 'view_dashboard'}
# Note: These are permissions that are NOT shared across any roles
unique_permissions = {'export_csv', 'query_api', 'edit_code', 'read_logs'}

from collections import Counter

all_perm= [ v for v_set in user_roles.values() for v in v_set]

counter_obj = Counter(all_perm)
print(counter_obj)

common_permissions = {k for k,v in counter_obj.items() if v == len(user_roles)}
unique_permissions = {k for k,v in counter_obj.items() if v == 1}

print(common_permissions)
print(unique_permissions)


# 5. Time-Series Gap Filler
# Scenario: You have a list of sensor readings with timestamps. 
# Some minutes are missing. Identify the missing timestamps within a range 
# and "impute" them with a default value of 0.

# Raw sensor logs with gaps

def time_series_imputed():
    sensor_readings = [
        {"timestamp": 1698830001, "value": 24.5},
        {"timestamp": 1698830002, "value": 24.7},
        {"timestamp": 1698830003, "value": 25.1},
        # Gap at ...004
        {"timestamp": 1698830005, "value": 24.2},
        {"timestamp": 1698830006, "value": 23.9},
        # Gap at ...007
        # Gap at ...008
        {"timestamp": 1698830009, "value": 24.0}
    ]
    expected_op = [
        {"timestamp": 1698830001, "value": 24.5},
        {"timestamp": 1698830002, "value": 24.7},
        {"timestamp": 1698830003, "value": 25.1},
        {"timestamp": 1698830004, "value": 0.0},  # Imputed
        {"timestamp": 1698830005, "value": 24.2},
        {"timestamp": 1698830006, "value": 23.9},
        {"timestamp": 1698830007, "value": 0.0},  # Imputed
        {"timestamp": 1698830008, "value": 0.0},  # Imputed
        {"timestamp": 1698830009, "value": 24.0}
    ]
    actual_data = { r["timestamp"]: r["value"]  for r in sensor_readings}

    min_timestamp = min(actual_data.keys())
    max_timestamp = max(actual_data.keys())

    imputed_list = []
    for x in range(min_timestamp,max_timestamp+1):
        imputed_list.append({"timestamp": x, "value": actual_data.get(x, 0.0)})
    return imputed_list
        

print(f'\n\n\n')
print(time_series_imputed())


# 6. Inverted Index Builder
# Scenario: Given a list of documents [{"id": 1, "text": "data engine"}, {"id": 2, "text": "engine oil"}],
# create a dictionary where each word maps to a set of document IDs.
# Concepts: collections.defaultdict, string splitting, set updates.

ip_documents = [
    {"id": 101, "text": "data engine pipeline"},
    {"id": 102, "text": "data quality check"},
    {"id": 103, "text": "spark engine optimization"},
    {"id": 104, "text": "spark data pipeline"}
]
expected_op_inverted_index = {
    "data": {101, 102, 104},
    "engine": {101, 103},
    "pipeline": {101, 104},
    "quality": {102},
    "check": {102},
    "spark": {103, 104},
    "optimization": {103}
}
import json

final_dict = dict()
for d in ip_documents:
    for word in d["text"].split(' '):
        if word not in final_dict:
            final_dict[word] = set()
        final_dict[word].add(d["id"])
         

print(f'\n\n {final_dict}')

from collections import defaultdict

# Initialize with 'set' as the default factory
final_dict = defaultdict(set)

for d in ip_documents:
    for word in d["text"].split(): # split() without ' ' handles multiple spaces too
        final_dict[word].add(d["id"])

# To print it as a standard dict:
print(dict(final_dict))


# 7. Multi-Key GroupBy Aggregator
# Scenario: Without using Pandas, take a list of sales records and group them by (year, region). 
# The result should be a dict where the key is a tuple and the value is a sum of revenue.
# Concepts: Tuple keys in dicts, dict.get(key, default).

sales_records = [
    {"year": 2023, "region": "EMEA", "revenue": 5000, "product": "SaaS"},
    {"year": 2023, "region": "APAC", "revenue": 3000, "product": "Hardware"},
    {"year": 2023, "region": "EMEA", "revenue": 2500, "product": "Support"},
    {"year": 2024, "region": "EMEA", "revenue": 7000, "product": "SaaS"},
    {"year": 2024, "region": "APAC", "revenue": 4500, "product": "SaaS"},
    {"year": 2023, "region": "APAC", "revenue": 1200, "product": "Support"}
]

expected_op ={
    (2023, "EMEA"): 7500,
    (2023, "APAC"): 4200,
    (2024, "EMEA"): 7000,
    (2024, "APAC"): 4500
}
# Multi key sort
new_list = sorted(sales_records, key=lambda d: (d["region"], -d["revenue"]))
print(f'\n\n {new_list}')


# Tuple can be dict key
aggregated = {}

for d in sales_records:
    key = (d["year"], d["region"])
    value = aggregated.get(key,0) + d["revenue"]

    aggregated[key] = value

print(f'\n\n {aggregated}')

for t,v in aggregated.items():
    print(f'{t}: {v}')



# 8. Dependency Graph Validator
# Scenario: Given a list of tasks and their dependencies [("taskB", "taskA"), ("taskC", "taskB")], 
# find all tasks that can start immediately (tasks with no dependencies) and tasks that are "orphaned."

# List of all tasks in the system
all_tasks = {"Fetch_Data", "Clean_Data", "Analyze_Data", "Send_Email", "Archive_Data", "Ghost_Task"}

# Dependency pairs: (Task that depends on something, The parent task it needs)
dependencies = [
    ("Clean_Data", "Fetch_Data"),
    ("Analyze_Data", "Clean_Data"),
    ("Send_Email", "Analyze_Data"),
    ("Archive_Data", "Clean_Data")
]

#starter_tasks = {"Fetch_Data"} 
#orphaned_tasks = {"Ghost_Task"}

# 1. Identify all tasks that REQUIRE something (the dependents)
dependents = {t[0] for t in dependencies}
print(f'\n\n dependents = {dependents}')

# 2. Identify all tasks that are PART of a relationship (either parents OR children)
involved_tasks = {task for pair in dependencies for task in pair}
print(f'involved_tasks = {involved_tasks}')

# 3. Starter Tasks: Involved in the graph, but don't depend on anything
# Logic: (All involved) - (Those that depend on something)
starter_tasks = involved_tasks - dependents

# 4. Orphaned Tasks: In the inventory, but not in the graph
orphaned_tasks = all_tasks - involved_tasks

print(f"Starter Tasks: {starter_tasks}")   # {'Fetch_Data'}
print(f"Orphaned Tasks: {orphaned_tasks}") # {'Ghost_Task'}



nested_log = {
    "event_id": "999-ABC",
    "user": {
        "profile": {
            "name": "Shubmukh",
            "role": "Principal Engineer"
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    },
    "metadata": {
        "source": "mobile_app",
        "version": 1.2
    }
}

final_dict = dict()

def recur_nested_log_process(incoming_dict,final_dict,parent_key=''):
    for k,v in incoming_dict.items():

        new_key = parent_key+'_'+k if parent_key else k

        if type(v) is not dict:
            final_dict[new_key] = v 
        else:
            # recur call when v is dict as well
            print(f'recur call for - {k}')
            recur_nested_log_process(v,final_dict,new_key)

recur_nested_log_process(nested_log,final_dict)
print(f'final_dict = {final_dict}')


# 10. Top-K Elements with Lambda
# Scenario: Given a list of product reviews (dicts with score and category),
# find the top 3 highest-rated products in a specific category, breaking ties using the product name length.

# 10. Top-K Elements with Lambda
# This final problem tests your ability to perform complex sorting
#  and multi-level tie-breaking using functional Python.
#  This is a very common task for building ranking systems or leaderboards.
#      The Input DataYou have a list of products with their review scores. 
#  Note that several items have identical scores.python

products = [
    {"name": "Laptop", "score": 95, "cat": "Tech"},
    {"name": "Monitor", "score": 88, "cat": "Tech"},
    {"name": "UltraWide-Monitor", "score": 88, "cat": "Tech"}, # Tie with Monitor
    {"name": "Keyboard", "score": 95, "cat": "Tech"},          # Tie with Laptop
    {"name": "Desk", "score": 90, "cat": "Furniture"},
    {"name": "Mouse", "score": 82, "cat": "Tech"},
    {"name": "Graphic-Card", "score": 95, "cat": "Tech"}       # Another 95!
]
# Use code with caution.The GoalFilter: 
# Only include products in the "Tech" category.
# Multi-Sort:Primary: Score (Highest first).
# Secondary (Tie-breaker): Length of the Name (Longest first).
# Slice: Take only the Top 3 results.
# Format: The final output should be a list of just the names.
# Expected Outcome
expected_op_10 = {
  "Tech": [
    "Graphic-Card",
    "Keyboard",
    "Laptop"
  ],
  "Furniture": [
    "Desk"
  ]
}
#(Explanation: Graphic-Card has 12 chars, Keyboard has 8, Laptop has 6. All have score 95.)
  
# intermediate_dict = {
#     "Tech": [{r1}, {r2}, {r2}] sorted list
# }

print(f'\n\n')
intermediate_dict = defaultdict(list)

for d in products:
    category = d["cat"]
    intermediate_dict[category].append(d)

print(intermediate_dict)

for k,v_list in intermediate_dict.items():
    sorted_list = sorted(v_list,key = lambda d: (-d["score"], -len(d["name"]))) # list of dict , get dict[name]
    intermediate_dict[k] = [d["name"] for d in sorted_list[:3]]

print(json.dumps(intermediate_dict,indent=2))







print(f'\n------problem 11---------\n')

# 11. Schema Registry Version Merger
# Scenario: You have multiple versions of a schema (dicts). 
# Merge them so that the final dict contains the most recent version of every field,
# but keep a _version_history list for every key showing all its past data types.
# Concepts: Dictionary merging, nested lists, tracking state.

# Version 1 (The original)
v1 = {
    "user_id": "INT",
    "name": "STRING",
    "email": "STRING"
}

# Version 2 (Added 'age', changed 'user_id' to BIGINT)
v2 = {
    "user_id": "BIGINT",
    "name": "STRING",
    "email": "STRING",
    "age": "INT"
}

# Version 3 (Added 'is_active', changed 'age' to FLOAT)
v3 = {
    "user_id": "BIGINT",
    "name": "STRING",
    "age": "FLOAT",
    "is_active": "BOOLEAN"
}

# The input for your function
versions = [v1, v2, v3]
pr_10_expected_op ={
    "user_id": {
        "current_type": "BIGINT",
        "version_history": ["INT", "BIGINT"]
    },
    "name": {
        "current_type": "STRING",
        "version_history": ["STRING"]
    },
    "email": {
        "current_type": "STRING",
        "version_history": ["STRING"]
    },
    "age": {
        "current_type": "FLOAT",
        "version_history": ["INT", "FLOAT"]
    },
    "is_active": {
        "current_type": "BOOLEAN",
        "version_history": ["BOOLEAN"]
    }
}


final_schema_version = {}

for v_dict in versions:
    for k,v in v_dict.items():
        if k not in final_schema_version: # 1st time 
            final_schema_version[k]= { "current_type": v, "version_history": [v]}
        else: # already present
            # element of final_schema_version[k] 
            element_dict = final_schema_version[k]
            element_dict["current_type"] = v 
            # 2. Check deduplication: Only append if it's a new type
            if v != element_dict["version_history"][-1]:
                element_dict["version_history"].append(v)
print(final_schema_version)
            

print(f'\n------problem 12---------\n')

# 12. Multi-Level Anagram Grouper
# Scenario: Given a massive list of strings, group words that are anagrams of each other into nested lists. 
# For an extra challenge, group these sets by the length of the words.
# Concepts: collections.defaultdict(list), sorted() as a dict key, nested dictionaries.

words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent", "rat", "art"]

pr_12_op = {
    3: [
        ["eat", "tea", "ate"], # Anagrams of length 3
        ["tan", "nat"],        # Anagrams of length 3
        ["bat"],               # No anagram match
        ["rat", "art"]         # Anagrams of length 3
    ],
    6: [
        ["listen", "silent"]   # Anagrams of length 6
    ]
}


final_dict = defaultdict(list)
for w in words:
    if len(w) not in final_dict:
        final_dict[len(w)].append([w]) # if length is not there
    else:
        list_of_list = final_dict[len(w)]
        anagram_found=0
        for l in list_of_list:
            first_elem_of_l = l[0]
            if sorted(first_elem_of_l) == sorted(w): # anagram list found
                l.append(w)
                anagram_found=1
                break
        # all sub lists travered no match anagram list- creat enew list
        if anagram_found==0:
            final_dict[len(w)].append([w])

print(f'{dict(final_dict)}')



# 13. Log Stream Sessionizer
# Scenario: You have a list of user actions with timestamps. 
# Create "sessions" for each user where a session ends if there is a gap of more than 30 minutes between actions.
# Concepts: Time-series logic, grouping, stateful iteration.

# 30-minute inactivity window
logs = [
    (10, "user_1", "login"),
    (15, "user_1", "click"),
    (20, "user_2", "login"),
    (45, "user_1", "click"),  # Still user_1 session (gap: 30 mins)
    (55, "user_2", "logout"), # Still user_2 session (gap: 35 mins - WRONG, it's 35 mins from 20)
    (80, "user_1", "logout")  # New user_1 session (gap: 35 mins since 45)
]

pr_13_op = {
    "user_1": [
        ["login", "click", "click"], # Session 1 (Times: 10, 15, 45)
        ["logout"]                  # Session 2 (Time: 80 - started because 80-45 > 30)
    ],
    "user_2": [
        ["login"],                  # Session 1 (Time: 20)
        ["logout"]                  # Session 2 (Time: 55 - started because 55-20 > 35)
    ]
}


# two state problem 
# keep last seen state time
# use a new_session_flag 
def pr_13(logs):
    final_answer = defaultdict(list)
    user_state_dict = {}

    for time,user,action in logs:
        if (user not in final_answer) or (user_state_dict[user] + 30 < time):
            final_answer[user].append([action])
        else:
            final_answer[user][-1].append(action)
        #keep state  last tiem seen
        user_state_dict[user] = time 
    return dict(final_answer)

print(pr_13(logs))


# 14. The "Missing Transaction" Audit (Set Mastery)As a Data Engineer, 
# you often have to reconcile data between two systems (e.g., your App DB vs. Stripe/PayPal). 
# Using for loops to find missing items is \(O(N^2)\) and slow.

# The Task:You have two lists of IDs.
# order_ids: ["ORD1", "ORD2", "ORD3", "ORD5"]
# payment_ids: ["ORD1", "ORD2", "ORD4", "ORD5"]
# Return a dictionary with:
# ghost_orders: 
# Orders that exist but were never paid.orphan_payments: 
# Payments received for orders that don't exist in our system.reconciled_count:
#     The number of orders that match perfectly in both systems


order_ids = ["ORD1", "ORD2", "ORD3", "ORD5", "ORD7", "ORD8"]
payment_ids = ["ORD1", "ORD2", "ORD4", "ORD5", "ORD9"]

pr_14_expected_op = {
    "ghost_orders": ["ORD3", "ORD7", "ORD8"],  # In orders, but NOT in payments
    "orphan_payments": ["ORD4", "ORD9"],     # In payments, but NOT in orders
    "reconciled_count": 3                    # ORD1, ORD2, ORD5 match
}

ghost_orders = list(set(order_ids) - set(payment_ids))
orphan_payments = list(set(payment_ids) - set(order_ids))
reconciled_count = len(set(payment_ids).intersection(set(order_ids)))

print(ghost_orders)
print(orphan_payments)
print(reconciled_count)

        
# 15. The API Rate Limiter (Sliding Window)Scenario: You have a script that scrapes a public API. 
# The API has a strict limit: Maximum 3 calls in any 10-second window. If you exceed this, you get blocked.

pr_15_requests = [1, 2, 3, 4, 11, 12, 13, 15, 25]

# [1, 2, 3] are ok. 
# 4 is BLOCKED (calls 1,2,3 are within 10s). 
# 11 is OK (only 2,3 are within 10s of 11).
pr_15_exp_op = [1, 2, 3, 11, 12, 15, 25] 



# --------------------------------------


