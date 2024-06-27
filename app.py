from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dice")
def dice_roll():
    dice = int(request.args.get("dice", "6"))
    roll = randint(1, dice)
    return render_template("dice_roll.html", dice=dice, roll=roll)

if __name__ == '__main__':
    app.run(debug=True)
