# coding=utf-8

from flask import Flask, make_response, session, request, jsonify


app = Flask(__name__)


class Myconfig(object):
    DEBUG = True

app.config.from_object(Myconfig)


@app.route("/index")
def index():
    res = make_response("this is indexes")
    res.set_cookie("name","piggg",max_age=3600)
    return res

@app.route("/getcookie")
def get_cookies():
    name = request.cookies.get("name")
    csrf = request.cookies.get("csrftoken")
    dict_a = {"csrftoken":csrf, "name":name}
    return jsonify(dict_a)


@app.route("/delcookie")
def del_cookie():
    res = make_response("success")
    res.delete_cookie("name")
    return res

app.config["SECRET_KEY"] = "akdjvoisanvs=2=87"

@app.route("/setsession")
def set_session():
    session["school"] = "itcast"
    return "success session"

@app.route("/getsession")
def get_session():
    school = session.get("school")
    return "school : %s" % school



if __name__ == '__main__':
    app.run(host='192.168.146.130', port=5000)
