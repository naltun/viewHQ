from flask import Flask, render_template
from flask_socketio import SocketIO
import redis

################################################################
#                       LOG SYMBOLS                            #
# [*] a standard message between the client and the server     #
# [!] indicates an action has taken place from the client-side #
################################################################

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
def handle_connection(connMsg):
    # set the view by grabbing the last word in the returned message
    view = connMsg.split() # first we need to turn the string into a list
    view = view[-1] # now we grab the last value
    redis.set('currentView', view)
    print(connMsg)

@socketio.on('latest_view')
def handle_view(view):
    # store the latest view for checking
    redis.set('requestedView', view)
    print('[!] The latest view is ' + view)

if __name__ == '__main__':
    ###############
    # GLOBAL VARS #
    ###############
    global redis
    redis = redis.StrictRedis(host='localhost', port=6379)
    socketio.run(app, debug=True)
