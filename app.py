import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "I am a CI-CD hero!"

if __name__ == '__main__':
    app.run(
        debug=True, # Optional but useful for now
        host="0.0.0.0" # Listen for connections directed _to_ any address
    )
