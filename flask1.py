

from flask import Flask,render_template,request
from playbot import run

app = Flask(__name__)

@app.route('/')
def welcome():
    name="hello"
    x=run(name)
    return render_template('page.html',data=x)
#if __name__ == '__main__':
    #app.run(debug=True)

