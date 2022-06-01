from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generic")
def generic():
    return render_template("generic.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/type")
def type():
    return render_template("type.html")

@app.route("/location")
def location():
    return render_template("location.html")

if __name__ == "__main__":
    app.run(debug=True)
