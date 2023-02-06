from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect, Error


load_dotenv()

class Database:
    def __init__(self):
        self.host = getenv('MYSQL_HOST')
        self.user = getenv('MYSQL_USER')
        self.password = getenv('MYSQL_PASSWORD')
        self.name = getenv('MYSQL_DB')

    def createConnection(self):
        try:
            return connect(
                host=self.host,
                database=self.name,
                user=self.user,
                password=self.password,
            )
        except Error as e:
            print('MySQL Database connection error : ', e.msg)