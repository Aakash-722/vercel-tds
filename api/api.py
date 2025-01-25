from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the JSON data
with open("q-vercel-python.json") as file:
    data = json.load(file)

@app.route("/api", methods=["GET"])
def get_marks():
    # Extract names from query parameters
    names = request.args.getlist("name")
    marks = [data.get(name, "Not Found") for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
