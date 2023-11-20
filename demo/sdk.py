import frappe
from demo.utils import success_response, error_response
from demo.api.V1 import V1
import time
@frappe.whitelist(allow_guest=True)
def api(**kwargs):
    try:
        print("1")
        st = time.time()
        print("2")
        version = kwargs.get('version')
        print("3")
        if version == "v1":
            print("4")
            api = V1()
        elif version =="v2":
            api = V2()

        response = api.class_map(kwargs)
        print("5")
        et = time.time()
        if type(response) == dict:
            print("6")
            response['exec_time'] = f"{round(et - st, 4)} seconds"
            print("7")
        return response
    except Exception as e:
        print("8...")
        frappe.logger("registration").exception(e)
        return error_response(e)