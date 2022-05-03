#!/usr/bin/env python3
""" Python function """


def schools_by_topic(mongo_collection, topic):
    """Python function that returns the list"""
    return mongo_collection.find({"topics": topic})
