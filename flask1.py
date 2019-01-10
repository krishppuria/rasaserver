

from flask import Flask,render_template,request
import playbot

app = Flask(__name__)

@app.route('/')
def welcome():
    name="hello"
    x=name
    return render_template('page.html',data=x)
#if __name__ == '__main__':
    #app.run(debug=True)

