#!/usr/bin/env python3
"""Something useful"""


def list_all(mongo_collection):
    if not mongo_collection:
        return []
    else:
        return mongo_collection.find()