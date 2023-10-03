from pydantic import BaseModel


class CourseCreateModel(BaseModel):
    name: str
    teacher_id: int
