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


@contact_bp.route('/api/contacts/<contactId>', methods=['PUT', 'POST'])
def update(contactId):
    reqBody = request.get_json()
    phone = reqBody.get('phone')
    resp = main_services.update(contactId, phone)
    return resp, 204
