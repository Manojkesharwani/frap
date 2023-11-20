frappe.ui.form.on('Dailyy', {
    refresh:function(frm){
        let popup = new frappe.ui.Dialog({
            title:"Enter Your Details",
            fields: [
                {
                    label : "first_name",
                    fieldname : "first_name",
                    fieldtype : "Data",
 
                }
            ],
            size:'small',
            primary_action_label:"Submit",
            primary_action(values){
                console.log(values)
               frm.set_value("first_name", values.first_name);
                popup.hide();
            }
        })
            popup.show();
    }
});