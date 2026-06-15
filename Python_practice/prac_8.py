
# To count unique users in a 10-minute window for a high-volume stream

test_data_pr_16 = [
    ("user_1", 100),   # T=100: First user
    ("user_2", 200),   # T=200: Second user
    ("user_1", 300),   # T=300: user_1 repeats (Count should not increase)
    ("user_3", 650),   # T=650: Window is [50, 650]. user_1(100) and user_1(300) both inside.
    ("user_4", 701),   # T=701: Window is [101, 701]. user_1(100) expires. 
                       #        BUT user_1 remains because of its t=300 event.
    ("user_5", 901),   # T=901: Window is [301, 901]. user_2(200) and user_1(300) expire.
    ("user_6", 1600)   # T=1600: Huge jump. All previous users expire.
]



from collections import deque, defaultdict

def problem_16(event_list):
    events = deque()
    user_counts = defaultdict(int)

    for u,t in event_list:
        events.append((u, t))
        user_counts[u] += 1

        # loop over event queue, expire events events[0] 1st tuple of queue, events[0][1] = tiemtamp of 1st tuple
        # current record user u, time stamp t 10 min = 600 sec
        while events and (events[0][1] < t - 600):
            expired_user,_ = events.popleft()
            # decrement count
            user_counts[expired_user] -= 1

            # if user count is 0 then del
            if user_counts[expired_user] == 0:
                del user_counts[expired_user]

        print(f'current item = {u}{t} \n distinct user_counts = {len(user_counts.keys())}')

problem_16(test_data_pr_16)


# -----------------------------

rate_limit_test_data_pr_17 = [
    ("user_A", 1),   # Req 1: OK
    ("user_A", 5),   # Req 2: OK
    ("user_B", 6),   # Req 1 for B: OK
    ("user_A", 8),   # Req 3: OK (A hits limit)
    ("user_A", 9),   # Req 4: REJECT (Still within 10s of first request)
    ("user_B", 12),  # Req 2 for B: OK
    ("user_A", 12),  # Req 5: OK (T=1 is evicted, window is now [2, 12], count=3)
    ("user_A", 13)   # Req 6: REJECT (T=5 and T=8 are still active)
]

user_rate_limit_dict = defaultdict(deque)

from collections import deque, defaultdict

# Using a 10-second window as per your comments
WINDOW = 10 
LIMIT = 3

def fn_rate_limit_test_data_pr_17(event_list):
    user_rate_limit_dict = defaultdict(deque)
    
    for u, t in event_list:
        # 1. Cleanup: Always remove expired timestamps for this specific user
        while user_rate_limit_dict[u] and user_rate_limit_dict[u][0] <= t - WINDOW:
            user_rate_limit_dict[u].popleft()
        
        # 2. Check Limit: Is there room in the deque?
        if len(user_rate_limit_dict[u]) < LIMIT:
            user_rate_limit_dict[u].append(t)
            print(f"ACCEPTED: User {u} at {t}")
        else:
            print(f"REJECTED: User {u} at {t} (Limit reached)")
            
        # 3. Debug State
        print(dict(user_rate_limit_dict)) # Convert to dict for cleaner printing

fn_rate_limit_test_data_pr_17(rate_limit_test_data_pr_17)



# Moving Average of Stock Prices

stock_test_data_pr_18 = [
    (150.00, 100),   # T=100: First trade
    (151.00, 200),   # T=200: Price going up
    (152.00, 350),   # T=350: Window is [50, 350]. All 3 prices are in.
    (155.00, 450),   # T=450: Window is [150, 450]. T=100 (150.00) expires.
    (160.00, 550),   # T=550: Window is [250, 550]. T=200 (151.00) expires.
    (140.00, 900)    # T=900: Huge gap. Everything before T=600 expires.
]

stock_price_queue = deque()

def fn_moving_avg_stock_price_pr_18(event_list):
    sum_of_stocks = 0
    for p,t in event_list:
        # clean expired items from left 1st elemnt of deque = stock_price_queue[0] which is tuple
        while stock_price_queue and stock_price_queue[0][1] < t - 300: # 5 min = 300 sec
            s_value,_ = stock_price_queue.popleft()
            sum_of_stocks -= s_value

        stock_price_queue.append((p,t))
        sum_of_stocks += p 

        len_of_stocks = len(stock_price_queue)

        print(f'stock_price_queue = {stock_price_queue} avg = {sum_of_stocks}/{len_of_stocks} = {sum_of_stocks/len_of_stocks}')
        # sum(price for price, timestamp in stock_price_queue)

        #find avg of stock_price_queue

fn_moving_avg_stock_price_pr_18(stock_test_data_pr_18)








