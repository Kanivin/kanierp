# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# MIT License. See license.txt


import frappe


def execute():
	frappe.reload_doc("accounts", "doctype", "Payment Schedule")
	if frappe.db.count("Payment Schedule"):
		frappe.db.sql(
			"""
			UPDATE
				`tabPayment Schedule` ps
			SET
				ps.outstanding = (ps.payment_amount - ps.paid_amount)
		"""
		)
