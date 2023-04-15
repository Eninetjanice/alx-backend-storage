#!/usr/bin/env python3
'''
This script provides some stats about Nginx logs stored in MongoDB
And adds the top 10 of the most present IPs in nginx db logs collection
'''

from pymongo import MongoClient


def nginxlog_stats:
    """ Provides Nginx log statistics """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    total_logs = nginx.count_documents({})
    get = nginx.count_documents({'method' : 'GET'})
    post = nginx.count_documents({'method' : 'POST'})
    put = nginx.count_documents({'method' : 'PUT'})
    patch = nginx.count_documents({'method' : 'PATCH'})
    delete = nginx.count_documents({'method' : 'DELETE'})

    path = nginx.count_documents({'$and': [{'method' : 'GET'}, {"path":
                                                                "/status"}]})

    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")
    print("IPs:")
    sorted_ips = nginx.aggregate(
        [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
         {"$sort": {"count": -1}}])
    i = 0
    for s in sorted_ips:
        if i == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        i += 1


if __name__ == "__main__":
    nginxlog_stats()
