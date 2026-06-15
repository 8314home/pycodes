# The Schema Evolution Detector
# Scenario: You have two JSON-like schemas. 
# Identify which fields were added, which were deleted, and which had a data type change.
# Data: old = {"id": "int", "name": "str"} vs new = {"id": "int", "name": "text", "status": "bool"}.

# Concepts: Dict comparison, Set logic, type checking.

import json

def process_schema_change(old: dict, new: dict):
    # Quick exit if identical
    if old == new:
        return {"added": [], "removed": [], "data_type_change": []}

    old_keys = old.keys()
    new_keys = new.keys()

    # 1. Use Set subtraction for instant results
    added = list(new_keys - old_keys)
    removed = list(old_keys - new_keys)

    # 2. Use Set intersection to find keys present in both
    common_keys = old_keys & new_keys

    # 3. List comprehension for type changes
    data_type_change = [
        {k: f"from {old[k]} to {new[k]}"}
        for k in common_keys 
        if old[k] != new[k]
    ]

    return {
        "added": added,
        "removed": removed,
        "data_type_change": data_type_change
    }

if __name__ == '__main__':
    old = {"id": "int", "name": "str", "created_at": "datetime"} 
    new = {"id": "int", "name": "text", "status": "bool", "created_at": "timestamp"}

    result = process_schema_change(old, new)
    print(json.dumps(result, indent=2))

    

