from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["employee_db"]

collection = db["employees"]


def save_employee_mongo(data):

    collection.insert_one(data)