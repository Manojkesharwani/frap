// Copyright (c) 2023, manoj and contributors
// For license information, please see license.txt


// frappe.ui.form.on('Companys', {
//     surname:function(frm){
//         console.log(frm.doc.name1);
//         console.log(frm.doc.surname);
//         frm.set_value("full_data",frm.doc.name1+" "+frm.doc.surname);
// 		console.log(frm.doc.full_data);
//     }
// });


// frappe.ui.form.on('Companys', {
//     surname:function(frm){
//         console.log(frm.doc.name1);
//         console.log(frm.doc.surname);
//         frm.set_value("full_data",frm.doc.name1+" "+frm.doc.surname);
//     },
//     after_save:function(frm,cdt,cdn){
//         var child = locals[cdt][cdn]
//         var row = frappe.model.add_child(frm.doc,"Company Child Table","company_table");
//         row.first_name = frm.doc.name1
//         row.last_name = frm.doc.surname
//         row.full_name = frm.doc.full_data
//         refresh_field("company_table");
//     }
// });
