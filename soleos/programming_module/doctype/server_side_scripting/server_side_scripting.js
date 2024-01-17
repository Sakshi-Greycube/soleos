// Copyright (c) 2024, GreyCube Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Server Side Scripting', {
// 	enable: function(frm){
// 		frm.call({
// 			doc: frm.doc,
// 			method: 'frm_call',
// 			args: {
// 				msg: "Hello"
// 			},
// 			freeze: true,
// 			freeze_message:__('Calling frm_call Method'),
// 			callback: function(r){
// 				//frappe.msgprint(r.message)

// 				//frappe.msgprint("Server Side calling Completed")

// 				//frm.refresh_field('medication_orders');
// 			}
// 		});
// 	}
// });


////////  frappe_call()   //////////////

frappe.ui.form.on('Server Side Scripting', {
	enable: function(frm){
		frappe.call({
			method: 'soleos.programming_module.doctype.client_side_scripting.client_side_scripting.frappe_call',
			args: {
				//name: frm.doc.name,
				client: frm.doc.client_side_doc
			},
			freeze: true,
			freeze_message:__('Calling frappe_call Method'),
			callback: function(r){
				frappe.msgprint(r.message)
				console.log(r)

				//frappe.msgprint("Server Side calling Completed")

				//frm.refresh_field('medication_orders');
			}
		});
	}
});
