from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_folder="assets", static_url_path="/content")

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
    new_id = (
        max([p["id"] for p in properties]) + 1 if properties else 1
    )  # this line finds the next available ID meaning it checks the current highest ID and adds 1 to it
    new_property = {
        "id": new_id,
        "title": data.get("title"),
        "location": data.get("location"),
        "rent": data.get("rent"),
    }
    properties.append(new_property)
    return jsonify(new_property), 201


if __name__ == "__main__":
    app.run(debug=True)
