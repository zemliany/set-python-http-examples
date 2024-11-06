#!/usr/bin/env python3

import requests
import time
from multiprocess import Pool

target_endpoint = 'https://httpbin.org/uuid'
requests_num = 10

start = time.time()


def get_endpoint_data(session, target_endpoint):
    with session.get(target_endpoint) as resp:
        try:
            resp.raise_for_status()
            print(resp.json()['uuid'])
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)


with Pool() as pool:
    with requests.Session() as session:
        results = pool.starmap(get_endpoint_data, [(session, target_endpoint) for _ in range(requests_num)])

end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {requests_num} API calls")