from flask import Flask, jsonify, render_template, request
from pydantic import BaseModel, ValidationError

from backend.services.question_service import QuestionService


class Answer(BaseModel):
    id: int
    answer: str


def create_app(question_service: QuestionService) -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        print(render_template("index.html"))
        return render_template("index.html")

    @app.route("/question/<int:question_id>", methods=["GET"])
    def get_question(question_id):
        try:
            question = question_service.get_question_by_id(question_id)
            return jsonify(question)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.route("/submit", methods=["POST"])
    def submit_answer():
        try:
            data = Answer(**request.json)
            print(data)
            return jsonify({"message": "답변이 저장되었습니다.", "data": data.dict()})
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

    return app
