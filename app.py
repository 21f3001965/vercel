from flask import Flask
import json

app = Flask(__name__)

with open('tds.json','r') as f:
    data = json.load(f)

@app.route('/')
def home():
    return {"hello"}

if __name__ == "__main__":
    app.run()