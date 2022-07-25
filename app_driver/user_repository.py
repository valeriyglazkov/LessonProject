from test_data.create_user import UserEmailDefinition


class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_users(self) -> list:
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            records = cursor.fetchall()

            users = list()
            for row in records:
                users.append({
                    'id': row[0],
                    'first_name': row[2],
                    'last_name': row[3],
                    'patronymic': row[4],
                    'email': row[5],
                    'phone_number': row[6]
                })

            return users

    # def get_user_id(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(f"SELECT user_id FROM users WHERE email = '%{UserEmailDefinition.email}%'")
    #         user_id = cursor.fetchone()
    #         return user_id

    # def delete_user(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(f"DELETE FROM users WHERE user_id = {UserRepository.get_user_id(self)}")
