# Copyright (c) 2024, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

@frappe.whitelist()
def frappe_call(client):
	# import time
	# time.sleep(5)
	# frappe.msgprint(name)
	
	# doc = frappe.get_doc('Server Side Scripting', name)
	# frappe.msgprint(_("The First Name {0} is and Age is {1}").format(doc.first_name, doc.age))
		
	doc = frappe.get_doc('Client Side Scripting', client)
	frappe.msgprint(_("The First Name {0} is and Age is {1}").format(doc.first_name, doc.age))
		
	# self.mob_no= 987654321
			
	return "Hi This Message from frappe_call"
	
