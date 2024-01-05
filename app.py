from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dummy_index():
    message = 'To test the game1 route, append /game1 at the end of the URL string or click <a href="http://localhost:5000/game1">here</a>'
    return message

@app.route('/game1')
def game1():
    return render_template('game1.html')

if __name__ == '__main__':
    app.run(debug=True)