# # Copyright (c) 2026, Sukku and contributors
# # For license information, please see license.txt

# import frappe
# from frappe import _
# from frappe.utils import flt


# def execute(filters=None):
# 	filters = filters or {}
# 	columns = get_columns()
# 	data    = get_data(filters)
# 	return columns, data


# def get_columns():
# 	return [
# 		{
# 			"label":     _("Customer"),
# 			"fieldname": "customer",
# 			"fieldtype": "Link",
# 			"options":   "Customer",
# 			"width":     150,
# 		},
# 		{
# 			"label":     _("Customer Name"),
# 			"fieldname": "customer_name",
# 			"fieldtype": "Data",
# 			"width":     200,
# 		},
# 		{
# 			"label":     _("Sales Person"),
# 			"fieldname": "sales_person",
# 			"fieldtype": "Link",
# 			"options":   "Sales Person",
# 			"width":     160,
# 		},
# 		{
# 			"label":     _("Total Target"),
# 			"fieldname": "total_target",
# 			"fieldtype": "Currency",
# 			"width":     140,
# 		},
# 		{
# 			"label":     _("Total Achieved"),
# 			"fieldname": "total_achieved",
# 			"fieldtype": "Currency",
# 			"width":     140,
# 		},
# 		{
# 			"label":     _("Total Balance"),
# 			"fieldname": "total_balance",
# 			"fieldtype": "Currency",
# 			"width":     140,
# 		},
# 		{
# 			"label":     _("Achievement %"),
# 			"fieldname": "achievement_percent",
# 			"fieldtype": "Percent",
# 			"width":     130,
# 		},
# 	]


# def get_data(filters):
# 	customer      = filters.get("customer", "")
# 	customer_name = filters.get("customer_name", "")

# 	parent_conditions = {"docstatus": ["<", 2]}
# 	if customer:
# 		parent_conditions["name"] = customer

# 	parents = frappe.get_all(
# 		"Sales Person Target",
# 		filters=parent_conditions,
# 		fields=["name", "total_target", "total_achieved", "total_balance", "achievement_percent"],
# 	)

# 	if not parents:
# 		return []

# 	result         = []
# 	grand_target   = 0.0
# 	grand_achieved = 0.0

# 	for parent in parents:
# 		cust_code = parent.name
# 		cust_name = frappe.db.get_value("Customer", cust_code, "customer_name") or cust_code

# 		if customer_name and customer_name.lower() not in cust_name.lower():
# 			continue

# 		child_rows = frappe.get_all(
# 			"Yearly Target Detail",
# 			filters={"parent": cust_code},
# 			fields=["sales_person", "target_amount", "achieved_amount"],
# 		)

# 		if not child_rows:
# 			target   = flt(parent.total_target)
# 			achieved = flt(parent.total_achieved)
# 			balance  = flt(parent.total_balance)
# 			pct      = flt(parent.achievement_percent)

# 			result.append({
# 				"customer":            cust_code,
# 				"customer_name":       cust_name,
# 				"sales_person":        "",
# 				"total_target":        target,
# 				"total_achieved":      achieved,
# 				"total_balance":       balance,
# 				"achievement_percent": pct,
# 				"is_total_row":        0,
# 			})
# 			grand_target   += target
# 			grand_achieved += achieved

# 		else:
# 			for child in child_rows:
# 				target   = flt(child.target_amount)
# 				achieved = flt(child.achieved_amount)
# 				balance  = target - achieved
# 				pct      = round((achieved / target * 100), 2) if target else 0.0

# 				result.append({
# 					"customer":            cust_code,
# 					"customer_name":       cust_name,
# 					"sales_person":        child.sales_person,
# 					"total_target":        target,
# 					"total_achieved":      achieved,
# 					"total_balance":       balance,
# 					"achievement_percent": pct,
# 					"is_total_row":        0,
# 				})
# 				grand_target   += target
# 				grand_achieved += achieved

# 	result.sort(key=lambda x: (x["customer_name"], x["sales_person"] or ""))

# 	if result:
# 		grand_balance = grand_target - grand_achieved
# 		grand_pct     = round((grand_achieved / grand_target * 100), 2) if grand_target else 0.0

# 		result.append({
# 			"customer":            "",
# 			"customer_name":       "Total",
# 			"sales_person":        "",
# 			"total_target":        grand_target,
# 			"total_achieved":      grand_achieved,
# 			"total_balance":       grand_balance,
# 			"achievement_percent": grand_pct,
# 			"is_total_row":        1,
# 		})

# 	return result






# # Copyright (c) 2026, Sukku and contributors
# # For license information, please see license.txt

# import frappe
# from frappe import _
# from frappe.utils import flt


# def execute(filters=None):
# 	filters = filters or {}
# 	columns = get_columns()
# 	data    = get_data(filters)
# 	return columns, data


# def get_columns():
# 	return [
# 		{
# 			"label":     _("Customer"),
# 			"fieldname": "customer",
# 			"fieldtype": "Link",
# 			"options":   "Customer",
# 			"width":     150,
# 		},
# 		{
# 			"label":     _("Customer Name"),
# 			"fieldname": "customer_name",
# 			"fieldtype": "Data",
# 			"width":     200,
# 		},
# 		{
# 			"label":     _("Sales Person"),
# 			"fieldname": "sales_person",
# 			"fieldtype": "Link",
# 			"options":   "Sales Person",
# 			"width":     160,
# 		},
# 		{
# 			"label":     _("Last Year Target"),
# 			"fieldname": "last_year_target",
# 			"fieldtype": "Currency",
# 			"width":     150,
# 		},
# 		{
# 			"label":     _("Last Year Achievement"),
# 			"fieldname": "last_year_achievement",
# 			"fieldtype": "Currency",
# 			"width":     170,
# 		},
# 		{
# 			"label":     _("Contribution (%)"),
# 			"fieldname": "contribution_",
# 			"fieldtype": "Percent",
# 			"width":     140,
# 		},
# 		{
# 			"label":     _("Current Year Target"),
# 			"fieldname": "current_year_target",
# 			"fieldtype": "Currency",
# 			"width":     160,
# 		},
# 		{
# 			"label":     _("Total Achieved"),
# 			"fieldname": "total_achieved",
# 			"fieldtype": "Currency",
# 			"width":     140,
# 		},
# 		{
# 			"label":     _("Achievement %"),
# 			"fieldname": "achievement_percent",
# 			"fieldtype": "Percent",
# 			"width":     130,
# 		},
# 	]


# def get_data(filters):
# 	customer      = filters.get("customer", "")
# 	sales_person  = filters.get("sales_person", "")
# 	fiscal_year   = filters.get("fiscal_year") or _get_fiscal_year()

# 	# Get fiscal year date range
# 	fy_dates = frappe.db.get_value(
# 		"Fiscal Year", fiscal_year, ["year_start_date", "year_end_date"], as_dict=True
# 	)
# 	if not fy_dates:
# 		return []

# 	fy_start = fy_dates.year_start_date
# 	fy_end   = fy_dates.year_end_date

# 	parent_conditions = {"docstatus": ["<", 2]}
# 	if customer:
# 		parent_conditions["name"] = customer

# 	parents = frappe.get_all(
# 		"Sales Person Target",
# 		filters=parent_conditions,
# 		fields=["name"],
# 	)

# 	if not parents:
# 		return []

# 	result                 = []
# 	grand_last_yr_target   = 0.0
# 	grand_last_yr_achieved = 0.0
# 	grand_contribution     = 0.0
# 	grand_curr_yr_target   = 0.0
# 	grand_total_achieved   = 0.0

# 	for parent in parents:
# 		cust_code = parent.name
# 		cust_name = frappe.db.get_value("Customer", cust_code, "customer_name") or cust_code

# 		# Get child rows filtered by sales_person if provided
# 		child_filters = {"parent": cust_code}
# 		if sales_person:
# 			child_filters["sales_person"] = sales_person

# 		child_rows = frappe.get_all(
# 			"Yearly Target Detail",
# 			filters=child_filters,
# 			fields=[
# 				"sales_person",
# 				"target_amount",
# 				"achieved_amount",
# 				"contribution_",
# 				"current_year",
# 			],
# 		)

# 		if not child_rows:
# 			continue

# 		for child in child_rows:
# 			sp               = child.sales_person
# 			last_yr_target   = flt(child.target_amount)
# 			last_yr_achieved = flt(child.achieved_amount)
# 			contribution     = flt(child.contribution_)
# 			curr_yr_target   = flt(child.current_year)

# 			# Total Achieved: sum allocated_amount from Sales Invoice Team
# 			# where sales_person matches and customer matches and invoice is submitted
# 			# within fiscal year date range
# 			total_achieved = _get_sales_invoice_achieved(
# 				cust_code, sp, fy_start, fy_end
# 			)

# 			# Achievement % = (Total Achieved / Current Year Target) * 100
# 			pct = round((total_achieved / curr_yr_target * 100), 2) if curr_yr_target else 0.0

# 			result.append({
# 				"customer":              cust_code,
# 				"customer_name":         cust_name,
# 				"sales_person":          sp,
# 				"last_year_target":      last_yr_target,
# 				"last_year_achievement": last_yr_achieved,
# 				"contribution_":         contribution,
# 				"current_year_target":   curr_yr_target,
# 				"total_achieved":        total_achieved,
# 				"achievement_percent":   pct,
# 				"is_total_row":          0,
# 			})

# 			grand_last_yr_target   += last_yr_target
# 			grand_last_yr_achieved += last_yr_achieved
# 			grand_contribution     += contribution
# 			grand_curr_yr_target   += curr_yr_target
# 			grand_total_achieved   += total_achieved

# 	result.sort(key=lambda x: (x["customer_name"], x["sales_person"] or ""))

# 	if result:
# 		grand_pct = round((grand_total_achieved / grand_curr_yr_target * 100), 2) if grand_curr_yr_target else 0.0

# 		result.append({
# 			"customer":              "",
# 			"customer_name":         "Total",
# 			"sales_person":          "",
# 			"last_year_target":      grand_last_yr_target,
# 			"last_year_achievement": grand_last_yr_achieved,
# 			"contribution_":         grand_contribution,
# 			"current_year_target":   grand_curr_yr_target,
# 			"total_achieved":        grand_total_achieved,
# 			"achievement_percent":   grand_pct,
# 			"is_total_row":          1,
# 		})

# 	return result


# def _get_sales_invoice_achieved(customer, sales_person, fy_start, fy_end):
# 	"""
# 	Sum allocated_amount from Sales Team child table of Sales Invoice
# 	where:
# 	  - Sales Invoice is submitted (docstatus = 1)
# 	  - Sales Invoice customer = customer
# 	  - Sales Invoice posting_date within fiscal year
# 	  - Sales Team sales_person = sales_person
# 	"""
# 	result = frappe.db.sql("""
# 		SELECT
# 			SUM(st.allocated_amount) AS total
# 		FROM
# 			`tabSales Invoice` si
# 		INNER JOIN
# 			`tabSales Team` st ON st.parent = si.name
# 		WHERE
# 			si.docstatus = 1
# 			AND si.customer = %(customer)s
# 			AND st.sales_person = %(sales_person)s
# 			AND si.posting_date BETWEEN %(fy_start)s AND %(fy_end)s
# 	""", {
# 		"customer":    customer,
# 		"sales_person": sales_person,
# 		"fy_start":    fy_start,
# 		"fy_end":      fy_end,
# 	}, as_dict=True)

# 	return flt(result[0].total) if result and result[0].total else 0.0


# def _get_fiscal_year():
# 	return (
# 		frappe.db.get_value(
# 			"Fiscal Year",
# 			{"disabled": 0},
# 			"name",
# 			order_by="year_start_date desc",
# 		)
# 		or ""
# 	)


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
			"label":     _("Last Year Target"),
			"fieldname": "last_year_target",
			"fieldtype": "Currency",
			"width":     150,
		},
		{
			"label":     _("Last Year Achievement"),
			"fieldname": "last_year_achievement",
			"fieldtype": "Currency",
			"width":     170,
		},
		{
			"label":     _("Contribution (%)"),
			"fieldname": "contribution_",
			"fieldtype": "Percent",
			"width":     140,
		},
		{
			"label":     _("Current Year Target"),
			"fieldname": "current_year_target",
			"fieldtype": "Currency",
			"width":     160,
		},
		{
			"label":     _("Total Achieved"),
			"fieldname": "total_achieved",
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
	customer     = filters.get("customer", "")
	sales_person = filters.get("sales_person", "")
	fiscal_year  = filters.get("fiscal_year") or _get_fiscal_year()

	# Get fiscal year date range
	fy_dates = frappe.db.get_value(
		"Fiscal Year", fiscal_year,
		["year_start_date", "year_end_date"],
		as_dict=True
	)
	if not fy_dates:
		return []

	fy_start = fy_dates.year_start_date
	fy_end   = fy_dates.year_end_date

	# Build parent filters
	parent_conditions = {"docstatus": ["<", 2]}
	if customer:
		parent_conditions["name"] = customer

	parents = frappe.get_all(
		"Sales Person Target",
		filters=parent_conditions,
		fields=["name"],
	)

	if not parents:
		return []

	result                 = []
	grand_last_yr_target   = 0.0
	grand_last_yr_achieved = 0.0
	grand_contribution     = 0.0
	grand_curr_yr_target   = 0.0
	grand_total_achieved   = 0.0

	for parent in parents:
		cust_code = parent.name
		cust_name = frappe.db.get_value(
			"Customer", cust_code, "customer_name"
		) or cust_code

		# Build child filters
		child_filters = {"parent": cust_code}
		if sales_person:
			child_filters["sales_person"] = sales_person

		child_rows = frappe.get_all(
			"Yearly Target Detail",
			filters=child_filters,
			fields=[
				"sales_person",
				"target_amount",
				"achieved_amount",
				"contribution_",
				"current_year",
			],
		)

		if not child_rows:
			continue

		for child in child_rows:
			sp               = child.sales_person
			last_yr_target   = flt(child.target_amount)
			last_yr_achieved = flt(child.achieved_amount)
			contribution     = flt(child.contribution_)
			curr_yr_target   = flt(child.current_year)

			# Total Achieved = SUM of allocated_amount from Sales Team
			# on SUBMITTED Sales Invoices only (docstatus=1, NOT cancelled)
			# for this exact customer + sales_person within fiscal year
			total_achieved = _get_invoice_achieved(
				cust_code, sp, fy_start, fy_end
			)

			# Achievement % = (Total Achieved / Current Year Target) * 100
			pct = (
				round((total_achieved / curr_yr_target * 100), 2)
				if curr_yr_target else 0.0
			)

			result.append({
				"customer":              cust_code,
				"customer_name":         cust_name,
				"sales_person":          sp,
				"last_year_target":      last_yr_target,
				"last_year_achievement": last_yr_achieved,
				"contribution_":         contribution,
				"current_year_target":   curr_yr_target,
				"total_achieved":        total_achieved,
				"achievement_percent":   pct,
				"is_total_row":          0,
			})

			grand_last_yr_target   += last_yr_target
			grand_last_yr_achieved += last_yr_achieved
			grand_contribution     += contribution
			grand_curr_yr_target   += curr_yr_target
			grand_total_achieved   += total_achieved

	result.sort(key=lambda x: (x["customer_name"], x["sales_person"] or ""))

	if result:
		grand_pct = (
			round((grand_total_achieved / grand_curr_yr_target * 100), 2)
			if grand_curr_yr_target else 0.0
		)
		result.append({
			"customer":              "",
			"customer_name":         "Total",
			"sales_person":          "",
			"last_year_target":      grand_last_yr_target,
			"last_year_achievement": grand_last_yr_achieved,
			"contribution_":         grand_contribution,
			"current_year_target":   grand_curr_yr_target,
			"total_achieved":        grand_total_achieved,
			"achievement_percent":   grand_pct,
			"is_total_row":          1,
		})

	return result


def _get_invoice_achieved(customer, sales_person, fy_start, fy_end):
	"""
	Sum allocated_amount from tabSales Team (child of Sales Invoice)
	WHERE:
	  - Sales Invoice docstatus = 1 (Submitted only, NOT cancelled)
	  - Sales Invoice customer  = customer
	  - Sales Team sales_person = sales_person
	  - Sales Invoice posting_date BETWEEN fy_start AND fy_end

	Example for VIBGYOR TECHNOLOGIES / Sanjeev Bharti:
	  - RPL/25-26/0073  Cancelled  → EXCLUDED (docstatus=2)
	  - 26-27/0449      Submitted  → allocated_amount ₹11,400 → INCLUDED
	  Total Achieved = ₹11,400.00
	"""
	result = frappe.db.sql("""
		SELECT
			SUM(st.allocated_amount) AS total
		FROM
			`tabSales Invoice` si
		INNER JOIN
			`tabSales Team` st ON st.parent = si.name
		WHERE
			si.docstatus   = 1
			AND si.customer       = %(customer)s
			AND st.sales_person   = %(sales_person)s
			AND si.posting_date  BETWEEN %(fy_start)s AND %(fy_end)s
	""", {
		"customer":     customer,
		"sales_person": sales_person,
		"fy_start":     fy_start,
		"fy_end":       fy_end,
	}, as_dict=True)

	return flt(result[0].total) if result and result[0].total else 0.0


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