import frappe
from demo.utils import success_response, error_response
def report_api_fun(kwargs):
    print(kwargs)
    conditions = []
    try:
        if kwargs['name1']:
            conditions.append(f"WHERE re.name1 LIKE '%%{kwargs['name1']}%%'")
    except:
        pass

    try:
        if kwargs['email']:
            conditions.append(f"{' AND ' if conditions else 'WHERE '}re.email LIKE '%%{kwargs['email']}%%'")
    except:
        pass

    try:
        if kwargs['pincode']:
            conditions.append(f"{' AND ' if conditions else 'WHERE '}re.pincode LIKE '%%{kwargs['pincode']}%%'")
    except:
        pass

    if len(conditions) == 0:
        conditions = ""

    if len(conditions) > 1:
        conditions = " ".join(conditions)

    if len(conditions) == 1:
        conditions = conditions[0]

    data = frappe.db.sql(f"""
            SELECT  
                re.name1,re.email,re.location,re.pincode,re.contact
            FROM
                `tabReport_Api` AS re {conditions}
        """,as_dict=True)
    print("data:--",data,conditions)
    return data