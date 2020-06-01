from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['GET'])
def listing():
    result = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': result})


@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    quant_receive = request.form['quant_give']
    phone_receive = request.form['phone_give']
    address_receive = request.form['address_give']

    order = {'name': name_receive, 'quant': quant_receive,
             'phone': phone_receive, 'address': address_receive}

    db.orders.insert_one(order)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
