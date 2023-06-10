'''Explore the Flask Module and Create a Web Server
   Using Flask & Python?
'''
'''1) GO to Google
   2) Search Flask minimal APP
   3)Copy the Code and Start
   4)Need to Install
     cammand:pip install flask
     Flask is using to create website
     in python
   5) Click on the link of Terminal
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()