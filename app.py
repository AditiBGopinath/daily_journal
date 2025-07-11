from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/write", methods=["GET", "POST"])
def write():
	if request.method == "POST":
		entry = request.form["entry"]
		return render_template("submitted.html", entry_text=entry)	
	return render_template("write.html")

if __name__ =="__main__":
	app.run(debug=True)
