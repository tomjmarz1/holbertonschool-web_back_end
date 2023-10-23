#!/usr/bin/env python3
"""
web request
"""
import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()

def count_requests(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_count_requests(self, *args):
        r.expire(func.__qualname__ + ":{args}", 10)
        return func()
    return wrapper_count_requests

@count_requests
def get_page(url: str) -> str:
    response = requests.get(url)
    count = r.lrange("count:{url}",0, -1)
    return str(len(count))

get_page("http://slowwly.robertomurray.co.uk")