from flask import Flask, request
import random

import os
import json

app = Flask(__name__)

@app.route('/rec1')
def meal_recom():
    meals = [
    {'meal': 'Burger', 
     'price': '$10'},
    {'meal': 'Fish', 
     'price': '$17'},
    {'meal': 'Pizza', 
     'price': '$15'},
    {'meal': 'Beef', 
     'price': '$19'},
    {'meal': 'Sandwich', 
     'price': '$13'},
    {'meal': 'Turkey', 
     'price': '$16'},
    {'meal': 'Dumplings',
     'price': '$12'},
    {'meal': 'Hotpot', 
     'price': '$10'},
    {'meal': 'Dumsum', 
     'price': '$17'},
    {'meal': 'Noodle', 
     'price': '$13'},
    {'meal': 'Taco', 
     'price': '$18'},
    {'meal': 'Chaofan', 
     'price': '$15'},
    {'meal': 'Baozi', 
     'price': '$30'}]
    meal_show = random.choice(meals)
    return json.dumps(meal_show)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
