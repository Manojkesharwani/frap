# Copyright (c) 2023, manoj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class customdoc1(Document):
	def before_insert(self):
		x=self.name1
		y=self.surname
		doc =frappe.new_doc("custom doc2")
		print(doc)
		doc.d_name = x
		doc.d_surname = y
		print(doc.d_name)
		doc.save()

	# def on_cancel(self):
	# 	doc2=frappe.get_doc("custom doc2",{"d_name":self.d_name})
	# 	if doc2:
	# 		doc2.delete()

