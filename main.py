from flask import Flask, render_template,request,redirect,url_for
import pandas
import joblib

app = Flask(__name__)
loaded_model = joblib.load('forest_knowledge_model')

@app.route("/jobone/<index>")
def jobone(index):
    print(index)
    id = int(index)
    filename = 'job_test.csv'
    data = pandas.read_csv(filename, header=0)
    myData = data.values[id]
    return render_template("job_test.html", myData=myData,id=id+1)

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

# @app.route("/type1/<string:location>")
# def type1(location):
#     return render_template("type1.html")
#     return f'{location}'

@app.route('/location',methods=['POST','GET'])
def location():
    #request_method = request.method
    if request.method == "POST":
        location = request.form['location']
        return redirect(url_for('type',location = location))
    return render_template('location.html')

@app.route("/job2")
def job2():
    return render_template("job2.html")

@app.route("/job1")
def job1():
    return render_template("job1.html")

if __name__ == "__main__":
    app.run(debug=True)
