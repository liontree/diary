from flask import Flask
from diary import app
#app = Flask(__name__)

@app.route('/')
def test():
    return "welcome to test page"

if __name__ == '__main__':
    app.run()
