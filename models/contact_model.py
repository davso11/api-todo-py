from models.database import MySQLDB
from utils.jsonConverter import toJson


class Contact():
    def __init__(self, db: MySQLDB):
        self.__dbConnection = db.connection
        self.__contacts = self.__fetch_all()

    def __query(self, sql, params=[], isEdit=False):
        self.__dbConnection.connect()
        cursor = self.__dbConnection.cursor()

        if (len(params) == 0):
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)

        results = cursor.fetchall()

        if not isEdit:
            fields_list = cursor.description

        if (isEdit):
            self.__dbConnection.commit()
            cursor.close()
            self.__dbConnection.close()
            return 'Done'

        cursor.close()
        self.__dbConnection.close()

        return toJson(fields_list, results)

    def __fetch_all(self):
        sql = 'SELECT contact, contactId, userId FROM contact'
        return self.__query(sql)

    def get_all(self):
        return self.__contacts

    def get_one(self, contactId):
        sql = 'SELECT contactId, contact, userId FROM contact WHERE contactId = %s'
        row = self.__query(sql, [contactId])
        return row

    def update(self, contactId, phone):
        sql = "UPDATE contact SET contact = %s, updatedAt = CURRENT_TIMESTAMP WHERE contactId = %s"
        row = self.__query(sql, [phone, contactId], True)
        return row
