import json
from models.database import MySQLDB


class Contact:
    def __init__(self, db: MySQLDB) -> None:
        self.contactId = None
        self.contact = None
        self.userId = None

        # MySQL
        self.connection = db.connection

    def query(self, sql, params=[], isEdit=False):
        self.connection.connect()
        cursor = self.connection.cursor()

        if (len(params) == 0):
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)

        results = cursor.fetchall()

        if (isEdit):
            self.connection.commit()

        cursor.close()
        self.connection.close()

        return json.dumps(results)

    def get_all(self):
        sql = 'SELECT contactId, contact, userId FROM contact'
        rows = self.query(sql)
        return rows

    def get_one(self, contactId):
        sql = 'SELECT contactId, contact, userId FROM contact WHERE contactId = %s'
        row = self.query(sql, [contactId])
        return row

    def update(self, contactId, phone):
        sql = "UPDATE contact SET contact = %s, updatedAt = CURRENT_TIMESTAMP WHERE contactId = %s"
        row = self.query(sql, [phone, contactId], True)
        return row
