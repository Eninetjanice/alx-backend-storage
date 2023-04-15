#!/usr/bin/env python3
''' Lists all documents in a collection '''


def list_all(mongo_collection):
    """ Lists all documents in a collection
    Arg: mongo_collection; pymongo collection object
    Return value: Empty list if no doc in collection """
    search_doc = mongo_collection.find()
    if search_doc.count() == 0:
        return []
    else:
        return [doc for doc search_doc]
