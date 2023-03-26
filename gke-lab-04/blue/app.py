# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
   html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Linux Academy!</h1><h2 style='color: #0000ff; text-shadow: 2px 2px 3px #030000'>Blue Version</h2><img src='https://storage.googleapis.com/la-gcp-labs-resources/essentials/Logo-Pinehead-NVY.png' width='40%' alt='Pinehead @ Linux Academy'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)