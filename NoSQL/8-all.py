#!/usr/bin/env python3
"""Something useful"""


def list_all(mongo_collection):
    return mongo_collection.find()