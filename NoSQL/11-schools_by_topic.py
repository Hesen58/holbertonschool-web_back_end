#!/usr/bin/env python3
"""Something useful"""


def schools_by_topic(mongo_collection, topic):
    """Something more useful"""
    return mongo_collection.find({"topics": topic})