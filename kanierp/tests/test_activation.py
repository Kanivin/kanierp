from frappe.tests.utils import KanivinTestCase

from kanierp.utilities.activation import get_level


class TestActivation(KanivinTestCase):
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
