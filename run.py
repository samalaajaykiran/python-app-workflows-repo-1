# run.py

from app import app, socketio
import eventlet
eventlet.monkey_patch()  # This makes sure that Eventlet will handle all I/O operations asynchronously

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

