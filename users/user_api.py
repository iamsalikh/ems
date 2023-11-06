from fastapi import APIRouter, Body
from users import UserRegisterModel, LoginUserModel
from database.userservice import register_user_db, login_user_db, change_user_info_db, get_exact_user_db, get_all_users_db

user_router = APIRouter(prefix='/user', tags=['Управления пользователями'])


# регистрация
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    result = register_user_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Пользователь с такой почтой существует'}


# аутентификация
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    result = login_user_db(**data.model_dump())
    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователя с такой почтой не найдено'}


# получение списка всеx пользователей
@user_router.get('/get-all-users')
async def get_all_users():
    result = get_all_users_db()

    return {'status': 1, 'message': result}


# получение конкретного пользователя по его id
@user_router.get('/get-exact-user')
async def get_exact_user(user_id: int):
    result = get_exact_user_db(user_id)
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Пользователь не найден'}


# редактирование профилей пользователей(изменение пароля, контактной информации)
@user_router.put('/change-user-info')
async def change_user_info(user_id: int = Body(...), info_to_change: str = Body(...), new_info: str = Body(...)):
    result = change_user_info_db(user_id, info_to_change, new_info)
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Пользователь не найден'}
