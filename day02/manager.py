# coding=utf-8

from flask import Flask
from flask_script import Manager


app = Flask(__name__)

manager = Manager(app)


class Myconfig(object):
    DEBUG = True

app.config.from_object(Myconfig)


@app.route("/index")
def index():
            # 返回的内容     返回的状态码    返回的headers
    return 'indexxxxxxxxx', 200


if __name__ == '__main__':
    manager.run()
