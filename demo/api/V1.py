import frappe
from demo.utils import success_response, error_response
import demo.api.v1.access_token  as  access_token
import demo.api.v1.gst as gst
import demo.api.v1.itemcode as itemcode
import demo.api.v1.hospital_file as hospital_file
import demo.api.v1.api_report as api_report

class V1():
    def __init__(self):
        self.methods = {
            'access_token':['get_access_token'],
            'gst':["user_exist_or_not"],
            'itemcode':["item"],
            "hospital_file":["hospital_fun"],
            "api_report":["report_api_fun"]

        }

    def class_map(self, kwargs):
        entity = kwargs.get('entity')
        print("222")
        method = kwargs.get('method')
        print("333")
        if self.methods.get(entity):
            if method in self.methods.get(entity):
                print("222")
                function = f"{kwargs.get('entity')}.{kwargs.get('method')}({kwargs})"
                print("44")
                # print(eval(function))
                print("444")
                return eval(function)
            else:
                print("552")
                return error_response("Method Not Found!")
        else:
            return error_response("Entity Not Found!")