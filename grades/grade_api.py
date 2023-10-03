from fastapi import APIRouter

from database.gradeservice import add_grade_db, get_all_grades_of_exact_student_or_assignment_db, calculate_average_grade_db

grade_router = APIRouter(prefix='/grade', tags=['Управление оценками'])


# ввод оценок за выполненное задание
@grade_router.post('/add-grade')
async def add_grade(assignment_id, student_id, score):
    result = add_grade_db(assignment_id, student_id, score)

    if not result:
        return {'status': 0, 'message': 'Оценка уже существует'}

    return {'status': 1, 'message': result}


# получение списка оценок для конкретного студента или задания
@grade_router.get('/get-all-grades-of-exact-student-or-assignment')
async def get_all_grades_of_exact_student_or_assignment(assignment_id: int, student_id: int):
    result = get_all_grades_of_exact_student_or_assignment_db(assignment_id, student_id)

    return {'status': 1, 'message': result}


# расчет средней оценки для студента по курсу
@grade_router.get('/calculate-average-grade')
async def calculate_avarage_grade(student_id: int, course_id: int):
    result = calculate_average_grade_db(student_id, course_id)

    if result is None:
        return {'status': 0, 'message': 'Cтудент не имеет оценок по указанному курсу'}

    return {'status': 1, 'message': result}
