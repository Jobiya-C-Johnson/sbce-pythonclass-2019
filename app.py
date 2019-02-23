from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hello..."
    
@app.route("/Home")
def home():
    return "My home page"

@app.route("/Contact")
def contact():
    return "My contact"
if(__name__ == "__main__"):
    app.run()