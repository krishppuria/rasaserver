

from flask import Flask,render_template,request
from playbot import run

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        name=request.args.post('user')
        x=run(name)
        return render_template('page.html',data=x)
    return render_template('loggin.html')
if __name__ == '__main__':
    app.run(debug=True)

