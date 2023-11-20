# Copyright (c) 2023, manoj and contributors
# For license information, please see license.txt

import frappe
def execute(filters=None):
    columns = [
        {
            "fieldname":"item",
            "label":"Furniture Item",
            "fieldtype":"Data",
            "width": 150
        }
    ]
    data = [{"item":"Chair"},{"item":"Bat"},{"item":"Bed"}]
    return columns, data