import json

import jsonpickle
from flask import Flask
from flask import render_template
from flask import request
from json  import decoder
import jsonpickle

app = Flask(__name__)


class Words_stat:
    text = ""
    words = []
    count = 0

    def __init__(self, text):
        self.text = text
        self.words = self.text.split(' ')
        self.count = len(self.words)

    def default(self, o):
        return o.__dict__

    def  json(self):
        return jsonpickle.encode(self)

##=== = = = = Главная программа  === == =
@app.route("/")
def index():
    return "<html> <head> </head> <body lang=ru> <p> Привет!  Введите строку <form name=words method=post action='/words'> <input name='words' type=text></input> <input type=submit text='Ok'> </form></p>  </body> </html>"

@app.route("/words", methods = ['POST'])
def index2():
    words = request.form['words']
    data = []

    try:
        dec = json.loads( words)
        print ("wait data = ", dec ["data"] )
        obj = Words_stat(dec["data"])

        print("obj = ", obj)
        data= obj.json()

    except:

        obj = Words_stat(words)
        print("obj = ", obj)

        data = obj.json()

    return data


if __name__ == '__main__':
   app.run(debug = True)


