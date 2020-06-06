from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.fitlogdb

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분


@app.route('/api/list', methods=['GET'])
def workouts_list():
    workouts = list(db.fitlogdb.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'workouts_list': workouts, 'msg': '성공'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
