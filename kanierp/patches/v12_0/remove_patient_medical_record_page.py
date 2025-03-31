# Copyright (c) 2025


import frappe


def execute():
	frappe.delete_doc("Page", "medical_record")
