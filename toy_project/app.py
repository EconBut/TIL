from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.n5dbos3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def index1():
    return render_template('index.html')

@app.route('/page2')
def index2():
    return render_template('index2.html')


@app.route('/page3')
def index3():
    return render_template('index3.html')


@app.route('/page4')
def index4():
    return render_template('index4.html')


@app.route("/page2/cook", methods=["POST"])
def cook_post():
    cook_name = request.form["cookName_give"]
    image_url = request.form["imageUrl_give"]
    prep1 = request.form["prep1_give"]
    prep2 = request.form["prep2_give"]
    prep3 = request.form["prep3_give"]
    prep4 = request.form["prep4_give"]




    doc = {
        'name': cook_name,
        'image': image_url,
        'prep1': prep1,
        'prep2': prep2,
        'prep3': prep3,
        'prep4': prep4,

    }
    db.cook.insert_one(doc)

    return jsonify({'msg': '등록 완료'})


@app.route("/page4/complete", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.cook.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '구매 완료'})


@app.route("/page4/cancel", methods=["POST"])
def bucket_cancel():
    num_receive = request.form['num_give']
    db.cook.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    return jsonify({'msg': '구매 취소'})


@app.route("/page3/cook", methods=["GET"])
def bucket_get():
    cook_list = list(db.cook.find({}, {'_id': False}))
    return jsonify({'cooks': cook_list})

@app.route("/page4/cook", methods=["GET"])
def cook_get():
    cook_list = list(db.cook.find({}, {'_id': False}))
    return jsonify({'cooks': cook_list})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
