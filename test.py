from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)

@app.route("/compare", methods = ['POST'])
def compare():
    finalList = []
    stockList = request.json
    print(stockList)
    if len(stockList) > 0:
        for item in stockList:
            x = requests.get("https://www.okanebox.com.br/api/analisefundamentalista/"+item+"/")
            y = {
                'ticker': item,
            }
            x1 = x.json()
            print(x1[0])
            x1.insert(0, y)

            finalList.append(x1)
            
    return json.dumps(finalList)