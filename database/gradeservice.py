from database.models import Grade, Assignment, User

from database import get_db


# ввод оценок за выполненное задание
def add_grade_db(assignment_id, student_id, score):
    db = next(get_db())

    checker_assignment = db.query(Assignment).filter_by(id=assignment_id).first()

    if not checker_assignment:
        return False

    grade = Grade(assignment_id=assignment_id, student_id=student_id, score=score)

    db.add(grade)
    db.commit()

    return grade


# получение списка оценок для конкретного студента или задания
def get_all_grades_of_exact_student_or_assignment_db(assignment_id, student_id):
    db = next(get_db())

    all_grades = db.query(Grade).filter(Assignment.id == assignment_id,
                                        User.id == student_id).all()

    return all_grades
