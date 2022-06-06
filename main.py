# -*- coding:UTF-8 -*-
from asyncore import read
from flask import Flask, render_template,request,redirect,url_for
import pandas
import joblib
from pandas import DataFrame
import math

def rad(d):
   return d * math.pi / 180.0

def getDistance(LngA, LatA, LngB, LatB):
    R = 6371.004
    C = math.sin(rad(LatA)) * math.sin(rad(LatB)) + math.cos(rad(LatA)) * math.cos(rad(LatB)) * math.cos(rad(LngA - LngB))
    return (R * math.acos(C))

def score(LngA, LatA, LngB, LatB):
    D = getDistance(LngA, LatA, LngB, LatB)
    #大於100不顯示 小於100的計分，距離越近分數越高
    if (D > 50):
        return -1
    else:
        return 100 - (D*2)

loaded_model = joblib.load('forest_knowledge_model')
knowledge = {"管理":[],"行政管理":[],"經濟學和會計學":[],"銷售和行銷":[],"客戶和個人服務":[],"人力資源":[],"交通運輸":[],"生產和作業":[],"食品生產":[],"資訊與電子":[],"工程與科技":[],"設計":[],"建築營造":[],"機械":[],"數學":[],"物理":[],"化學":[],"生命科學":[],"心理學":[0],"社會學和人類學":[],"地理":[],"醫藥和牙科":[0],"治療和諮商":[0],"教育和訓練":[0],"本國語言":[0],"外國語文":[],"藝術":[],"歷史與考古":[],"哲學和宗教":[],"公共安全和資訊安全":[],"法律和政府":[0],"網路與電信":[],"傳播和媒體":[]}
lng_lat = {
'新北市':  [121.6739  ,24.91571],
'高雄市':  [120.666   ,23.01087], 
'台中市':  [120.9417  ,24.23321],
'台北市':  [121.5598  ,25.09108],
'桃園市':  [121.2168  ,24.93759],
'台南市':  [120.2513  ,23.1417 ],
'彰化縣':  [120.4818  ,23.99297], 
'屏東縣':  [120.62    ,22.54951], 
'雲林縣':  [120.3897  ,23.75585], 
'苗栗縣':  [120.9417  ,24.48927], 
'嘉義縣':  [120.574   ,23.45889], 
'新竹縣':  [121.1252  ,24.70328], 
'南投縣':  [120.9876  ,23.83876], 
'宜蘭縣':  [121.7195  ,24.69295], 
'新竹市':  [120.9647  ,24.80395], 
'基隆市':  [121.7081  ,25.10898], 
'花蓮縣':  [121.3542  ,23.7569 ],
'嘉義市':  [120.4473  ,23.47545], 
'台東縣':  [120.9876  ,22.98461], 
'金門縣':  [118.3186  ,24.43679], 
'澎湖縣':  [119.6151  ,23.56548], 
'連江縣':  [119.5397  ,26.19737]
}

loc = ""
result_name = ""
data = DataFrame({"tmp":[]})

def read_file(filename):
    data = pandas.read_excel(filename, header=0)
    score_list=[]
    for i in range(len(data.values)):
        data_loc = data.values[i][6]
        s = score(lng_lat[loc][0],lng_lat[loc][1],lng_lat[data_loc[0:3]][0],lng_lat[data_loc[0:3]][1])
        score_list.append(s)
    data["score"] = score_list
    data = data.sort_values(by=['score'],ascending=False)
    return data

# for i in knowledge:
#     a = random.randint(0,1)
#     knowledge[i].append(a)
# dataframe = DataFrame(knowledge)
# result = loaded_model.predict(dataframe)

app = Flask(__name__)
@app.route("/jobone/<index>")
def jobone(index):
    global data,result_name
    print(index)
    id = int(index)

    # if id == 0:
    filename = result_name+'.xlsx'
    data = read_file(filename)
    
    myData = data.values[id]
    return render_template("job_test.html", myData=myData,id=id)

@app.route("/")
def index():
    global loc,result_name,data
    loc = ""
    result_name = ""
    data = DataFrame({"tmp":[]})
    return render_template("index.html")

@app.route("/generic")
def generic():
    return render_template("generic.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

# @app.route("/type",methods=['POST','GET'])
# def type():
#     global loc
#     if request.method == "GET":
#         loc = request.url.split('=')[1]
#         print("location",loc)
#     return render_template("type.html")

@app.route("/type1",methods=['POST','GET'])
def type1():
    global loc
    if request.method == "GET":
        loc = request.url.split('=')[1]
        print("location",loc)
    return render_template("type1.html")

@app.route("/select")
def select():
    return render_template("select.html")

@app.route('/location',methods=['POST','GET'])
def location():
    if request.method == "POST":
        location = request.form['location']
        return redirect(url_for('type1',location = location))
    return render_template('location.html')

@app.route("/question/<index>",methods=['POST','GET'])
def question(index):
    print(index)
    id = int(index)
    filename = 'question.xlsx'
    question = pandas.read_excel(filename, header=0)
    global result_name, data
    if id == 27:
        print("data",type(data),data)
        for i in knowledge:
            if len(knowledge[i]) > 1:
                knowledge[i] = [knowledge[i][0]]
            elif len(knowledge[i]) < 1:
                knowledge[i] = [1]
        dataframe = DataFrame(knowledge)
        result = loaded_model.predict(dataframe)
        result_name = str(result)[1:-1]
        # filename = result_name+'.xlsx'
        # data = read_file(filename)
        # print("type",type(data),data)
        return redirect(url_for('jobone',index = 0))
        
    myData = question.values[id]
    if request.method == "POST":
        knowledge[myData[0]].append(request.form['feature'])
        # print(myData[0],knowledge[myData[0]])
        print(id)
        knowledge[myData[0]].append(request.form['feature'])
    return render_template("question.html", myData=myData,id=id)

@app.route("/job2")
def job2():
    return render_template("job2.html")

@app.route("/job1")
def job1():
    return render_template("job1.html")

if __name__ == "__main__":
    app.run(debug=True)
