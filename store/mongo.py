import pymongo

from config.helper import config

class MongoStore:
    def __init__(self):
        self.client = pymongo.MongoClient(config()['mongo']['uri'])
        self.db = self.client[config()['mongo']['dbname']]
    
    def set_collection(self, collection):
        self.collection = self.db[collection]
    
    def replace_one(self, condition, data, upsert=True):
        return self.collection.replace_one(condition, data, upsert=upsert)
    
    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)

    def exists(self, condition):
        return self.collection.count_documents(condition, limit = 1) != 0
