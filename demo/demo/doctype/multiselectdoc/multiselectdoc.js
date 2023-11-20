// Copyright (c) 2023, manoj and contributors
// For license information, please see license.txt
frappe.ui.form.on('Multiselectdoc', {
    refresh: function(frm) {
        frm.add_custom_button(__('Customer Approval'), function() {
            var d = new frappe.ui.form.MultiSelectDialog({
                doctype: "Custom MultiSelect Form",
                target: frm,
                setters: {
                    form: null,
                },
                add_filters_group: 1,
                allow_child_item_selection: 1,
                child_fieldname: "custom_item_child_table",
                child_columns: ["item_name", "total_price"],
                get_query() {
                    return {
                        filters: { docstatus: ['!=', 2] }
                    };
                },

                action(selections, args) {
                    console.log(selections, args);
                    args.filtered_children.forEach(data => {
                        frappe.call({
                            method: "demo.demo.doctype.multiselectdoc.multiselectdoc.multiselect_fuc",
                            args: {
                                key: data
                            },
                            callback: (response) => {
                                var child_row = frm.add_child(
                                    'item_child_table',
                                    {
                                        item_name: response.message["item_name"],
                                        total_price: response.message.total_price,
                                        gst_amount: response.message.gst_applied
                                    }
                                );
                                frm.refresh_field("item_child_table");
                            }
                        });
                    });
                }
            });
        });
    }
});



