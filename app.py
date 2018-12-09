from flask import Flask, jsonify, request
import requests
import pickle
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/qwe/', methods=['POST', 'GET'])
def qwe_world():
    r = requests.post("http://seasonvar.ru/?mod=login",
                      data={'login': request.form['login'], 'password': request.form['password']})

    with open('cookies.txt', 'wb') as f:
        pickle.dump(r.cookies, f)

    # soup = BeautifulSoup(r.text, 'html.parser')

    # li = soup.find_all('li', {'class': ['headmenu-title']})
    # print(li)
    return "ok"


@app.route('/qwe2/')
def qwe2_world():
    with open('cookies.txt', 'rb') as f:
        r = requests.get("http://seasonvar.ru/?mod=pause", cookies=pickle.load(f))
        soup = BeautifulSoup(r.text, 'html.parser')
        li = soup.find_all('li', {'class': ['headmenu-title']})
        print(li)
        return soup.title.string

    return "Cookie Error"


@app.route('/qwe3/')
def qwe3_world():
    with open('cookies.txt', 'rb') as f:
        r = requests.get("http://seasonvar.ru/serial-2447--Skazka_o_hvoste_fei-1-sezon.html", cookies=pickle.load(f))
        return r.text


@app.route('/asd/')
def asd_world():
    d = {'a': 'b'}
    return jsonify(d)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
