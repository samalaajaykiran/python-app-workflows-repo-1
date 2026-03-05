# app/routes.py

from app import app, socketio
from flask import render_template
from flask_socketio import emit

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    emit('response', {'data': msg}, broadcast=True)