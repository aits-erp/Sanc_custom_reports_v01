# Copyright (c) 2026, Sukku and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data    = get_data(filters)
	return columns, data


# ── Columns ────────────────────────────────────────────────────────────────────
def get_columns():
	return [
		# 1. Customer Code
		{
			"label":     _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options":   "Customer",
			"width":     150,
		},
		# 2. Customer Name
		{
			"label":     _("Customer Name"),
			"fieldname": "customer_name",
			"fieldtype": "Data",
			"width":     200,
		},
		# 3. Sales Person
		{
			"label":     _("Sales Person"),
			"fieldname": "sales_person",
			"fieldtype": "Link",
			"options":   "Sales Person",
			"width":     160,
		},
		# 4. Total Target
		{
			"label":     _("Total Target"),
			"fieldname": "total_target",
			"fieldtype": "Currency",
			"width":     140,
		},
		# 5. Total Achieved
		{
			"label":     _("Total Achieved"),
			"fieldname": "total_achieved",
			"fieldtype": "Currency",
			"width":     140,
		},
		# 6. Total Balance
		{
			"label":     _("Total Balance"),
			"fieldname": "total_balance",
			"fieldtype": "Currency",
			"width":     140,
		},
		# 7. Achievement %
		{
			"label":     _("Achievement %"),
			"fieldname": "achievement_percent",
			"fieldtype": "Percent",
			"width":     130,
		},
	]


# ── Data ───────────────────────────────────────────────────────────────────────
def get_data(filters):
	customer      = filters.get("customer", "")
	customer_name = filters.get("customer_name", "")
	period_type   = filters.get("period_type", "Yearly")
	fiscal_year   = filters.get("fiscal_year") or _get_fiscal_year()

	# Child doctype depends on Period Type
	child_map = {
		"Yearly":    "Yearly Target Detail",
		"Quarterly": "Quarterly Target Detail",
		"Monthly":   "Monthly Target Detail",
	}
	child_doctype = child_map.get(period_type, "Yearly Target Detail")

	# ── Build WHERE clause ────────────────────────────────────────────────────
	conditions = ["spt.fiscal_year = %(fiscal_year)s", "spt.docstatus < 2"]
	params     = {"fiscal_year": fiscal_year}

	if customer:
		conditions.append("spt.customer = %(customer)s")
		params["customer"] = customer

	if customer_name:
		conditions.append("cust.customer_name LIKE %(customer_name)s")
		params["customer_name"] = f"%{customer_name}%"

	where = " AND ".join(conditions)

	sql = f"""
		SELECT
			spt.customer                                  AS customer,
			COALESCE(cust.customer_name, spt.customer)   AS customer_name,
			child.sales_person                            AS sales_person,
			SUM(COALESCE(child.target_amount,   0))      AS total_target,
			SUM(COALESCE(child.achieved_amount, 0))      AS total_achieved
		FROM
			`tabSales Person Target`  spt
		INNER JOIN
			`tab{child_doctype}` child ON child.parent = spt.name
		LEFT JOIN
			`tabCustomer` cust ON cust.name = spt.customer
		WHERE
			{where}
		GROUP BY
			spt.customer,
			child.sales_person
		ORDER BY
			cust.customer_name,
			child.sales_person
	"""

	try:
		rows = frappe.db.sql(sql, params, as_dict=True)
	except Exception:
		frappe.log_error(frappe.get_traceback(), "Sales Person Target Report")
		return []

	result         = []
	grand_target   = 0.0
	grand_achieved = 0.0

	for row in rows:
		target   = flt(row.total_target)
		achieved = flt(row.total_achieved)
		balance  = target - achieved
		pct      = round((achieved / target * 100), 2) if target else 0.0

		result.append({
			"customer":            row.customer,
			"customer_name":       row.customer_name,
			"sales_person":        row.sales_person,
			"total_target":        target,
			"total_achieved":      achieved,
			"total_balance":       balance,
			"achievement_percent": pct,
			"is_total_row":        0,
		})

		grand_target   += target
		grand_achieved += achieved

	# ── Grand Total row ───────────────────────────────────────────────────────
	if result:
		grand_balance = grand_target - grand_achieved
		grand_pct     = round((grand_achieved / grand_target * 100), 2) if grand_target else 0.0

		result.append({
			"customer":            "",
			"customer_name":       "Grand Total",
			"sales_person":        "",
			"total_target":        grand_target,
			"total_achieved":      grand_achieved,
			"total_balance":       grand_balance,
			"achievement_percent": grand_pct,
			"is_total_row":        1,
		})

	return result


# ── Helper ─────────────────────────────────────────────────────────────────────
def _get_fiscal_year():
	return (
		frappe.db.get_value(
			"Fiscal Year",
			{"disabled": 0},
			"name",
			order_by="year_start_date desc",
		)
		or ""
	)