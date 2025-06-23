# Flask is:
# A micro web framework in Python.
# Lightweight, beginner-friendly.
# Perfect for small to medium apps.
# Doesn’t force you into a structure (unlike Django).
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Sud!"


if __name__ == "__main__":
    app.run(debug=True)
