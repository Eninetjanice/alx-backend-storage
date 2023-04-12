#!/usr/bin/env python3
''' Lists all documents in a collection '''

from pymongo.collection import Collection


def list_all(mongo_collection: Collection):
    """ Lists all documents in a collection
    Arg: mongo_collection; the pymongo collection object
    Return value: Empty list if no doc in the collection """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    else:
        return [doc for doc in documents]
