"""
REdis Cache exercise file
"""
# !/usr/bin/env python3


import redis
import uuid
from typing import Union, ByteString, Any, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts how many times function is called"""
    @wraps(method)
    def wrapper_count_calls(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_count_calls


def call_history(method: Callable) -> Callable:
    """saves inputs and output of all function calls"""
    @wraps(method)
    def wrapper_call_history(self, *args):
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        keyReturned = method(self, *args)
        self._redis.rpush(method.__qualname__ + ":outputs", keyReturned)
        return keyReturned
    return wrapper_call_history


class Cache:
    """
    Defines a Redis cache
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """get value from redis"""
        r = self._redis.get(key)
        if fn is not None:
            r = fn(r)
        return r

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """save data to redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, name) -> str:
        """convert byte string to string before calling get from redis"""
        return self.get(name, lambda b: d.decode("utf-8"))

    def get_int(self, i) -> int:
        """convert bytes to int before calling get from redis"""
        return self.get(i, lambda b: int.from_bytes(b))


def replay(method: Callable) -> None:
    """function counts method calls for passed method"""
    listInputs = redis.Redis().lrange(method.__qualname__ + ":inputs", 0, -1)
    listOutputs = redis.Redis().lrange(method.__qualname__ + ":outputs", 0, -1)
    zipped = zip(listInputs, listOutputs)
    calls = len(listInputs)
    print(f"{method.__qualname__} was called {calls} times:")
    for inputs, outputs in zipped:
        print(f"{method.__qualname__}(*{inputs.decode('utf-8')}) \
        -> {outputs.decode('utf-8')}")
