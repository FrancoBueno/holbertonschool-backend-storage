#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name:"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ all topics of a school """
    mongo_collection.update_Many(
        {'name': name},
        {'$set': {"topics": topics}}
    )
