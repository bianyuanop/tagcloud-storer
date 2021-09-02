from flask import Flask, json, request 
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def store():
	data = request.form['imageUrl']	

	with sqlite3.connect('./images.db') as db:
		cur = db.cursor()
		cur.execute(
			'INSERT INTO img(dataurl) VALUES (?)',
			(data,)
		)
		db.commit()
		print('inserted data')
	return json.dumps({
		'msg': 'sucessful'
	})

@app.route('/get', methods=['GET'])
def get_all():
	with sqlite3.connect('./images.db') as db:
		cur = db.cursor()
		records = cur.execute(
			'SELECT id from img'
		).fetchall()

		ids = [id[0] for id in records]
		print(ids)

		return json.dumps({
			'idx': json.dumps(ids)
		})

@app.route('/get/<id>', methods=['GET'])
def get(id):
	with sqlite3.connect('./images.db') as db:
		cur = db.cursor()
		record = cur.execute(
			'SELECT dataurl FROM img WHERE id=?',
			(id,)
		).fetchone()

		if record != None:
			img = record[0]
		else:
			img = ""

		return json.dumps({
			'datauri': img
		})

if __name__ == '__main__':
	app.run(port=4000, debug=True)
