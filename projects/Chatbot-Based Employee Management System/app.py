from flask import Flask, request, jsonify
from chatbot import extract_employee_data
from employee_service import create_employee
from mongo_db import save_chat

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():

    payload = request.get_json(silent=True) or {}
    message = payload.get("message")

    if not message:
        return jsonify({"error": "Field 'message' is required."}), 400

    data = extract_employee_data(message)

    if data["employee_name"]:

        emp = create_employee(data)

        response = f"""
Employee Created Successfully

Employee ID : {emp['employee_id']}
Name : {emp['employee_name']}
Department : {emp['department']}
Skills : {emp['skills']}
"""

    else:

        response = "Please provide employee details."

    save_chat(message, response)

    return jsonify({"response": response})


if __name__ == "__main__":
    # Disable the reloader to avoid daemon-thread shutdown errors on exit.
    app.run(debug=True, use_reloader=False)
