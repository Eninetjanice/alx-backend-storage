#!/usr/bin/env python3
""" This script changes all topics of a school document based on the name. """


def update_topics(mongo_collection, name, topics):
    """ Change school topics in a doc based on the name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
