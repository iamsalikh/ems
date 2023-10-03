from database.models import Course

from database import get_db


# создание новых курсов
def create_course_db(name, teacher_id):
    db = next(get_db())

    checker = db.query(Course).filter_by(name=name).first()

    if checker:
        return False

    new_course = Course(name=name, teacher_id=teacher_id)

    return new_course


# получение списка всех курсов
def get_all_courses_db():
    db = next(get_db())

    all_courses = db.query(Course).all()

    return all_courses


# получение информации о конкретном курсе по его ID
def get_exact_course_db(course_id):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(id=course_id).first()

    return exact_course


# редактирование курсов(изменение названия, добавление/удаление материалов)
def change_course_name_db(course_id, name):
    db = next(get_db())

    course = db.query(Course).filter_by(id=course_id).first()

    if course:
        course.name = name

        db.commit()

        return course

    return 'Курс по такому ID не найден'


# удаление курса
def delete_course_db(course_id):
    db = next(get_db())

    course = db.query(Course).filter_by(id=course_id).first()

    if course:
        db.delete(course)
        db.commit()

        return True

    return False
