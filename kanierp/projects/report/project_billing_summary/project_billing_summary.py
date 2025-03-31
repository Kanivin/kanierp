# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe

from kanierp.projects.report.billing_summary import get_columns, get_data


def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns()

	data = get_data(filters)
	return columns, data
