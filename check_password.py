import requests
import hashlib
import sys


def request_api_data(query_chars):
    url = 'https://api.pwnedpasswords.com/range/'  # + password to check
    res = requests.get(url + str(query_chars))
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, check the API')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exist in API answer

    # hashing our password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # we need the first 5 characters from the received hash, to work with API
    first5_chars, tail = sha1password[:5], sha1password[5:]

    responce = request_api_data(first5_chars)
    return get_password_leaks_count(responce, tail)


def main(passwords):
    for password in passwords:
        result = pwned_api_check(password)
        if result != 0:
            print(
                f'{password} was found {result} times... You should change your password!')
        else:
            print(f'{password} was NOT found! You can use it!)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
