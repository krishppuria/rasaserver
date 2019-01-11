from flask import Flask,render_template,request,jsonify
from playbot import run
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('loggin.html')
@app.route('/user')
def data():
    name=request.args.get('user')
    x=run(name)
    return jsonify({"value":x})
if __name__ == '__main__':
    app.run(debug=True)

