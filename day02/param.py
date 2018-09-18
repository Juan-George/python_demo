# coding=utf-8

from flask import Flask, request, abort

app = Flask(__name__)


class Myconfig(object):
    DEBUG = True

app.config.from_object(Myconfig)


@app.route("/getparam")
def get_param():
    name = request.args.get('name')
    return "get param %s" % name


@app.route("/upload", methods=["POST",'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files["meizi"]
        f.save("pic.txt")
    return 'success'


# 自定义异常处理
@app.errorhandler(404)
def error_handler(error):
    return "您寻找的页面被狗吃了 %s" % error


@app.route("/")
def index():
    abort(403)
    return "index"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
