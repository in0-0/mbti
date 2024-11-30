import pytest

from backend.app import create_app


# Mock 서비스 클래스
class MockQuestionService:
    def get_question_by_id(self, question_id):
        if question_id == 1:
            return {"id": 1, "text": "Mock Question"}
        raise ValueError(f"Question with ID {question_id} not found.")


@pytest.fixture
def client():
    mock_service = MockQuestionService()
    app = create_app(mock_service)
    app.config["TESTIING"] = True

    with app.test_client() as client:
        yield client


def test_get_question(client):
    response = client.get("/question/1")
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "text": "Mock Question"}
