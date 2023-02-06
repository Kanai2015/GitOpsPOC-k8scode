from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Ditipriya Bublai Sonai Humpu buri- Here you go with your first GitOps demo\... TY!!!'
