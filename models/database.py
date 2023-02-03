from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect, Error


load_dotenv()


class MySQLDB:
    def __init__(self) -> None:
        self.connection = self.__createConnection()
        self.cursor = self.connection.cursor()

    def __createConnection(self):
        try:
            return connect(
                host=getenv("MYSQL_HOST"),
                database=getenv("MYSQL_DB"),
                user=getenv("MYSQL_USER"),
                password=getenv("MYSQL_PASSWORD"),
            )
        except Error as e:
            print('MySQL Database connection error : ', e)
