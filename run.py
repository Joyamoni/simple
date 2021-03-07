from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return("<h1>Hello flask</h1>")



if __name__ == "__main__":
    app.run()
