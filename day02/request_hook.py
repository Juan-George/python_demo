# coding=utf-8

from flask import Flask

app = Flask(__name__)


class Myconfig(object):
    DEBUG = True

app.config.from_object(Myconfig)

@app.before_first_request
def view1():
    print "before first"

@app.before_request
def view2():
    print "before request"

@app.after_request
def view1(response):
    print "after request dont show when exception"
    return response

@app.teardown_request
def view1(response):
    print "after  no matter exception or not"
    return response


@app.route("/index")
def index():

    print "*"*30
    return "index"





if __name__ == '__main__':
    app.run(host='192.168.146.130', port=5000)
