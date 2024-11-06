#!/usr/bin/env python3

import requests
import time


target_endpoint = 'https://httpbin.org/uuid'
requests_num = 10

start = time.time()

for _ in range(requests_num):
    try:
        r = requests.get(target_endpoint)
        r.raise_for_status()
        print(r.json()['uuid'])
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {requests_num} API calls")