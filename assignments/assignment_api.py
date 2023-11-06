from fastapi import APIRouter, Body
from assignments import AssignmentCreateModel
from database.assignmentservice import create_assignment_db, get_list_of_assignments_exact_course_db, get_info_about_exact_assignment_db, change_info_of_assignment_db

assignment_router = APIRouter(prefix='/assignment', tags=['Управление заданиями'])


# создание новых заданий для курсов
@assignment_router.post('/create-assignment')
async def create_assignment(data: AssignmentCreateModel):
    result = create_assignment_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Такое задание существует'}


# получение списка заданий для определенного курса
@assignment_router.get('/get-all-assignments-of-exact-course')
async def get_all_assignments_of_exact_course():
    result = get_list_of_assignments_exact_course_db()

    return {'status': 1, 'message': result}


# получение информации о конкретном задании по его ID
@assignment_router.get('/get-info-about-exact-assignment')
async def get_info_about_exact_assignment(assignment_id: int):
    result = get_info_about_exact_assignment_db(assignment_id)
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Задание не найдено'}


# Редактирование заданий(изменения описания, дедлайнов)
@assignment_router.put('/change-info-of-assignment')
async def change_info_of_assignment(assignments_id: int = Body(...),
                                    info_to_change: str = Body(...),
                                    new_info: str = Body(...)):
    result = change_info_of_assignment_db(assignments_id, info_to_change, new_info)

    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Задания не найдена'}
