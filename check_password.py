import requests
import hashlib


def request_api_data(query_chars):
    url = 'https://api.pwnedpasswords.com/range/'  # + password to check
    res = requests.get(url + str(query_chars))
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, check the API')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)


def pwned_api_check(password):
    # Check password if it exist in API answer

    # hashing our password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5], sha1password[5:]

    responce = request_api_data(first5_chars)
    return get_password_leaks_count(responce, tail)


pwned_api_check('vivi')
