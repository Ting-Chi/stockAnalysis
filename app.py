'''import flask
import io
import urllib.request
import json
from flask import request, render_template

# initialize our Flask application
app = flask.Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def predict():
    if flask.request.method == "POST":
        return render_template('index.html')
    else:
        data = {}
       
        data['stock-date']=request.form['stock-date']
        input1=[]
        input1.append(data)
        
        data = str.encode(json.dumps(input1))
        print(data)
        
        url = 'https://ussouthcentral.services.azureml.net/workspaces/60222f0db7d747efb0c25f133c5f7222/services/21f2075997064547aabfebec42c748c6/execute?api-version=2.0&format=swagger'
        api_key = 'O6NKVxKiA5/wWPB9zAy6jWGjgounMm1q5kV/zGtNWyrqevD+ZP5moU7omFiNdTL2ZOY1HLDLRSeocnPhpD3QcQ=='
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, data, headers)
        print(req.text)
        result=''
        response = urllib.request.urlopen(req)
        result = response.read()
        result_dict = json.loads(result)
        ScoredLabels = result_dict["Results"]["output1"][0]["Scored Labels"]

        # return the data dictionary as a JSON response
        return "Scored Labels:"+ ScoredLabels #flask.jsonify(result)
        
# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    app.run()
'''

from flask import Flask, request, render_template
app = Flask(__name__)

#網頁執行/stock時，會導至index.html
@app.route('/stock=['GET']')
def getdata():
    return ranger_template('index.html')

#index.html按下submit時，會取得前端傳來的username，並回傳"Hellold! "+name
@app.route('/stock=['POST']')
def submit():
    name = request.form.get('usernamereturn "Hello, " + name')

if __name__ == '__main__':
 app.run()

'''
def hello():
    return "Hello Azure!"
'''
