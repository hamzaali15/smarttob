import frappe
from frappe import _

def calculate_costing(self, method):
	self.total_cost = self.operating_cost + self.raw_material_cost + self.scrap_material_cost + self.electricity_cost + self.rent_cost + self.consumable_cost + self.wages
	self.flags.ignore_validate_update_after_submit = True
	self.db_update()
	# self.save(ignore_permissions=True)