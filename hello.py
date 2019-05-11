from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)



@app.route('/')
def toss():
    coin = randint(0,2)
    return render_template('hello.html', spin=spin)


app.run(debug=True)
