from flask import Flask,jsonify
import os

app = Flask(__name__)


#declarator for route to end point
@app.route('/')
def hello():
    return jsonify(hello ='world!')

#entry point
if __name__ == '__main__':
    app.run(debug=True)
