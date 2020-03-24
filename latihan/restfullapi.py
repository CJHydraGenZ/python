from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dbrestapi'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbrestapi'

mongo = PyMongo(app)


@app.route('/col', methods=['GET'])
def get_all_framework():
    mycol = mongo.db.restapi

    output = []

    for x in mycol.find():
        output.append({'nama': x['nama'], 'bahasa': x['bahasa']})

    return jsonify({'result': output})


@app.route('/col/<nama>', methods=['GET'])
def get_one_framework(nama):
    mycol = mongo.db.restapi
    x = mycol.find_one({'nama': nama})
    if x:
        output = {'nama': x['nama'], 'bahasa': x['bahasa']}
    else:
        output = "No result found"

    return jsonify({'result': output})


@app.route('/col', methods=['POST'])
def add_framework():
    mycol = mongo.db.restapi

    nama = request.json['nama']
    bahasa = request.json['bahasa']

    mycol_id = mycol.insert({'nama': nama, 'bahasa': bahasa})
    new_framework = mycol.find_one({'_id': mycol_id})
    output = {'nama': new_framework['nama'],
              'bahasa':  new_framework['bahasa']}

    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
