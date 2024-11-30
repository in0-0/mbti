from app import create_app
from services.question_service import QuestionService

if __name__ == "__main__":
    question_service = QuestionService()  # 서비스 객체 생성
    app = create_app(question_service)  # 의존성 주입
    app.run(debug=True)
