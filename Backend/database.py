import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import ssl
load_dotenv()

URI = os.environ.get("MONGODB_URI")
DB = os.environ.get("MONGODB_DATABASE")
COLLECTION = os.environ.get("MONGODB_COLLECTION")
client = MongoClient(URI, ssl = True, ssl_cert_reqs = ssl.CERT_NONE)
db = client[DB]
collection = db[COLLECTION]



def createChat(message = ""):
    messages = [message] if message != "" else []
    x = collection.insert_one({"messages": messages})
    return x

def getAllChatIds():
    x = collection.find({}, {"messages": 0})
    return [_ for _ in x]

def addMessage(chat_id, message):
    collection.update_one(
    { "_id": ObjectId(chat_id) },
    { "$addToSet": { "messages": message }})

def getMessages(chat_id):
    query = {"_id": ObjectId(chat_id)}
    currChat = collection.find_one(query)
    messages = currChat["messages"]
    return messages