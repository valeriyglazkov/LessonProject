from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from dataclass_wizard import JSONWizard, DateTimePattern


@dataclass
class RegisterVm(JSONWizard):
    """Модель представления данных регистрации пользователя"""
    email: str
    password: str
    confirm_password: str
    first_name: str
    last_name: str
    patronymic: Optional[str]
    phone_number: str


@dataclass
class LoginVm(JSONWizard):
    """Модель представления данных авторизации пользователя"""
    email: str
    password: str


@dataclass
class UserVm(JSONWizard):
    """Модель представления данных пользователя"""
    id: UUID
    first_name: str
    last_name: str
    patronymic: Optional[str]
    email: str
    phone_number: str
    registration_date: DateTimePattern['%Y-%m-%dT%H:%M:%S.%fZ']


@dataclass
class CheckLoginVm(str):
    email: str
    password: str
