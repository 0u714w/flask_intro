#! python3

from flask import Flask, render_template
from tinydb import TinyDB
from random import randint


app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def print_recipe(recipe=None):
    return render_template('recipe.html', recipe=random_recipe())

def random_recipe():
    all = db.all()
    random = all[randint(0,1)]
    return random['name'] + '\n' + random['instructions'] + '\n' + random['url']

