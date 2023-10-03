from pydantic import BaseModel


class LoginUserModel(BaseModel):
    email: str
    password: str


class UserRegisterModel(BaseModel):
    name: str
    surname: str
    phone_number: int
    email: str
    password: str
    city: str
    role: str
