#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name:"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ all topics of a school """
    query = {"name", name}
    new = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new)
