from flask import Flask, jsonify, request, render_template, flash, get_flashed_messages

app = Flask(__name__, static_folder="assets", static_url_path="/content")
app.secret_key = "supersecretkey"  # Needed for flashing

properties = [
    {"id": 1, "title": "2BHK Apartment", "location": "Pokhara", "rent": 25000},
    {"id": 2, "title": "3BHK House", "location": "Kathmandu", "rent": 50000},
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/properties", methods=["GET"])
def get_properties():
    return jsonify(properties)


@app.route("/api/properties", methods=["POST"])
def add_property():
    data = request.get_json()
    if not data.get("title") or not data.get("location") or not data.get("rent"):
        return jsonify({"error": "Missing data"}), 400

    new_id = max([p["id"] for p in properties]) + 1 if properties else 1
    new_property = {
        "id": new_id,
        "title": data["title"],
        "location": data["location"],
        "rent": data["rent"],
    }
    properties.append(new_property)

    flash("Property added successfully!")

    return jsonify(new_property), 201


@app.route("/get-flash-messages")
def get_flash_messages():
    messages = get_flashed_messages()
    return jsonify(messages)


if __name__ == "__main__":
    app.run(debug=True)
