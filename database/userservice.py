from database.models import User

from database import get_db


# регистрация
def register_user_db(name, surname, phone_number, email, password, city, role):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return False

    new_user = User(name=name, surname=surname, phone_number=phone_number, password=password, city=city, role=role)

    db.add(new_user)
    db.commit()


# аутентификация
def login_user_db(email, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return "Неверный пароль"

    return 'Ошибка в данных'


# получение списка всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


# получение конкретного пользователя по id
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    return exact_user


# редактировние профилей пользователей
def change_user_info_db(user_id: int, info_to_change: str, new_info: str):
    db = next(get_db())

    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        if info_to_change == 'new_password':
            checker.password = new_info

        elif info_to_change == 'new_email':
            checker.email = new_info

        elif info_to_change == 'new_city':
            checker.city = new_info

        db.commit()

        return f'{info_to_change} изменения внесены'

    return 'Пользователь не найден'
