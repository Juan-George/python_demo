#coding=utf-8

from flask import Flask,url_for,current_app
from werkzeug.routing import BaseConverter


app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates',)


# 设置配置文件信息
# app.config.from_pyfile('Config.cfg')

# 定义一个配置类
class MyConfig(object):
    DEBUG=True
    ITCAST='python'

app.config.from_object(MyConfig)



@app.route('/hello')
def hello2():
    # print 'aa'
    return 'hello world 2'

@app.route('/hello')
def hello():
    return 'hello world 1'

@app.route('/aaa')
@app.route('/staticfile')
def static_file():
    return 'staticfile'


@app.route('/index',methods=['post','get'])
def index():
    return 'index'

# 使用url_for进行反向解析
@app.route('/redirect')
def redirect_url():

    return "<a href='%s'>hello</a>" % url_for('hello')

if __name__ == '__main__':
    # print app.url_map
    print (current_app.config.get('ITCAST'))
    app.run(host='0.0.0.0',port=5002)