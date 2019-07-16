# run with env FLASK_APP=dice_server.py flask run

from flask import Flask
import random

app = Flask(__name__)

dice_results = [1, 2, 3, 4, 5, 6]
DICE_IMAGES_PATH = "static/{}.jpg"

def get_dice_result():
    return random.choice(dice_results)

@app.route('/')
def roll_dice():
    return "Dice roll: %d" % get_dice_result()

@app.route('/img')
def roll_dice_with_image():
    result = get_dice_result()
    img = DICE_IMAGES_PATH.format(result)
    return '<img src="' + img + '" alt="' + str(result )+ '">'
