import frappe
from frappe.utils import random_string
import requests
from frappe.utils.data import get_url
def check_user_exists(email):
    """
    Check if a user with the provied Email. exists
    """
    return frappe.db.exists('User', email)
def success_response(data=None, id=None):
    response = {'msg': 'success'}
    response['data'] = data
    if id:
        response['data'] = {'id': id, "name": id}
    return response
def error_response(err_msg):
    # frappe.log_error(frappe.get_traceback(), 'Api Error')
    return {
        'msg': 'error',
        'error': err_msg
    }