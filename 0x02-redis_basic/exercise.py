#!/usr/bin/env python3

"""
Redis module which defines a Cache class that stores, reads, writes to,
increments and retrieves data in Redis.
"""

from functools import wraps
from typing import Union, Optional, Callable
import redis
import uuid

UnionTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ Count num of times methods of Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Returns a Callable """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Add input params to a list in redis, & store its output into another list.
    """
        key = method.__qualname__
    inputs_key = "".join([key, ":inputs"])
    outputs_key = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapp, returns a Callable """
        self._redis.rpush(inputs_key, str(args))
        output_data = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output_data))
        return output_data

    return wrapper


class Cache:
    """ Defines Cache redis class """

    def __init__(self):
        """ Redis model Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionTypes) -> str:
        """
        Generate a random key (e.g. using uuid),
         store the input data in Redis using the
          random key and return the key.
        """
        key = str(uuid4())
        self._redis.set({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionTypes:
        """
        Reads from Redis and converts the data back
        to the desired format
        eval:
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data
        """
        value = self._redis.get(key)
        if value is None:
            return value
        if fn is not None:
            return fn(value)
        return value

    def get_int(self, key: bytes) -> int:
        """Retrieves val stored in Redis & returns it in int format"""
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> UnionTypes:
        """Retrieves val stored in Redis & returns it in str format"""
        return str(self.get(key, lambda x: x.decode('utf-8')))
