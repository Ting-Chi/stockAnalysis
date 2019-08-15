import flask
import io
import urllib.request
import json
from flask import request, render_template

# initialize our Flask application
app = flask.Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def predict():
    if flask.request.method == "GET":
        return render_template('index.html')
    else:
        data = {}
       
        data['stock-date']=request.form['stock-date']
        data['price']='0'
        input1=[]
        input1.append(data)
        
        body = str.encode(json.dumps(input1))
        print(body)
        url = '依據你的API填寫'
        api_key = '依據你的API填寫'
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)
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