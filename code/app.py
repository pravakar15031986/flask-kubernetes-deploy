from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World from app Flaskfor testing purpose </h2>'

if __name__ == "__main__":
    app.run(debug=True)
