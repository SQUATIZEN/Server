from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return "Aplikasi Ngukurban"

if __name__ == '__main__':
    app.run()