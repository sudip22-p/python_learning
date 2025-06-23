from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    title = request.form["title"]
    rent = request.form["rent"]
    location = request.form["location"]
    furnished = request.form["furnished"]
    return f"Added: {title}, Rent: {rent}, Location: {location}, Furnished: {furnished}"


if __name__ == "__main__":
    app.run(debug=True)
