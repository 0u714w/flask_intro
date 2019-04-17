#! python3

from flask import Flask, render_template
from tinydb import TinyDB
import random


app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def print_recipe(recipe=None):
    return render_template('recipe.html', recipe=random_recipe())

def random_recipe():
    all = db.all()
    r = random.choice(all)
    return r

