import pymongo
"""Something useful"""


def list_all(mongo_collection):
    if not mongo_collection:
        return []
    else:
        