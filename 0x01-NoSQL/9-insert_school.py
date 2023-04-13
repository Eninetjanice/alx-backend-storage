#!/usr/bin/env python3
''' Function that inserts a new document in a collection based on kwargs '''

from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """Insert a document and return the new _id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id