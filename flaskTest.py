from flask import Flask

app = Flask(__name__) # __name__은 현재 모듈의 이름
@app.route("/")
def hello() :
    return "hello, Let's use the flask."

