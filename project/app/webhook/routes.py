from flask import Blueprint, request, jsonify, render_template
from app.extensions import mongo
from datetime import datetime

webhook = Blueprint('Webhook', __name__)

@webhook.route('/')
def index():
    return render_template('index.html')

@webhook.route('/events')
def get_events():
    print("Mongo DB:", mongo.db)  # Should not be None
    events = list(mongo.db.events.find({}, {'_id': 0}))
    return jsonify(events)
