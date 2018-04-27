from flask import Flask, render_template
from flask_socketio import SocketIO
import redis

app = Flask(__name__)
socketio = SocketIO(app)

##########
# ROUTES #
##########

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/simulation')
def simulation():
    return render_template('simulation.html')

######################
# SocketIO FUNCTIONS #
######################
@socketio.on('connection')
def handle_connection(data):
    print(data)

if __name__ == '__main__':
    ###############
    # GLOBAL VARS #
    ###############
    global view
    global redis
    redis = redis.StrictRedis(host='localhost', port=6379)
    socketio.run(app, debug=True)
