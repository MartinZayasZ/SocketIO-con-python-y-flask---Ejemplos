from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print(f'Conexión éxitosa')
    # if not self.authenticate(request.args):
    #     raise ConnectionRefusedError('unauthorized!')

@socketio.on('sendMessage')
def sendMessage(data):
    print(f'Mensaje: {data}')
    socketio.emit('messages', data)


if __name__ == '__main__':
    socketio.run(app)