# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProcessPaymentReconciliationLogAllocations(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allocated_amount: DF.Currency
		amount: DF.Currency
		currency: DF.Link | None
		difference_account: DF.Link | None
		difference_amount: DF.Currency
		exchange_rate: DF.Float
		gain_loss_posting_date: DF.Date | None
		invoice_number: DF.DynamicLink
		invoice_type: DF.Link
		is_advance: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reconciled: DF.Check
		reference_name: DF.DynamicLink
		reference_row: DF.Data | None
		reference_type: DF.Link
		unreconciled_amount: DF.Currency
	# end: auto-generated types

	pass
