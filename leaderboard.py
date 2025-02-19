from flask import Flask, request, jsonify

app = Flask(__name__)
leaderboard = []

@app.route('/leaderboard', methods=['POST'])
def save_score():
    score = request.json['score']
    leaderboard.append(score)
    leaderboard.sort(reverse=True)  # Highest score first
    return jsonify({"status": "saved", "leaderboard": leaderboard[:10]})  # Return top 10

if __name__ == "__main__":
    app.run(debug=True)

