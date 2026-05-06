import os
import random
from flask import Flask, jsonify

app = Flask(__name__)
secret_number = random.randint(1, 100)

@app.route('/guess/<int:guess>')
def guess(guess):
    global secret_number
    if guess < secret_number:
        return jsonify({"msg": "Higher"})
    elif guess > secret_number:
        return jsonify({"msg": "Lower"})
    else:
        old = secret_number
        secret_number = random.randint(1, 100)
        return jsonify({"msg": "Correct! New game started.", "old_secret": old})

@app.route('/')
def home():
    return jsonify({"msg": "Guess a number between 1 and 100 at /guess/<number>"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
