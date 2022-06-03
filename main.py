from flask import Flask, render_template
import csv
import hashlib
from pathlib import Path
import flask, pandas

app = Flask(__name__)

# class Cache:
#     template = '''<tbody>
# {% for v in data %}
#   <tr>
#     <td>{{ v[0] }}</td>
#     <td>{{ v[1] }}</td>
#     <td>{{ v[2] }}</td>
#     <td>{{ v[3] }}</td>
#   </tr>
# {% endfor %}
# </tbody>'''
#     csv_file = Path(__file__).parent / 'job_test.csv'

#     def __init__(self, app: flask.Flask):
#         self._app = app
#         self._cache = None
#         self._filehash = None
#         self()  # first-time initialization

#     def __call__(self):
#         filehash = self._hash_file()
#         if filehash != self._filehash:
#             self._filehash = filehash
#             self._cache = self._render()

#         return self._cache

#     def _hash_file(self) -> str:
#         with self.csv_file.open('rb') as f:
#             md5 = hashlib.md5()
#             while data := f.read(65536):  # 64kb chunks
#                 md5.update(data)
#             return md5.hexdigest()

#     def _render(self):
#         with self.csv_file.open(newline='') as f:
#             reader = csv.reader(f)
#             next(reader)  # skip header

#             with self._app.app_context():
#                 return flask.render_template_string(self.template, data=reader)

# cache = Cache(app)

# @app.route('/joball')
# def weather_dashboard():
#     return flask.render_template('home.html', table_body=cache())

@app.route('/joball')
def joball():
    filename = 'job_test.csv'
    data = pandas.read_csv(filename, header=0)
    myData = data.values
    return render_template('home.html', myData=myData)

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

@app.route("/job1")
def job1():
    filename = 'job_test.csv'
    data = pandas.read_csv(filename, header=0)
    myData = data.values
    return render_template("job1.html")

@app.route("/jobone")
def jobone():
    filename = 'job_test.csv'
    data = pandas.read_csv(filename, header=0)
    myData = data.values[0]
    return render_template("job_test.html", myData=myData)

@app.route("/job2")
def job2():
    return render_template("job2.html")



if __name__ == "__main__":
    app.run(debug=True)
