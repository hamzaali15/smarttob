import frappe
from frappe import _

def calculate_costing(self, method):
	self.total_cost = self.operating_cost + self.raw_material_cost + self.scrap_material_cost + self.electricity_cost + self.rent_cost + self.consumable_cost + self.wages
	self.indirect_total_cost = self.electricity_cost + self.rent_cost + self.consumable_cost + self.wages
	self.flags.ignore_validate_update_after_submit = True
	self.db_update()
	# self.save(ignore_permissions=True)

def add_expense_account(self, method):
	if self.get('__islocal'):
	# if not self.name:
		if self.stock_entry_type == "Manufacture":
			if self.from_bom == 1:
				# doc_name = frappe.get_value('Work Order', self.bom_no, 'name')
				indirect_total_cost = frappe.db.get_value("Work Order", self.work_order, 'indirect_total_cost')
				smart_settings = frappe.get_single('SMART Settings')
				if not smart_settings.expense_account:
					frappe.throw("Please Set Expense Account in SMART Settings")
				if indirect_total_cost:
					self.append('additional_costs', {
						'expense_account': smart_settings.expense_account,
						'description': "Overheads Cost",
						'amount': indirect_total_cost
						})
					self.total_additional_costs += indirect_total_cost