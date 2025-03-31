# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from kanierp.selling.report.sales_partner_target_variance_based_on_item_group.item_group_wise_sales_target_variance import (
	get_data_column,
)


def execute(filters=None):
	return get_data_column(filters, "Sales Partner")
