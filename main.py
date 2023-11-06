from fastapi import FastAPI

from database import Base, engine
Base.metadata.create_all(bind=engine)

from users.user_api import user_router
from assignments.assignment_api import assignment_router
from courses.course_api import course_router
from grades.grade_api import grade_router

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(course_router)
app.include_router(assignment_router)
app.include_router(grade_router)


@app.get('/hello')
async def hello_world():
    return {'message': 'Hello Wild!'}
