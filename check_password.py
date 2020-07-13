import requests
import hashlib


def request_api_data(query_chars):
    url = 'https://api.pwnedpasswords.com/range/'  # + password to check
    res = requests.get(url + str(query_chars))
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, check the API')
    return res


def pwned_api_check(password):
    # Check password if it exist in API answer
    pass
