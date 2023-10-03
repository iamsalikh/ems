from pydantic import BaseModel


class AssignmentCreateModel(BaseModel):
    course_id: int
    description: int
    deadline: str
