from datetime import datetime


class UserEmailDefinition:
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
    email = (timestamp + '_test@example.net')


SCENARIO = {
    'email': UserEmailDefinition.email,
    'password': 'Test123456',
    'confirmPassword': 'Test123456',
    'lastName': 'Тестов',
    'firstName': 'Тест',
    'patronymic': 'Тестович',
    'phoneNumber': '+79999999999'
}


