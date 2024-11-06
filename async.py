#!/usr/bin/env python3

import asyncio
import aiohttp
import time
from aiohttp.web_exceptions import HTTPError

target_endpoint = 'https://httpbin.org/uuid'
requests_num = 10

start = time.time()


async def get_endpoint_data(session, target_endpoint):
    async with session.get(target_endpoint) as resp:
        try:
            resp.raise_for_status()
            endpoint_resp = await resp.json()
            print(endpoint_resp['uuid'])
        except HTTPError as err:
            raise SystemExit(err)


async def call():
    async with aiohttp.ClientSession() as session:
        tasks = [get_endpoint_data(session, target_endpoint) for _ in range(requests_num)]
        await asyncio.gather(*tasks)


asyncio.run(call())

end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {requests_num} API calls")