from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbtimeattack

from datetime import datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    # idx_receive = request.form['idx_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    reg_date_receive = mytime

    doc = {
        # 'idx': idx_receive,
        'title': title_receive,
        'content': content_receive,
        'reg_date': reg_date_receive,

    }
    db.articles.insert_one(doc)
    return {"result": "success", "msg": "저장 완료!"}


@app.route('/show', methods=['GET'])
def get_post():
    articles = list(db.articles.find({}, {'_id': False}))
    articles.reverse()
    return jsonify({'all_articles': articles})


@app.route('/del', methods=['DELETE'])
def delete_post():
    idx_receive = request.form['idx_give']
    # db.articles.delete_one({'idx': idx_receive})
    return {"result": "success", "msg": "삭제 완료!"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
