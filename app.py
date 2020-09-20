from flask import Flask, request
from telegram_bot import handle_bot_msg
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)


@app.route("/")
def index():
    return "up"


@app.route("/hook", methods=['POST'])
def bot_req():
    return handle_bot_msg(request)
