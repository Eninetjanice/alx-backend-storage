#!/usr/bin/env python3

"""
This module defines a Cache class that stores data in Redis.
"""

import uuid
from typing import Union
import redis


class Cache:
    """
    A class that provides caching functionality using Redis.

    Methods:
    --------
    store(data: Union[str, bytes, int, float]) -> str
        Stores the provided data in Redis and returns the key used to store it.
    get(key: str, fn: Callable = None) -> Union[str, bytes, int, float]
        Retrieves value stored in Redis with the provided key, and applies the
        specified conversion func (if provided) to the val before returning it.

    get_str(key: str) -> str
        Convenience method; retrieves value stored in Redis with provided
        key and returns it as a string.

    get_int(key: str) -> int
        Convenience method; retrieves value stored in Redis with provided
        key and returns it as an integer.
    """

    def __init__(self) -> None:
        """
        Initializes Cache instance by creating Redis client & flushing the db.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis and returns the key used to store it.

        Parameters:
        -----------
        data : Union[str, bytes, int, float]
            Data to can be a string, bytes, integer or float.

        Returns:
        --------
        str
            The key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        """
        Retrieves value stored in Redis with provided key, & applies the
        specified conversion func (if provided) to val before returning it.

        Parameters:
        -----------
        key : str
            The key of the data to retrieve from Redis.
        fn : Callable, optional
            A callable that takes a single argument (data retrieved from Redis)
            returns a converted value. If not provided, the raw value retrieved
            from Redis will be returned.

        Returns:
        --------
        Union[str, bytes, int, float]
            Value stored in Redis with provided key, after being optionally
            converted by the specified function.
        """
        value = self._redis.get(key)
        if value is None:
            return value
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Convenience method that retrieves the value stored in Redis with
        provided key and returns it as a string.

        Parameters:
        -----------
        key : str
            The key of the data to retrieve from Redis.

        Returns:
        --------
        str
            The value stored in Redis with the provided key, as a string.
        """
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """
        Convenience method that retrieves the value stored in Redis with
        provided key and returns it as an integer.

        Parameters:
        -----------
        key : str
            The key of the data to retrieve from Redis.

        Returns:
        -------
        int
        """
        return self.get(key, fn=int)
