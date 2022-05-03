#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name:"""


def update_topics(mongo_collection, name, topics):
    """ all topics of a school """
    mongo_collection.updateMany(
        {'name': name},
        {'$set': {"topics": topics}}
    )
