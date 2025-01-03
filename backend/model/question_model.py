from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question: str
    option: list = ["Y", "N"]
