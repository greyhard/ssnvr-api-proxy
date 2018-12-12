from flask import Flask, jsonify, request
import requests
import pickle
import codecs
from base64 import b64encode, b64decode
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    r = requests.post("http://seasonvar.ru/?mod=login",
                      data={'login': request.form['login'], 'password': request.form['password']})

    json = {
        'status': 'ok',
        'token': codecs.encode(pickle.dumps(r.cookies), "base64").decode(),
    }

    return jsonify(json)


@app.route('/pause/', methods=['POST', 'GET'])
def pause():
    r = requests.get("http://seasonvar.ru/?mod=pause",
                     cookies=pickle.loads(codecs.decode(request.form['token'].encode(), "base64")))
    soup = BeautifulSoup(r.text, 'html.parser')
    li = soup.find_all('li', {'class': ['headmenu-title']})
    print(li)
    return soup.title.string


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
