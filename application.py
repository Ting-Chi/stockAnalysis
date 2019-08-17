from flask import Flask, request, render_template
import urllib.request
import json
import sys

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])

def submit():
    if request.method == 'POST':
        date = request.values['date']
        data = {
            "Inputs": {
                "input1":
                [
                    {
                        'stock':"2732",   
                        'date': date,   
                        'cost': "89.11",   
                    }
                ],
            },
            "GlobalParameters":  {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/60222f0db7d747efb0c25f133c5f7222/services/21f2075997064547aabfebec42c748c6/execute?api-version=2.0&format=swagger'
        api_key = 'O6NKVxKiA5/wWPB9zAy6jWGjgounMm1q5kV/zGtNWyrqevD+ZP5moU7omFiNdTL2ZOY1HLDLRSeocnPhpD3QcQ==' 
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)
        
        try:
            response = urllib.request.urlopen(req)
            result = response.read()
            result_dict = json.loads(result)
            ScoredLabels = result_dict["Results"]["output1"][0]["Scored Labels"]
            return '輸入日期:  ' + date + '   預測金額:  ' + ScoredLabels
           
        except urllib.error.HTTPError as error:
            return 'The request failed with status code: ' + str(error.code)

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            return error.info()
            return json.loads(error.read().decode("utf8", 'ignore'))
            return 'error'
   
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()