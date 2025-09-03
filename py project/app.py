from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user_choice = data.get("choice")
    if user_choice not in choices:
        return jsonify({"error": "Invalid choice"}), 400

    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    return jsonify({
        "user_choice": user_choice,
        "comp_choice": comp_choice,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
