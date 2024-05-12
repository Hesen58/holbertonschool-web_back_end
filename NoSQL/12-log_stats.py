#!usr/bin/env python3
"""Something useful"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.logs
    count = db.nginx.count_documents({})
    print(f"{count} logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        methodcount = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {methodcount}")
    statusGET = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{statusGET} status check")
