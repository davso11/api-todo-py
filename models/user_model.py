from mysql.connector import MySQLConnection

class User:
    def __init__(self, db_connection: MySQLConnection):
        self.connection = db_connection

    def get_user(self, user_id: str) -> str:
        # open all
        self.connection.connect()
        cursor = self.connection.cursor()

        sql = "SELECT userId FROM user WHERE userId = %s"
        cursor.execute(sql, [user_id])
        result = cursor.fetchone()

        # close all
        cursor.close()
        self.connection.close()

        return result

    def get_completed(self):
        pass