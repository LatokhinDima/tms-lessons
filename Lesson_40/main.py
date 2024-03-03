from fastapi import FastAPI
from polls_models import Database, Question, PaginatedQuestion

app = FastAPI()
db = Database()

@app.get("/questions")
def get_questions(ordering: str = '-pub_date', page_size: int = 5, page: int = 1) -> PaginatedQuestion:
    questions = db.get_questions()[(page - 1) * page_size: page * page_size]
    return PaginatedQuestion(count=len(questions), results=questions)


