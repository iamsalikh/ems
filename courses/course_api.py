from fastapi import APIRouter, Body
from courses import CourseCreateModel
from database.courseservice import create_course_db, get_all_courses_db, get_exact_course_db, change_course_name_db, delete_course_db
course_router = APIRouter(prefix='/course', tags=['Управления курсами'])


# создание новых курсов
@course_router.post('/create-course')
async def create_course(data: CourseCreateModel):
    result = create_course_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Такой курс существует'}


# получение списка всех курсов
@course_router.get('/get-all-courses')
async def get_all_courses():
    result = get_all_courses_db()

    return {'status': 1, 'message': result}


# получение информации о конкретном курсе по его ID
@course_router.get('/get-exact-course')
async def get_exact_course(course_id: int = None):
    if course_id is None:
        result = get_all_courses_db()
    else:
        result = get_exact_course_db(course_id)

    return result


# редактирование курсов(изменение названия, добавление/удаление материалов)
@course_router.put('/change-course')
async def change_course_info(course_id: int = Body(...), name: str = Body(...)):
    result = change_course_name_db(course_id, name)

    return {'status': 1, 'message': result}


@course_router.delete('/delete-course')
async def delete_course(course_id):
    result = delete_course_db(course_id)

    return {'status': 1, 'message': result}
