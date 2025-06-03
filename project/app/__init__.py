from flask import Flask
from dotenv import load_dotenv
import os

from .extensions import mongo
from .webhook.routes import webhook

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb+srv://soham:6NxAnIdVhyRM8l44@webhookcluster.yktjejr.mongodb.net/webhooks?retryWrites=true&w=majority"

    mongo.init_app(app)

    print("MONGO INIT:", mongo.db)

    app.register_blueprint(webhook)

    return app
