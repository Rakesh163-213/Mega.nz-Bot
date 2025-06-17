# Copyright (c) 2021 - Present Itz-fork
# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/Mega.nz-Bot
# Description: __main__.py
from flask import Flask
from threading import Thread  # ✅ Add this line

# == Flask App ==
app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Flask is running! Bot should be running too.'

def run_flask():
    app.run(host='0.0.0.0', port=8000)

# Start Flask in a separate thread
flask_thread = Thread(target=run_flask)
from pyrogram import idle

from . import CypherClient

# Run the bot
if __name__ == "__main__":
    # Custom pyrogram client
    print("> Starting Client")
    CypherClient.start()
    flask_thread.start()
    print("--------------------")
    idle()
