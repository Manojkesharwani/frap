// Copyright (c) 2023, manoj and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Valid date task', {
//     before_save: function (frm, cdt, cdn) {
//         var doc = locals[cdt][cdn];
//         if (!is_date_within_year_and_quater(doc.year, doc.quater, doc.date)) {
//             frappe.msgprint(__("Selected date is not within the specified year and quarter"));
//             frappe.validated = false; // This will prevent the document from being saved
//         }
//     }
// });

// function is_date_within_year_and_quarter(year, quarter, selected_date) {
//     // Your logic to validate if the selected date falls within the specified year and quarter
//     // Implement your own date validation logic here
//     // For example, you can use JavaScript Date object

//     // Placeholder logic (replace this with your actual logic)
//     return true;
// }
// frappe.ui.form.on('Valid date task', {
//     date: function (frm) {
//         // Assuming 'date' is your date field
//         var years = frm.doc.year
//         console.log("Selected years as string:", years);
        
//         // Extract the first character of the 'years' string
//         var from_year = years.slice(0, 4);
// 		var to_year = years.slice(-4);
//         console.log("from_year", from_year);
// 		console.log("to_year", to_year);


//         var year = frappe.datetime.str_to_user(frm.doc.date);
//         var lastFourCharacters = year.slice(-4);
        
//         if from_year = year:
// 		frappe.throw("Please select a valid year");
//     }
// });


frappe.ui.form.on('Valid date task', {
    date: function (frm) {
        // Assuming 'date' is your date field
        var years = frm.doc.year;
        console.log("Selected years as string:", years);
        
        // Extract the first 4 characters and the last 4 characters of the 'years' string
        var from_year = years.slice(0, 4);
        var to_year = years.slice(-4);
        console.log("from_year", from_year);
        console.log("to_year", to_year);

        var year = frappe.datetime.str_to_user(frm.doc.date);
        var lastFourCharacters = year.slice(-4);
        
        // Compare if the extracted year from 'date' is within the range of 'years'
        if (from_year !== lastFourCharacters ) {
            frappe.msgprint("Please select a valid year");
            frappe.validated = false; // Prevent the document from being saved
        }
    }
});
