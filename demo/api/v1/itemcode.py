import frappe
from frappe.model.naming import *
from demo.utils import success_response, error_response
print("ss")
@frappe.whitelist(allow_guest=True)
def item(kwargs):
    print("ssss")
    try:
        data={}
        doc = frappe.new_doc("Purchase Reciept")
        print(doc)
        doc.customer_name = kwargs["customer_name"]
        print(doc.customer_name)  
        
        for data in kwargs["purchase_reciept_item_ct"]:
            
            invoice_child = doc.append("purchase_reciept_item_ct",{})
            print(invoice_child)
            invoice_child.item_code = make_autoname(data["item_code"] +"-.#",invoice_child)
            print(invoice_child.item_code)
            # invoice_child.item_code = data["item_code"]
            invoice_child.item_name = data["item_name"]
        doc.save()    
        return success_response(data=doc)
        print("success")
   
    except Exception as e:
        frappe.logger("Token").exception(e)
        return error_response(e)