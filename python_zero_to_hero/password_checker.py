import sys
import hashlib
import requests

"""
How to run program:

python3 password_checker.py cred_file.txt

cred_file.txt will have list of cre___d to check

"""



"""
request module works like a simple browser app, it taken url for which you want to search 
and 
get s you corresponding response with status code
"""

# 1. Enter passowrd, generate sh1 eq hash value- divide two parts - 1st 5 chars + tail
# 2. send 1st 5 char to api - get response
# 3. take response  & cross check


def get_response_from_api(query_char: str) -> str:
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char).strip()
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'{__name__} -> get_response_from_api -> response.status_code -> {response.status_code}')
    return response.text


def password_to_hash(password: str = 'hello') -> (str, str):
    print(password.encode('UTF-8'))
    """
    There is one constructor method named for each type of hash. All return a hash object with the same simple 
    interface. For example: use sha1() to create a SHA1 hash object. You can now feed this object with arbitrary 
    strings using the update() method. At any point 
    you can ask it for the digest of the concatenation of the strings fed to it so far 
    using the digest() or hexdigest() methods.
    """
    hashed_password = hashlib.sha1(password.encode('UTF-8')).hexdigest()
    # print(f'hashed_password : {hashed_password}')
    v_first_5_char, v_tail = hashed_password[:5], hashed_password[5:]
    return str(v_first_5_char).upper(), str(v_tail).upper()


def process_password(input_value: str) -> None:
    first_5_char, tail = password_to_hash(input_value)
    # print(f'first_5_char = {first_5_char}')
    response_text_val = get_response_from_api(first_5_char)
    # print(type(response_text_val))
    list_of_tuples = ((k.split(':')[0], k.split(':')[1]) for k in response_text_val.splitlines())
    for k, v in list_of_tuples:
        # print(f'tail - {tail} hash val - {k}')
        if tail == k:
            print('match found, this password was hacked earlier')
            break
    else:
        print("good to use this password")
    return


if __name__ == '__main__':
    print('starting program')
    list_file = sys.argv[1:]
    with open('src/' + list_file[0], 'r') as fpassfile:
        fpass_list = fpassfile.readlines()
        # print(fpass_list)
        for i in fpass_list:
            i = i.rstrip('\n')
            print(f'processing : {i}')
            process_password(i)
