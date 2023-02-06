from mysql.connector import MySQLConnection


class Todo:
    def __init__(self, db_connection: MySQLConnection):
        self.connection = db_connection

    def get_active(self):
        # open all
        self.connection.connect()
        cursor = self.connection.cursor()

        sql = "SELECT COUNT(id) FROM todo WHERE isDone = 0"
        cursor.execute(sql)
        result = cursor.fetchone()

        # close all
        cursor.close()
        self.connection.close()

        return result

    def get_completed(self):
        self.connection.connect()
        cursor = self.connection.cursor()

        sql = "SELECT COUNT(id) FROM todo WHERE isDone = 1"
        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.close()
        self.connection.close()

        return result
