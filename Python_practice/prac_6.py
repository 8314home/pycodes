
# High-Cardinality Deduplication
# Scenario: Given a stream of logs (list of dicts), 
# keep only the latest entry for each user_id based on a timestamp, 
# but only if the event_type is in an "allow-list" set.

# give me data set to work with .
# do not give me code or logic to implement.

# dict = key -> user_id , compare timestamp between 2 records and event type: keep entire data

import json 
from datetime import datetime

logs = [
    {"user_id": "U101", "timestamp": "2023-10-01 10:00:00", "event_type": "login", "data": "session_a"},
    {"user_id": "U102", "timestamp": "2023-10-01 10:05:00", "event_type": "purchase", "data": "item_x"},
    {"user_id": "U101", "timestamp": "2023-10-01 10:10:00", "event_type": "click", "data": "button_1"},
    {"user_id": "U103", "timestamp": "2023-10-01 10:12:00", "event_type": "login", "data": "session_b"},
    {"user_id": "U102", "timestamp": "2023-10-01 10:15:00", "event_type": "logout", "data": "end_session"},
    {"user_id": "U101", "timestamp": "2023-10-01 10:20:00", "event_type": "purchase", "data": "item_y"},
    {"user_id": "U104", "timestamp": "2023-10-01 10:22:00", "event_type": "error", "data": "404_not_found"},
    {"user_id": "U102", "timestamp": "2023-10-01 10:25:00", "event_type": "login", "data": "session_c"},
    {"user_id": "U103", "timestamp": "2023-10-01 10:30:00", "event_type": "purchase", "data": "item_z"},
    {"user_id": "U101", "timestamp": "2023-10-01 10:02:00", "event_type": "login", "data": "session_late"},
    {"user_id": "U104", "timestamp": "2023-10-01 10:40:00", "event_type": "login", "data": "session_d"},
    {"user_id": "U101", "timestamp": "2023-10-01 10:35:00", "event_type": "logout", "data": "final_exit"}
]

allow_list = {"login", "purchase", "click"}


expected_outcome = [
    {"user_id": "U101", "timestamp": "2023-10-01 10:20:00", "event_type": "purchase", "data": "item_y"},
    {"user_id": "U102", "timestamp": "2023-10-01 10:25:00", "event_type": "login", "data": "session_c"},
    {"user_id": "U103", "timestamp": "2023-10-01 10:30:00", "event_type": "purchase", "data": "item_z"},
    {"user_id": "U104", "timestamp": "2023-10-01 10:40:00", "event_type": "login", "data": "session_d"}
]

from datetime import datetime

def keep_latest_entry_for_user_id(logs):
    mem = dict() # { user_id : original_record}

    # filter events of allow_list
    filtered = filter(lambda r: r["event_type"] in allow_list, logs)
    # create a new sorted list
    sorted_list = sorted(filtered, key=lambda r: datetime.strptime(r["timestamp"], "%Y-%m-%d %H:%M:%S"), reverse=True)

    # take 1st value for every user
    for r in sorted_list:
        user_id = r["user_id"]
        if user_id not in mem:
            mem[user_id] = r
    return mem


if __name__ == '__main__':
    print(json.dumps(keep_latest_entry_for_user_id(logs),indent=2))