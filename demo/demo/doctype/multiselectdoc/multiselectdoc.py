# Copyright (c) 2023, manoj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Multiselectdoc(Document):
	pass
@frappe.whitelist()
def multiselect_fuc(**kwargs):
	doc = frappe.get_doc("item child table doctype",kwargs["key"])
	return doc

