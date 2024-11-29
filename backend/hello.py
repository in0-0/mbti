from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

questions = [
    {"id": 0, "text": "넌 외향적이냐", "options": ["Y", "N"]},
    {"id": 1, "text": "넌 내향인이냐", "options": ["Y", "N"]},
    {"id": 2, "text": "넌 친구 있냐", "options": ["Y", "N"]}
]

@app.route('/')
def home():
    print(render_template("index.html"))
    return render_template("index.html")

@app.route("/question/<int:question_id>", methods=["GET"])
def get_question(question_id):
    if question_id < len(questions):
        question = questions[question_id]
        return jsonify(question)
    else:
        return jsonify({"text": "모든 질문 완료"})

@app.route('/submit', methods=["POST"])
def submit_answer():
    data = request.json
    print(data)
    return jsonify({"message": "답변이 저장되었습니다.", "data": data})

if __name__ == "__main__":
    app.run(debug=True)