import json

sample_data_json = """{
    "users": [{
        "userId": 1,
        "firstName": "Krish",
        "lastName": "Lee",
        "phoneNumber": "123456",
        "emailAddress": "krish.lee@learningcontainer.com"
    },
        {
            "userId": 2,
            "firstName": "racks",
            "lastName": "jacson",
            "phoneNumber": "123456",
            "emailAddress": "racks.jacson@learningcontainer.com"
        },
        {
            "userId": 3,
            "firstName": "denial",
            "lastName": "roast",
            "phoneNumber": "33333333",
            "emailAddress": "denial.roast@learningcontainer.com"
        },
        {
            "userId": 4,
            "firstName": "devid",
            "lastName": "neo",
            "phoneNumber": "222222222",
            "emailAddress": "devid.neo@learningcontainer.com"
        },
        {
            "userId": 5,
            "firstName": "jone",
            "lastName": "mac",
            "phoneNumber": "111111111",
            "emailAddress": "jone.mac@learningcontainer.com"
        }]
}"""

# Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4.

data_loaded = json.loads(sample_data_json)
print("json exercise")
print(type(data_loaded))
print(len(data_loaded["users"]))

for i in range(len(data_loaded["users"])):
    print(data_loaded["users"][i])

ldict = {}
for i in range(len(data_loaded["users"])):
    ldict.update({data_loaded["users"][i]["firstName"]: int(data_loaded["users"][i]["phoneNumber"])})

print(ldict)
final_json_str = {"final_list": ldict}

print(type(final_json_str))

print(json.dumps(final_json_str, sort_keys=True, indent=4))


# 8. Write a Python program to check whether a JSON string contains complex object or not.


# 6. Write a Python program to create a new JSON file from an existing JSON file


