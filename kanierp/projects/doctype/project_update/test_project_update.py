# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# See license.txt

import unittest

import frappe


class TestProjectUpdate(unittest.TestCase):
	pass


test_records = frappe.get_test_records("Project Update")
test_ignore = ["Sales Order"]
