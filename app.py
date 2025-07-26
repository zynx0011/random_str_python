from flask import Flask
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_random_str():
    options = ["Investments", "Smallcase", "Stocks", "buy-the-dip", "TickerTape"]
    random_str = random.choice(options)
    return "Your random string is :" + random_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)