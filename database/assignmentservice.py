from database.models import Assignment

from database import get_db


# создание новых заданий для курсов
def create_assignment_db(course_id, description, deadline):
    db = next(get_db())

    checker = db.query(Assignment).filter_by(id=course_id).first()
    if checker:
        return False

    new_assignment = Assignment(id=course_id, description=description, deadline=deadline)

    db.add(new_assignment)
    db.commit()

    return new_assignment


# получение списка заданий для определенного курса
def get_list_of_assignments_exact_course_db():
    db = next(get_db())

    all_assignments = db.query(Assignment).all()

    return all_assignments


# получение информации о конкретном задании по его ID
def get_info_about_exact_assignment_db(assignment_id):
    db = next(get_db())

    exact_assignment = db.query(Assignment).filter_by(id=assignment_id).first()

    return exact_assignment


# Редактирование заданий(изменения описания, дедлайнов, прикрепленных файлов)
def change_info_of_assignment_db(assignment_id: int, info_to_change: str, new_info: str):
    db = next(get_db())

    checker = db.query(Assignment).filter_by(id=assignment_id).first()

    if checker:
        if info_to_change == 'new description':
            checker.description = new_info

        elif info_to_change == 'new deadline':
            checker.deadline = new_info

        db.commit()

        return f'{info_to_change} изменения внесены'
