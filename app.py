from flask import Flask
import os

app = Flask(__name__)
SECRET_NUMBER = 42

@app.route('/guess/<int:guess>')
def guess(guess):
    if guess < SECRET_NUMBER:
        return {"msg": "Higher"}
    elif guess > SECRET_NUMBER:
        return {"msg": "Lower"}
    else:
        return {"msg": "Correct! You win!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
