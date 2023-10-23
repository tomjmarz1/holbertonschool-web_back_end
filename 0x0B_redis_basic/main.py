"""
Main file
"""
#!/usr/bin/env python3

import redis

Cache =__import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

# #ex0
# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

# #ex1
# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     # assert cache.get(key, fn=fn) == value

# #ex2
# cache.store(b"first")
# print(cache.store.__qualname__)

# print(cache.get("Cache.store"))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))


#ex3
s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

replay(cache.store)