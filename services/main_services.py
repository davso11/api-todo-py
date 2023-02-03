from models.database import MySQLDB
from models.contact_model import Contact


# Modèles
contact = Contact(MySQLDB())


def find_all_contacts():
    return contact.get_all()


def find_one_contact(ID: str):
    return contact.get_one(ID)


def update(ID: str, phone: str):
    return contact.update(ID, phone)
