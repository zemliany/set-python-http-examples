# #!/usr/bin/env python3

import requests
import time
from concurrent.futures import ThreadPoolExecutor


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


with ThreadPoolExecutor(max_workers=50) as executor:
    with requests.Session() as session:
        executor.map(get_endpoint_data, [session] * requests_num, [target_endpoint] * requests_num)
        executor.shutdown(wait=True)

end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {requests_num} API calls")
