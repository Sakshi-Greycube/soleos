// Copyright (c) 2024, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {

	//this is event trigger when refresh page
	// refresh: function(frm) {
    //  frappe.msgprint("Hello Soleos from 'refresh' event");
	// 	// alert("Hello Soleos from 'refresh' event")
	// 	console.log("I`m Refreshed!!")
	// }

	//this event trigger when we load the page
	// onload: function(frm){
	// 	frappe.msgprint("Hello Soleos from 'onload' event");
	// 	console.log("I`m Reloaded!!")
	// }
		
	// validate: function(frm){
	// 	if(frm.doc.age < 18){
	// 		frappe.throw("You Are not Allowed to fill the form");
	// 		frappe.validate = false;
	// 	}
	// 	else{
	// 		frappe.msgprint("You are Allowed to fill the form");
	// 	}
	// }
	
	//this event trigger before saving the document, it`s throwing the error..not save the doc.
	// before_save: function(frm){
	// 	frappe.throw("Hello Soleos from 'before_save' event");
	// }

	//this event trigger after saving the document
	// after_save: function(frm){
	// 	frappe.throw("Hello Soleos from 'after_save' event");
	// }

	//field base triggering

	//this event trigger when status of enable field is change
	// enable: function(frm){
	// 	frappe.msgprint("Hello Soleos from 'enable' filename event");
	// }

	//this event trigger when status of age field is change
	// age: function(frm){
	// 	frappe.msgprint("Hello Soleos from 'age' filename event");
	// }

	// family_member_on_form_rendered: function(frm){
	// 	frappe.msgprint("Hello Soleos from 'family_memeber' child table rendered event");
	// }

	// before_submit: function(frm){
	// 	frappe.throw("Hello Soleos from 'before_submit' event");
	// }

	// on_submit: function(frm){
	// 	frappe.throw("Hello Soleos from 'on_submit' event");
	// }

	// before_cancel: function(frm){
	// 	frappe.throw("Hello Soleos from 'before_cancel' event");
	// }

	// after_cancel: function(frm){
	// 	frappe.throw("Hello Soleos from 'after_cancel' event");
	// }

	/* validate field:
	   -throw error when first_name is empty
	   -throw error when age is less than 18*/

	// validate: function(frm){
	// 	if(frm.doc.first_name == undefined){
	// 	frappe.throw("First Name Must Be not Empty!!");
	// 	frappe.validate = false;
	// 	}
	// 	if(frm.doc.age < 18){
	// 		frappe.throw("You Are not Allowed to fill the form");
	// 		frappe.validate = false;
	// 	}
	// 	else{
	// 		frappe.msgprint("You are Allowed to fill the form");
	// 		frappe.validate = true;
	// 	}
	// }

	//fetching values
	//frm.doc.first_name

	// after_save: function(frm){
	// 	frappe.msgprint(__("The full name is '{0}'", 
	// 	[frm.doc.first_name +" "+ frm.doc.middle_name+" "+ frm.doc.last_name]));

	// for(let row of frm.doc.family_member){
	// 	frappe.msgprint(__("{0}, The Family Member Name is '{1}' and relation is '{2}'", 
	// 	        [row.idx, row.name1, row.relation]))
	// 	}
	// }

	onload: function(frm){
		frm.set_value('current_user',frappe.boot.user.name);
	}

	//frm.set_intro & frm.is_new()
	// refresh: function(frm){

	// 	frm.set_intro('You Are In Client Side Scripting');

		//msg show only when create a new site
		// if(frm.is_new()){
		// 	frm.set_intro('Now, You can create a new Client Side Scripting Doctype');
		// }
	// }

	//frm.set_value

	// validate: function(frm){
	// 	frm.set_value('full_name',frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name)
	
	// 	let row = frm.add_child('family_member',{
	// 		name1: "Johnson jose",
	// 		relation: "Father",
	// 		age: 47,
	// 	})
	// }

	//set-up doc field property
	//frm.set_df_property('field_name', diff_doc_property, value of doc_field)

// enable:function(frm){	

// 	frm.set_df_property('first_name','reqd',1);    //reqd -> keyword to set field ad mandetory
//  //when you click on enable field first_name become mandetory

//     frm.set_df_property('middle_name','read_only',1);

// 	frm.toggle_reqd('age',true);
// }

//Button
// refresh:function(frm){
// 	// frm.add_custom_button('Click Me Button',() =>{
// 	// 	frappe.msgprint(__('You Clicked Me!!'));
// 	// })

// 	frm.add_custom_button('Click Me1',() =>{

// 		frappe.msgprint(__('You Clicked 1!!'))
// 	}, 'click me')

// 	frm.add_custom_button('Click Me2',() =>{

// 		frappe.msgprint(__('You Clicked 2!!'))
// 	}, 'click me')

// }

 });


//Child Table Scripts:

frappe.ui.form.on('Family Members',{
	//cdt(child doctype name i.e Family Member)
	//cdn is the row name

	// name1: function(frm, cdt, cdn){
	// 	frappe.msgprint("Hello from child DocType 'name1' event")
    //     console.log("Name is Added!");
	// },

	// relation(frm, cdt, cdn){
	// 	frappe.msgprint("Hello from child DocType 'relation' event")
    //     console.log("Relation is Added")
	// },

	// age: function(frm, cdt, cdn){
	// 	frappe.msgprint("Hello from child DocType 'age' event")
	// 	console.log("Age is Added")
	// },

	//This Event Trigger When Click On add row field
	family_member_add: function(frm, cdt, cdn){
		let row = locals[cdt][cdn];
		frappe.msgprint(__("{0}, is added!!", [row.idx]));
		console.log(row.idx + " Row added!!")
	}
})