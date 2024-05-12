#!/usr/bin/env python3
"""Something useful"""


def update_topics(mongo_collection, name, topics):
    """Something more useful"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})