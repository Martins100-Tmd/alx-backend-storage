#!/usr/bin/env python3
'''
Task 0's module
'''
import redis
import uuid
import json
from typings import Union


class Cache:
    '''redis cache class
    '''

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        '''returns a string
        '''
        uniqueId = uuid()
        self._redis.set(uniqueId, json.dumps(data))
        return uniqueId
