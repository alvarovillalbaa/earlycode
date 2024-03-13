# To avoid the bot going to sleep after 1H of no-use(when the replit web server gets closed)
from flask import Flask  # Flask used as a web server
from threading import Thread

app = FLask("")


@app.route("/")
def home():
    return "Hello. I am alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
