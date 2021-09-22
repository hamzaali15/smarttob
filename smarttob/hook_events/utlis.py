import frappe
from frappe import _

@frappe.whitelist()
def cal_amount(self,method):
    self.total_custom = 0
    for row in self.items:
        self.total_custom += float(row.qty) * float(frappe.db.get_value("Item",row.item_code,"custom_rate"))