from flask import Flask, render_template
import json

app = Flask(__name__)

with open('tds.json','r') as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('home.html')
if __name__ == "__main__":
    app.run()