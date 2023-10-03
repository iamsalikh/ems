from database.models import Grade, Assignment

from database import get_db


# ввод оценок за выполненное задание
def add_grade_db(assignment_id, student_id, score):
    db = next(get_db())

    checker = db.query(Grade).filter_by(assignment_id=assignment_id, student_id=student_id).first()

    if checker:
        return False

    grade = Grade(assignment_id=assignment_id, student_id=student_id, score=score)

    db.add(grade)
    db.commit()

    return grade


# получение списка оценок для конкретного студента или задания
def get_all_grades_of_exact_student_or_assignment_db(assignment_id, student_id):
    db = next(get_db())

    all_grades = db.query(Grade).filter(Grade.assignment_id == assignment_id,
                                        Grade.student_id == student_id).all()

    return all_grades


# расчет средней оценки для студента по курсу
def calculate_average_grade_db(student_id, course_id):
    db = next(get_db())

    grades = db.query(Grade).join(Assignment).filter(Assignment.course_id == course_id,
                                                     Grade.student_id == student_id).all()

    if not grades:
        return None

    total_score = sum(grade.score for grade in grades)
    average_score = total_score / len(grades)

    return average_score
