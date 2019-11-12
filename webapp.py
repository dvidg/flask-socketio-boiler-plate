from flask import Flask, redirect, url_for, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def homepage():
    message = "hello world"
    return render_template('index.html', message=message)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

### Receiving WebSocket Messages ###
@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
		socketio.run(app, host = "0.0.0.0", port = 3000, debug = True)	
