from flask import current_app as app
from flask import render_template, request, redirect, url_for
import requests

@app.route("/", methods = ["GET", "POST"])
def home():
    res = requests.get("http://127.0.0.1:5000/chatids")
    chat_ids = res.json()["chat_ids"]
    if request.method == "POST":
        req = {"message": request.form["message"]}
        cid = requests.post("http://127.0.0.1:5000/newchat", json = req, headers = {"Content-type": "application/json"})
        cid = cid.json()
        cid = cid["cid"]
        return redirect(url_for("chat", cid = cid))
    return render_template('index.html', page = 'home', chats = chat_ids)


@app.route("/chat/<cid>", methods = ["GET", "POST"])
def chat(cid):
    res = requests.get("http://127.0.0.1:5000/chatids")
    chat_ids = res.json()["chat_ids"]
    if request.method == "POST":
        req = {"message": request.form["message"]}
        requests.post(f"http://127.0.0.1:5000/message/{cid}", json = req, headers = {"Content-type": "application/json"})
    return render_template("index.html", page = 'chat', chats = chat_ids)