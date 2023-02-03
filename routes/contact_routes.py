from flask import Blueprint, request
from services import main_services


contact_bp = Blueprint('contact', __name__)


@contact_bp.route('/api/contacts/')
def get_contacts():
    resp = main_services.find_all_contacts()
    return resp


@contact_bp.route('/api/contacts/<string:contactId>')
def get_one(contactId):
    resp = main_services.find_one_contact(contactId)
    return resp


@contact_bp.route('/api/contacts/', methods=['PUT', 'POST'])
def update():
    reqBody = request.get_json()
    contact_id = reqBody.get('contactId')
    phone = reqBody.get('phone')
    # print(f'ID = {contact_id}\nPhone = {phone}')
    resp = main_services.update(contact_id, phone)
    return resp, 204
