# Copyright (c) 2025, Kanivin and Contributors
# License: GNU General Public License v3. See license.txt

import frappe

from kanierp.regional.united_arab_emirates.setup import setup


def execute():
	company = frappe.get_all("Company", filters={"country": "United Arab Emirates"})
	if not company:
		return

	frappe.reload_doc("regional", "report", "uae_vat_201")
	frappe.reload_doc("regional", "doctype", "uae_vat_settings")
	frappe.reload_doc("regional", "doctype", "uae_vat_account")

	setup()
