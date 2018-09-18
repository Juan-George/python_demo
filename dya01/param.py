#coding=utf-8

from flask import Flask,url_for,current_app,request

from werkzeug.routing import BaseConverter

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

class Myconfig(object):
    DEBUG=True
    ITCAST = 'heima'

app.config.from_object(Myconfig)

class ReConverter(BaseConverter):

    def __init__(self,url_map,*args):
        super(ReConverter,self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

app.url_map.converters['re'] = ReConverter

# @app.route('/<name>')
# def view1(name):
#
#     return "name :%s" % name
#     # return name

@app.route('/<int:id1>/<int:id>')
def view2(id,id1):
    return "id:%s %s" % (id,id1)

@app.route("/my/<re('\d{3}'):id>")
def view3(id):
    return "id: %s" % id

# 反响解析
@app.route('/<re("\d+"):id>')
def view4(id):
    print type(id)
    return "<a href=%s>hello=========</a>" % url_for('view3',id=id)


if __name__ == '__main__':
    # print current_app.config.get('ITCAST')
    print u'你好'
    app.run(host='0.0.0.0',port=5002)




