import frappe,re
from demo.utils import success_response, error_response


# def validate_pan(gst_number):
#     pan_pattern = r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}$"
#     if re.match(pan_pattern,pan):
#         return True
#     return False

def user_exist_or_not(kwargs):
    print("hhhhh")
    user = frappe.get_doc("Api Acess token")
    print("user")
    data={}
    if user.username == kwargs["username"] and user.password == kwargs["password"]:
        print(user.api_access,type(user.api_access))
        data["username"] = user.username
        data["password"] = user.password
        if int(user.api_access) == 1:
            data["api_access"] = user.api_access
            data["details"] = {data["api_access"] : user.api_access}

            # try:
            #     print("hello")
            #     gst_details_userr = frappe.get_doc("GSTIN", kwargs["username"]) 
            #     # print(gst_details_userr)
            #     userr_value = gst_details_userr.userr
            #     userr_valuee = gst_details_userr.address
            #     print(userr_valuee)
            #     data["gst_details"] = {"userr": userr_value}
            #     print("2222")
            #     # print("444444")
            #     # data["gst_details"] = {"userr": gst_details_userr}
            #     # print("2222")
                 
            #     # print("2222")
            #     # # new_doc = frappe.new_doc("GST Details")
            #     # data["gst_details"]=gst_details_userr
            #     # # return gst_details
            # except:
            #     print("3")
            #     return error_response("GST Details Not found")
            
        else:
            print("user not valid")
        print(user.api_access)
        print(user.password)
        return success_response(data=data)
 
    else:
        return "Invalid Username or Password"

