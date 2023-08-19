#!/usr/bin/env python3
'''
Task 0's module
'''
import redis
import uuid
import json
from typing import Union


class Cache:
    '''redis cache class
    '''

    def __init__(self):
        self._redis = redis.Redis(charset='utf-8', decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        '''returns a string
        '''
        uniqueId =str(uuid.uuid4())
        self._redis.set(uniqueId, data)
        return uniqueId
