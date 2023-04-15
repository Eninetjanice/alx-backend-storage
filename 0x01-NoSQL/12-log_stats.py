#!/usr/bin/env python3
'''This script provides some stats about Nginx logs stored in MongoDB'''

from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def nginxlog_stats(mongo_collection, option=None)::
    """ Provides Nginx log statistics """
    data = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(data)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        nginxlog_stats(nginx_collection, method)
    check_status = mongo_collection.count_documents({"path": "/status"})
    print(f"{check_status} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginxlog_stats(nginx_collection)
