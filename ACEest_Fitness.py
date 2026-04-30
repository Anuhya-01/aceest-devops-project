from flask import Flask, request, jsonify

app = Flask(__name__)

# Instructor logic (integrated here)
programs = {
    "Fat Loss (FL)": 22,
    "Muscle Gain (MG)": 35,
    "Beginner (BG)": 26
}

@app.route('/')
def home():
    return "ACEest Running"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'weight' not in data or 'program' not in data:
        return jsonify({"error": "weight and program required"}), 400

    weight = data['weight']
    program = data['program']

    if program not in programs:
        return jsonify({"error": "Invalid program"}), 400

    calories = int(weight * programs[program])

    return jsonify({
        "program": program,
        "calories": calories
    })

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)