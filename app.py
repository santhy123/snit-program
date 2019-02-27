from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "HELLO.... I AM SANTHY"
@app.route("/home")
def home():
    return "welcome to my home page"
@app.route("/contact")
def contact():
    return "contact the page"
@app.route("/abort")
def abort():
    return "abort the page"
if (__name__=="__main__"):
    app.run()