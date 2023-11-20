// Copyright (c) 2023, manoj and contributors
// For license information, please see license.txt

frappe.ui.form.on('item child table doctype', {
	item_name : async function(frm,cdt,cdn) 
	{
	    var childtable = locals[cdt][cdn];
		console.log("iii")
		
		if (childtable.item_name == "")
		{
			console.log("pass1")
            frappe.model.set_value(cdt,cdn,"total_price",null)
            frappe.model.set_value(cdt,cdn,"gst_amount",null)
			console.log("pass2")
        }	
		else
		{	
			console.log("pass3")
			// frappe.model.set_value(cdt, cdn, "total_quantity", 11)
            var totalQuantity = 0
			
			console.log("pass3")
            var Item_details = await frappe.db.get_doc("Item pricee", childtable.item_name);
			console.log("pass3")
            var product = Item_details.item;
			console.log(Item_details)
			
            var Mydata = await frappe.db.get_list("Item Quantity",{
                fields:["item_quantity"],
                filters:{
                    "item_name_link":product
        }
	});
	Mydata.forEach(data=>{
		totalQuantity = totalQuantity + parseInt(data.item_quantity)
		// console.log(totalQuantity)
	})
	frappe.model.set_value(cdt,cdn,"total_price",totalQuantity*Item_details.item_price)
	frappe.model.set_value(cdt,cdn,"gst_applied",totalQuantity*Item_details.item_price*0.18)
	console.log("finally")
	}
	}
});
