#!/usr/bin/env python3
'''Task 11's module
'''


def school_by_topic(mongo_collection, topic):
    '''
    returns the list of school having a specific topic:
    '''
    result = mongo_collection.find(
            {'topics': topic}
            )
    return result
