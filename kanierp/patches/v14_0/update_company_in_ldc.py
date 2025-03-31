# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


import frappe

from kanierp import get_default_company


def execute():
	company = get_default_company()
	if company:
		for d in frappe.get_all("Lower Deduction Certificate", pluck="name"):
			frappe.db.set_value("Lower Deduction Certificate", d, "company", company, update_modified=False)
