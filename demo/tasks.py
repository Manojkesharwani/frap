import frappe
from frappe.utils import random_string


def cron():
    token = random_string(10)
    doc = frappe.get_doc({
    'doctype': 'Demo User',
    'username': 'New Task1',
    "password": "password",
    "token" : token
    })
    doc.insert()

    token = random_string(10)
    doc = frappe.get_doc("Demo User","New Task1")
    doc.token = token
    doc.save()

# def all():
#     pass


# def daily():
#     doc = frappe.new_doc("Dailyy")
#     doc.title = "Daily new_doc"
#     doc.insert()



# def hourly():
#     doc = frappe.get_doc({
#     'doctype': 'Dailyy',
#     'title': 'Manoj'
#     })
#     doc.insert()


# def weekly():
#     doc = frappe.get_doc({
#     'doctype': 'Dailyy',
#     'title': 'weekly'
#     })
#     doc.insert()

# def monthly():
#     doc = frappe.get_doc({
#     'doctype': 'Dailyy',
#     'title': 'monthly'
#     })
#     doc.insert()