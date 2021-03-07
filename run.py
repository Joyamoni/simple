from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    print(a)
    return jsonify(result=a + b)


@app.route("/test.html")
def html():
	return render_template("args.html")


@app.route("/req")
def wow():
	d=request.args.get("the_data")
	if d=="hello":
		return jsonify(msg="wow you clicked",color="red")





if __name__ == "__main__":
    app.run()