#!/usr/bin/env python3
'''
Task 0's module
'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    '''redis cache class
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, float, int]) -> str:
        '''returns a string
        '''
        uniqueId =str(uuid.uuid4())
        self._redis.set(uniqueId, data)
        return uniqueId

    def get(self, key: str, fn: Callable) -> Union[str, float, int, bytes]:
        '''get data from redis
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str):
        '''
        string return method
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
        int return method
        '''
        return self.get(key, lambda x: int(x))
