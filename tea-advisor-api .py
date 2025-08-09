from flask import Flask, jsonify, request
import random

app = Flask(__name__)

teas = [
    "Green Tea",
    "Black Tea",
    "Oolong Tea",
    "Chamomile Tea",
    "Peppermint Tea"
]

@app.route("/", methods=["GET"])
def index():
    return jsonify(endpoints=["/tea (GET, POST)", "/tea-by-mood?mood=<mood>"])

@app.route("/tea", methods=["GET"])
def get_random_tea():
    return jsonify(tea=random.choice(teas))

@app.route("/tea", methods=["POST"])
def add_tea():
    data = request.get_json() or {}
    name = (data.get("name") or "").strip()

    if not name:
        return jsonify(error="Field 'name' is required"), 400
    if len(name) > 50:
        return jsonify(error="Tea name must be ≤ 50 characters"), 400
    if name in teas:
        return jsonify(error="This tea already exists"), 409

    teas.append(name)
    return jsonify(added=name), 201

@app.route("/tea-by-mood", methods=["GET"])
def tea_by_mood():
    mood_map = {
        "relaxed": ["Chamomile Tea", "Peppermint Tea"],
        "energetic": ["Green Tea", "Black Tea"],
        "creative": ["Oolong Tea", "Matcha"]
    }
    mood = request.args.get("mood", "").lower()
    if mood not in mood_map:
        return jsonify(error="Unknown mood"), 400
    return jsonify(tea=random.choice(mood_map[mood]))

if __name__ == "__main__":
    
