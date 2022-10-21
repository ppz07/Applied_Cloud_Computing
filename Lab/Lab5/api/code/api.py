from flask import Flask, request 
import json
from sqlalchemy import create_engine
import os
app = Flask(__name__)

db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('PG_USER')
db_pass = os.environ.get('PG_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('PG_PORT') 

url = f'postgresql://{db_user}:{db_pass}@{db_host}:{str(db_port)}/{db_name}'
db = create_engine(url)

@app.route('/meal_rec')
@app.route('/')
def meal_pick():
      query = 'SELECT meal_name, meal_price FROM meal ORDER BY RANDOM() LIMIT 1;'
      row = db.execute(query)
      meal_picked = {}
      for r in row:
            meal_picked['meal'] = r[0]
            meal_picked['price'] = r[1]
      
      return json.dumps(meal_picked)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("API_PORT"), debug=True)
