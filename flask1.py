

from flask import Flask,render_template,request
import playbot

app = Flask(__name__)

@app.route('/')
def welcome():
    x=playbot.run("hello")
    return render_template('page.html',data=x)
if __name__ == '__main__':
    app.run(debug=True)

