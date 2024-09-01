from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of words for the spelling bee practice
word_list = ["ship", "tank"]

# Route to serve the web page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get a random word
@app.route('/get_word')
def get_word():
    word = random.choice(word_list)
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(debug=True)
