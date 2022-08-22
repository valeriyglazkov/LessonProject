from psycopg2.sql import SQL


class DBCleaner:

    def __init__(self, connection):
        self.connection = connection

    def delete_users(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM "AspNetUsers"')
        self.connection.commit()
