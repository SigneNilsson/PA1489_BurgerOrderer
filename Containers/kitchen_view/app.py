"""Kitchen View"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def frontpage():
    print('Loading front page', flush = True)
    return("Welcome!")

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)