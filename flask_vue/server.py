from flask import Flask, jsonify, render_template
from flask_cors import CORS
#from livereload import Server

#from backend.db import DbManager
#from backend.db.entitys.User import *


app = Flask(__name__, 
			static_folder='./frontend/dist/static',
			template_folder='./frontend/dist')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1.0/mensaje')
def mensaje():
	#p1 = User[1]
	msg = 'Nuevo mensaje con autoreload: '#+str(p1.mail)
	return jsonify(msg)

#@db_session
#def createUser():
#	p1 = User(name='John', mail='mail@mail.com')
	# commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool


@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def render_vue(path):
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
	#DbManager.createDB(True)
	#createUser()
	#server = Server(app.wsgi_app)
	#server.serve(open_url_delay=5, port=5000, host='localhost')