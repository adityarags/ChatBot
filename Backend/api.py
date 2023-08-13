from flask import current_app as app
from flask import request
from flask_restful import Resource, Api
from database import getAllChatIds, getMessages, addMessage, createChat
from flask import jsonify

api = Api(app)

class ChatList(Resource):
    def get(self):
        chat_ids = getAllChatIds()
        c = [str(chat_ids[i]["_id"]) for i in range(len(chat_ids))]
        result = {"chat_ids": c}
        return jsonify(result)

class Message(Resource):
    def get(self, cid):
        messages = getMessages(cid)
        result = {"messages": messages}
        return jsonify(result)
    
    def post(self, cid):
        response = request.json
        message = response["message"]
        addMessage(cid, message)
        return jsonify({"result": "message added"})
    

class NewChat(Resource):
    def post(self):
        print("hi")
        message = request.json["message"]
        print(message)
        x = createChat(message)
        return jsonify({"cid": str(x.inserted_id)})
    

api.add_resource(ChatList, "/chatids")
api.add_resource(Message, "/message/<cid>")
api.add_resource(NewChat, "/newchat")