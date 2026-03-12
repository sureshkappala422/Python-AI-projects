from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    response = chatbot_response(message)

    # Convert MongoDB ObjectId to string
    if "_id" in response:
        response["_id"] = str(response["_id"])

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)