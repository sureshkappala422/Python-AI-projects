from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_chatbot"]

employee_collection = db["employees"]
chat_collection = db["chat_logs"]

def save_employee(emp):

    employee_collection.insert_one(emp)


def save_chat(user, bot):

    chat_collection.insert_one({
        "user_message" : user,
        "bot_response" : bot

    })    
