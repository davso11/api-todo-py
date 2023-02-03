from os import getenv
from dotenv import load_dotenv
from mysql import connector


load_dotenv()


class MySQLDB:
    def __init__(self) -> None:
        self.connection = self.__createConnection()

    def __createConnection(self):
        try:
            return connector.connect(
                host=getenv("MYSQL_HOST"),
                database=getenv("MYSQL_DB"),
                user=getenv("MYSQL_USER"),
                password=getenv("MYSQL_PASSWORD"),
            )
        except connector.Error as e:
            print('MySQL Database connection error : ', e)
