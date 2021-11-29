import pymongo

class MongoStore:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['tiktok']
    
    def set_collection(self, collection):
        self.collection = self.db[collection]
    
    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)
