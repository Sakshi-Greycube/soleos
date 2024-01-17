# Copyright (c) 2024, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):
    pass

### Server Side Events ###	
	
	# def validate(self):
	# 	frappe.msgprint("Hello Frappe!!1")
		
	# def before_save(self):
	# 	frappe.throw("Hello Frappe from 'before_save' Event")
	# 	print('_' *100)

	# def before_insert(self):
	# 	frappe.throw("Hello Frappe from 'before_insert' Event")

	# def after_insert(self):
	# 	frappe.throw("Hello Frappe from 'after_insert' Event")

	# def on_update(self):
	# 	frappe.msgprint("Hello Frappe from 'on_update' Event")
	
	# def before_submit(self):
	# 	frappe.msgprint("Hello Frappe from 'before_submit' Event")
		
	# def on_submit(self):
	# 	frappe.msgprint("Hello Frappe 'on_submit' Event")
			
	# def on_cancel(self):
	# 	frappe.msgprint("Hello Frappe 'on_cancel' Event")
		 
	# def on_trash(self):
	# 	frappe.msgprint("Hello Frappe 'on_transh' Event")

	# def after_delete(self):
	# 	frappe.msgprint("Hello Frappe 'after_delete' Event")

### Value fetching ###

	# def validate(self):
	# 	frappe.msgprint(_("Hello My Full Name is '{0}' ").format(
	# 		self.first_name +" "+ self.middle_name +" "+ self.last_name))
	# 	for row in self.get("family_member"):
	# 		frappe.msgprint(_(
	# 			"{0}, The Family member name is '{1}' and relation is'{2}' ").format(
	# 				row.idx,row.name1,row.relation))		 



	# def validate(self):
	# 	self.new_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(_("The First Name {0} is and Age is {1}").format(doc.first_name, doc.age))
		
	# 	for row in doc.get("family_member"):
	# 	  frappe.msgprint(_(
	# 		"{0}. The family member name is '{1}' and relation is '{2}'").format(
	# 			row.idx,row.name1,row.relation))

### new_doc & delete_doc() ### 
	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Jake'
	# 	doc.last_name = 'Jay'
	# 	doc.age = 13

	# 	doc.append("family_member",{  "name1": "Jain",
	# 								   "relation": "Sister",
	# 								   "age": 14
	# 								})
	# 	doc.insert()

	

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR0003')	


	################## insert document ############
	
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = "Bally"
	# 	doc.age = 67
	# 	doc.insert()

# Some escape hatches that can be used to skip certain checks
		# doc.insert(
		# 	ignore_permissions = True    # ignore write permission during insert 
		# 	ignore_links = True          # ignore link validation in the document
		# 	ignore_if_duplicate = True   # don't insert if DuplicateEntryError is throw
		# 	ignore_mandatory = True      # insert even if mandatory field are not set
		# )

	######   save document   ######
		
	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = "Dany"
	# 	doc.age = 21
	# 	doc.save()

	# doc.save(
	# 	ignore_permissions=True,  # ignore write permissions during insert
	# 	ignore_version=True   # do not create a version records
	# )
	
	###### delete document ######
	
	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'PR0009')
	# 	doc.delete()

	# ###### doc.db_set() -> set value in document ######


	# def validate(self):
	# 	self.db_self_document()

	# def db_self_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'PR0010')
	# 	doc.db_set('age', 23)	

	# frappe.db.get_list(doctype, filters, or_filters, order_by, fields, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 					   filters={
	# 						   'enable':1
	# 					   },
	# 					   fields=['first_name', 'age'])
	# 	for d in doc:
	# 		frappe.msgprint(_("The parent first name is {0} and age is {1}").format(d.first_name,d.age))

###### get_value & set_value #######
	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR0010', ['first_name', 'age'])
	# 	frappe.msgprint(_("The parent first name is {0} and age is {1}").format(first_name,age))
	
	# def validate(self):
	# 	frappe.db.set_value('Client Side Scripting', 'PR0010', 'age', 12)

	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR0010', ['first_name', 'age'])
	# 	frappe.msgprint(_("The parent first name is {0} and age is {1}").format(first_name,age))

###### exists() & count() ######
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting', 'PR0027'): #True
	# 		frappe.msgprint(_("The Document is Exists in Database"))
	# 	else:
	# 		frappe.msgprint(_("The Document does not Exists in Database"))

	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting', {'enable':1})  # True
	# 	frappe.msgprint(_("The Enable Document Count is {0}").format(doc_count))
	
	# frappe.db.sql(query,filters,as_dict)

	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data = frappe.db.sql("""
	# 				   SELECT 
	# 				   		first_name,
	# 				   		age
	# 				   FROM
	# 				   		`tabClient Side Scripting`
	# 				   WHERE
	# 				   		enable = 1
	# 				   	""", as_dict= 1)
		
	# 	for d in data:
	# 		frappe.msgprint(_("The parent first name is {0} and age is {1}").format(d.first_name,d.age))

##### Server Side Calls ######
	
	#### frm.call() ####
	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	# frappe.msgprint(msg)
		
	# 	self.mob_no= 987654321
				
	# 	# return "Hi This Message from frm_call"

# @frappe.whitelist()
# def frappe_call(name):
# 	# import time
# 	# time.sleep(5)
# 	# frappe.msgprint(name)
	
# 	doc = frappe.get_doc('Server Side Scripting', name)
# 	frappe.msgprint(_("The First Name {0} is and Age is {1}").format(doc.first_name, doc.age))
		

# 	# doc = frappe.get_doc(name)
# 	# frappe.msgprint(doc.first_name)
		
# 	# self.mob_no= 987654321
			
# 	return "Hi This Message from frappe_call"
	

