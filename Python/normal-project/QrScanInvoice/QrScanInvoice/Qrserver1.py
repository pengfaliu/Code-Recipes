#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : liufapeng
# date : 2019-12-18

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    print("this is root")
    return "thanks"
    #return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args)
    return 'search'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return "login"
        #return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        return 'hello!\n'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)