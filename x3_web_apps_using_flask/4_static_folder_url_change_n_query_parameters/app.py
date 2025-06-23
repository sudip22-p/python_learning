from flask import Flask, render_template, request

# Change static folder to 'assets' and URL path to '/content'
# Normally, Flask serves static files from '/static' URL and 'static' folder.
# Changing to '/content' URL and 'assets' folder means:
# - You can name your folders however you want.
# - It avoids problems if '/static' URL clashes with other routes or tools in your app.
# For example, if you have a page or API using '/static', renaming the static URL fixes conflicts.
app = Flask(__name__, static_folder="assets", static_url_path="/content")


@app.route("/")
def home():
    # Grab query parameter 'user', default to 'Guest'
    username = request.args.get("user", "Guest")
    return render_template("index.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
