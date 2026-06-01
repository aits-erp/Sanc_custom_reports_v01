# Copyright (c) 2026, Sukku and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data    = get_data(filters)
	return columns, data


def get_columns():
	return [
		{
			"label":     _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options":   "Customer",
			"width":     150,
		},
		{
			"label":     _("Customer Name"),
			"fieldname": "customer_name",
			"fieldtype": "Data",
			"width":     200,
		},
		{
			"label":     _("Sales Person"),
			"fieldname": "sales_person",
			"fieldtype": "Link",
			"options":   "Sales Person",
			"width":     160,
		},
		{
			"label":     _("Total Target"),
			"fieldname": "total_target",
			"fieldtype": "Currency",
			"width":     140,
		},
		{
			"label":     _("Total Achieved"),
			"fieldname": "total_achieved",
			"fieldtype": "Currency",
			"width":     140,
		},
		{
			"label":     _("Total Balance"),
			"fieldname": "total_balance",
			"fieldtype": "Currency",
			"width":     140,
		},
		{
			"label":     _("Achievement %"),
			"fieldname": "achievement_percent",
			"fieldtype": "Percent",
			"width":     130,
		},
	]


def get_data(filters):
	customer      = filters.get("customer", "")
	customer_name = filters.get("customer_name", "")

	parent_conditions = {"docstatus": ["<", 2]}
	if customer:
		parent_conditions["name"] = customer

	parents = frappe.get_all(
		"Sales Person Target",
		filters=parent_conditions,
		fields=["name", "total_target", "total_achieved", "total_balance", "achievement_percent"],
	)

	if not parents:
		return []

	result         = []
	grand_target   = 0.0
	grand_achieved = 0.0

	for parent in parents:
		cust_code = parent.name
		cust_name = frappe.db.get_value("Customer", cust_code, "customer_name") or cust_code

		if customer_name and customer_name.lower() not in cust_name.lower():
			continue

		child_rows = frappe.get_all(
			"Yearly Target Detail",
			filters={"parent": cust_code},
			fields=["sales_person", "target_amount", "achieved_amount"],
		)

		if not child_rows:
			target   = flt(parent.total_target)
			achieved = flt(parent.total_achieved)
			balance  = flt(parent.total_balance)
			pct      = flt(parent.achievement_percent)

			result.append({
				"customer":            cust_code,
				"customer_name":       cust_name,
				"sales_person":        "",
				"total_target":        target,
				"total_achieved":      achieved,
				"total_balance":       balance,
				"achievement_percent": pct,
				"is_total_row":        0,
			})
			grand_target   += target
			grand_achieved += achieved

		else:
			for child in child_rows:
				target   = flt(child.target_amount)
				achieved = flt(child.achieved_amount)
				balance  = target - achieved
				pct      = round((achieved / target * 100), 2) if target else 0.0

				result.append({
					"customer":            cust_code,
					"customer_name":       cust_name,
					"sales_person":        child.sales_person,
					"total_target":        target,
					"total_achieved":      achieved,
					"total_balance":       balance,
					"achievement_percent": pct,
					"is_total_row":        0,
				})
				grand_target   += target
				grand_achieved += achieved

	result.sort(key=lambda x: (x["customer_name"], x["sales_person"] or ""))

	if result:
		grand_balance = grand_target - grand_achieved
		grand_pct     = round((grand_achieved / grand_target * 100), 2) if grand_target else 0.0

		result.append({
			"customer":            "",
			"customer_name":       "Total",
			"sales_person":        "",
			"total_target":        grand_target,
			"total_achieved":      grand_achieved,
			"total_balance":       grand_balance,
			"achievement_percent": grand_pct,
			"is_total_row":        1,
		})

	return result