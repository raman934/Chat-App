from flask import Flask, jsonify, request

from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '93478'
socketio = SocketIO(app)

users = [
	{
		'id': 2,
		'name': 'Anne',
		'age': 23
	},
	{
		'id': 1,
		'name': 'Cathy',
		'age': 22
	},
	{
		'id': 3,
		'name': 'Bill',
		'age': 21
	},
]

@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handleMsg(data):
	socketio.emit('push', data, broadcast=True, include_self=False)

@app.route('/users')
def getUsers():
	return jsonify(users)

@app.route('/users/<id>')
def getUser(id):
	user = list(filter(lambda u: str(u['id'])==id, users))
	return jsonify(user)

# /users/sort?field=age
@app.route('/users/sort')
def getUsersSorted():
	field = request.args.get('field')
	usersSorted = sorted(users, key=lambda u: u[field])
	return jsonify(usersSorted)

if __name__=="__main__":
	socketio.run(app)






