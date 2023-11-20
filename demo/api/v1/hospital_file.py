import frappe
from demo.utils import success_response, error_response
def hospital_fun(kwargs):
    print("ssss")
    try:
        data={}
        doc = frappe.get_doc("Hospital","Hospital429")
        print(doc)
        doc.hospital_name = kwargs["hospital_name"]
        doc.hospital_location = kwargs["hospital_location"]
        doc.hospital_pincode = kwargs["pin"]
        for data in kwargs["hospital_employees_table_field"]:
            hospital_emp= doc.append("hospital_employees_table_field",{})
            hospital_emp.emp_id = data["emp_id"]
            print(data)
            print(hospital_emp.emp_id)
        doc.save() 
        return success_response(data=doc)
        
        
    except Exception as e:
        frappe.logger("Token").exception(e)
        return error_response(e)