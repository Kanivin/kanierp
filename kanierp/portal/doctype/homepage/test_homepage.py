# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# See license.txt

import unittest

import frappe
from frappe.utils import set_request
from frappe.website.serve import get_response


class TestHomepage(unittest.TestCase):
	def test_homepage_load(self):
		set_request(method="GET", path="home")
		response = get_response()

		self.assertEqual(response.status_code, 200)

		html = frappe.safe_decode(response.get_data())
		self.assertTrue('<section class="hero-section' in html)
