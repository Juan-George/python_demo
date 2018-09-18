# coding=utf-8

from flask import Flask, make_response, jsonify, redirect,url_for
import json

app = Flask(__name__)


class Myconfig(object):
    DEBUG = True

app.config.from_object(Myconfig)


@app.route("/index")
def index():
            # 返回的内容     返回的状态码    返回的headers
    return 'indexxxxxxxxx', 200 , {"name":"dog","age":18}


@app.route("/")
def index1():
    res = make_response('创建 3 response对象')
    res.headers["name"]= 'pig'
    res.status = u"403 not"
    return res


# 返回json数据格式
@app.route("/json")
def json_data():
    dict_a = {"name":"dog", "age":19}
    # return json.dumps(dict_a)
    return jsonify(dict_a)

# 重定向
@app.route("/red")
def redirect_url():
    # return redirect("/json")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='192.168.146.130', port=5000)
