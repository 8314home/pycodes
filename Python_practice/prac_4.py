
import json 

# Asset Data Reconciliation
# Goal:
# Develop a Python function to compare two lists of asset dictionaries
# (representing "yesterday" vs. "today") and identify specific lifecycle changes based on a dynamic unique identifier.


#    previous = [
#         # Standard existing asset
#         {'assetId': "asset-1", 'hostname': "web-01", 'ip': "10.0.1.10", 'riskScore': 45},
#         # Asset that will be modified (IP and Score)
#         {'assetId': "asset-2", 'hostname': "web-02", 'ip': "10.0.1.11", 'riskScore': 72},
#         # Asset that will be removed
#         {'assetId': "asset-3", 'hostname': "db-01",  'ip': "10.0.2.10", 'riskScore': 30},
#         # Asset with a missing field that will be added in 'current'
#         {'assetId': "asset-4", 'hostname': "lb-01",  'ip': "10.0.3.10"} 
#     ]

#     current = [
#         # No change
#         {'assetId': "asset-1", 'hostname': "web-01", 'ip': "10.0.1.10", 'riskScore': 45},
#         # Multiple updates
#         {'assetId': "asset-2", 'hostname': "web-02", 'ip': "10.0.1.88", 'riskScore': 81},
#         # New asset added
#         {'assetId': "asset-6", 'hostname': "cache-01", 'ip': "10.0.4.10", 'riskScore': 20},
#         # Field added (riskScore) and IP changed
#         {'assetId': "asset-4", 'hostname': "lb-01", 'ip': "10.0.3.11", 'riskScore': 10},
#         # Asset added with totally different schema (data integrity test)
#         {'assetId': "asset-9", 'note': "temporary-vm", 'status': "active"}
#     ]

# Expected Output Format

# The output should be a structured dictionary (or JSON-like object) similar to the following:
# json
# {
#   "added": ["asset-6"],
#   "removed": ["asset-3"],
#   "changes": [
#     {
#       "assetId": "asset-2",
#       "updates": {
#         "ip": { "from": "10.0.1.11", "to": "10.0.1.88" },
#         "riskScore": { "from": 72, "to": 81 }
#       }
#     }
#   ]
# }


def reconcile(previous, current, key='assetId'):

    prev_keys = { d[key]: d for d in previous if key in d}
    curr_keys = { d[key]: d for d in current if key in d}

    prev_set = set(prev_keys.keys())
    current_set = set(curr_keys.keys())

    add_items = list(current_set - prev_set)
    remove_items = list(prev_set - current_set)

    common_items = list(prev_set.intersection(current_set))
    final_changes = []


    for c in common_items: # 
        # dict to dict  direct compare
        if prev_keys[c] != curr_keys[c]:  # both are dicts
            each_item_dict = {key:c ,"updates" : []} # Base comparison structure prepare
            keys_to_check = set(prev_keys[c].keys()).union(set(curr_keys[c].keys()))
            dict_item_p = prev_keys.get(c)
            dict_item_c = curr_keys.get(c)
        
            for k in keys_to_check:
                if dict_item_p.get(k) != dict_item_c.get(k):
                    each_item_dict["updates"].append({k : { "from": dict_item_p.get(k), "to": dict_item_c.get(k)}})
            final_changes.append(each_item_dict)

    final_dict = {
        "added": add_items,
        "removed": remove_items,
        "common_items": final_changes
    }

    return final_dict




if __name__ == '__main__':
    # State from the previous scan
    previous = [
        # Standard existing asset
        {'assetId': "asset-1", 'hostname': "web-01", 'ip': "10.0.1.10", 'riskScore': 45},
        # Asset that will be modified (IP and Score)
        {'assetId': "asset-2", 'hostname': "web-02", 'ip': "10.0.1.11", 'riskScore': 72},
        # Asset that will be removed
        {'assetId': "asset-3", 'hostname': "db-01",  'ip': "10.0.2.10", 'riskScore': 30},
        # Asset with a missing field that will be added in 'current'
        {'assetId': "asset-4", 'hostname': "lb-01",  'ip': "10.0.3.10"} 
    ]

    current = [
        # No change
        {'assetId': "asset-1", 'hostname': "web-01", 'ip': "10.0.1.10", 'riskScore': 45},
        # Multiple updates
        {'assetId': "asset-2", 'hostname': "web-02", 'ip': "10.0.1.88", 'riskScore': 81},
        # New asset added
        {'assetId': "asset-6", 'hostname': "cache-01", 'ip': "10.0.4.10", 'riskScore': 20},
        # Field added (riskScore) and IP changed
        {'assetId': "asset-4", 'hostname': "lb-01", 'ip': "10.0.3.11", 'riskScore': 10},
        # Asset added with totally different schema (data integrity test)
        {'assetId': "asset-9", 'note': "temporary-vm", 'status': "active"}
    ]

    diff_dict = reconcile(previous, current, key='assetId')
    
    print(json.dumps(diff_dict, indent=2))
