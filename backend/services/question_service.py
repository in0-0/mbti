from backend.model.question_model import Question


class QuestionService:
    def __init__(self):
        self.questions = [
            Question(id=1, question="당신은 외향적입니까?"),
            Question(id=2, question="당신은 내향적입니까?"),
            Question(id=3, question="당신은 친구가 많습니까?"),
        ]

    def get_question_by_id(self, question_id) -> Question:
        if question_id < len(self.questions):
            return self.questions[question_id]
        else:
            raise ValueError(f"Question with ID {question_id} not found.")
