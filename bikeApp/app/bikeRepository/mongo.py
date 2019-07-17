import os
from pymongo import MongoClient

COLLECTION_NAME = 'bikeApp'


class MongoBike(object):  # aka MongoRepository class
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).bikeApp

    def find_all(self, selector):
        return self.db.bikeApp.find(selector)
  
    def find(self, selector):
        return self.db.bikeApp.find_one(selector)
  
    def create(self, bikeInfo):
        return self.db.bikeApp.insert_one(bikeInfo)

    def update(self, selector, bikeInfo):
        return self.db.bikeApp.replace_one(selector, bikeInfo).modified_count
  
    def delete(self, selector):
        return self.db.bikeApp.delete_one(selector).deleted_count