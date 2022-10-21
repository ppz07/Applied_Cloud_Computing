
from flask import Flask, render_template
import requests
import json
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_meal():
   response = requests.get('http://' + str(os.environ.get("API_HOST")) + ':' + str(os.environ.get("API_PORT")) + "/" + str(os.environ.get("API_ENDPOINT")))
   response = response.content
   response = json.loads(response)
   meal = response['meal']
   price = response['price']
   
   return render_template('web.html', meal = meal, price = price)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port = 81, debug=True)
