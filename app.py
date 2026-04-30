from flask import Flask, jsonify, request

app = Flask(__name__)

programs = {
    "Fat Loss": {"factor": 22},
    "Muscle Gain": {"factor": 35},
    "Beginner": {"factor": 26}
}

@app.route("/")
def home():
    return "ACEest Fitness API Running"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    weight = data.get("weight")
    program = data.get("program")

    if program not in programs:
        return jsonify({"error": "Invalid program"}), 400

    calories = weight * programs[program]["factor"]
    return jsonify({"calories": calories})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)