from flask import Flask, render_template, request
import json
import os
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def get_meal():
   response = requests.get('http://' + str(os.environ.get("API_HOST")) + ':' + str(os.environ.get("API_PORT")) + "/" + str(os.environ.get("API_ENDPOINT")))
   response = response.content
   response = json.loads(response)
   meal = response['meal']
   price = response['price']
   
   return render_template('web.html', meal = meal, price = price)

# run some times with error because I put the file in wrong folder



if __name__=='__main__':
    app.run(host='0.0.0.0', port = 80, debug=True)


# reference https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/

