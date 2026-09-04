# import frappe
# from frappe import _
# from frappe.utils import cstr, formatdate


# def execute(filters=None):
# 	filters = filters or {}
# 	columns = get_columns()
# 	data = get_data(filters)
# 	return columns, data


# def get_columns():
# 	"""
# 	The 4 'Blank' spacer columns required by the RBI_ADAPTER_2022.xlsx
# 	format are shown again as real (currently empty) columns, in the
# 	exact positions the bank template expects:
# 		- 2 blanks right after Beneficiary Name
# 		- 1 blank right after Payment Details 7
# 		- 1 blank right after Transaction Date

# 	Transaction Type is a manually selectable field (Select fieldtype,
# 	editable in the report grid) with options I / N / R / M. It is
# 	pre-filled from Salary Slip.custom_transaction_type as a default,
# 	but can be changed by hand per row directly in the report.
# 	"""
# 	return [
# 		{
# 			"label": _("Transaction Type"),
# 			"fieldname": "transaction_type",
# 			"fieldtype": "Select",
# 			"options": "\nI\nN\nR\nM",
# 			"width": 110,
# 			"editable": 1,
# 		},
# 		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
# 		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
# 		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
# 		{"label": _("Blank"), "fieldname": "blank_1", "fieldtype": "Data", "width": 80},
# 		{"label": _("Blank"), "fieldname": "blank_2", "fieldtype": "Data", "width": 80},

# Copyright (c) 2026, Sukku and contributors
# For license information, please see license.txt


# import frappe
# from frappe import _
# from frappe.utils import cstr, formatdate


# def execute(filters=None):
# 	filters = filters or {}
# 	columns = get_columns()
# 	data = get_data(filters)
# 	return columns, data


# def get_columns():
# 	"""
# 	The 4 'Blank' spacer columns required by the RBI_ADAPTER_2022.xlsx
# 	format are shown again as real (currently empty) columns, in the
# 	exact positions the bank template expects:
# 		- 2 blanks right after Beneficiary Name
# 		- 1 blank right after Payment Details 7
# 		- 1 blank right after Transaction Date

# 	Transaction Type is plain Data here - the manual I/N/R/M dropdown is
# 	rendered client-side via the report's formatter() (same pattern as
# 	the AWB Number / Remark columns in SO vs PO Report). Whatever value
# 	is picked is saved back onto the underlying Salary Slip
# 	(custom_transaction_type) via the update_transaction_type API below,
# 	so it survives a report refresh and shows correctly in Excel export
# 	and the notepad download - all three read it from the same saved
# 	field.
# 	"""
# 	return [
# 		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 110},
# 		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
# 		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
# 		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
# 		{"label": _("Blank"), "fieldname": "blank_1", "fieldtype": "Data", "width": 80},
# 		{"label": _("Blank"), "fieldname": "blank_2", "fieldtype": "Data", "width": 80},
# 		{"label": _("Bene Address 1"), "fieldname": "bene_address_1", "fieldtype": "Data", "width": 130},
# 		{"label": _("Bene Address 2"), "fieldname": "bene_address_2", "fieldtype": "Data", "width": 130},
# 		{"label": _("Bene Address 3"), "fieldname": "bene_address_3", "fieldtype": "Data", "width": 130},
# 		{"label": _("Bene Address 4"), "fieldname": "bene_address_4", "fieldtype": "Data", "width": 130},
# 		{"label": _("Bene Address 5"), "fieldname": "bene_address_5", "fieldtype": "Data", "width": 130},
# 		{"label": _("Instruction Reference Number"), "fieldname": "instruction_reference_number", "fieldtype": "Data", "width": 160},
# 		{"label": _("Customer Reference Number"), "fieldname": "customer_reference_number", "fieldtype": "Data", "width": 160},
# 		{"label": _("Payment Details 1"), "fieldname": "payment_details_1", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 2"), "fieldname": "payment_details_2", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 3"), "fieldname": "payment_details_3", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 4"), "fieldname": "payment_details_4", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 5"), "fieldname": "payment_details_5", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 6"), "fieldname": "payment_details_6", "fieldtype": "Data", "width": 120},
# 		{"label": _("Payment Details 7"), "fieldname": "payment_details_7", "fieldtype": "Data", "width": 120},
# 		{"label": _("Blank"), "fieldname": "blank_3", "fieldtype": "Data", "width": 80},
# 		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 110},
# 		{"label": _("Blank"), "fieldname": "blank_4", "fieldtype": "Data", "width": 80},
# 		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 180},
# 		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 450},
# 	]


# def get_data(filters):
# 	data = []

# 	raw_rows = get_raw_rows(filters)

# 	serial_no = 0
# 	for row in raw_rows:
# 		serial_no += 1

# 		transaction_type = row.get("transaction_type")
# 		beneficiary_code = serial_no  # running serial number 1, 2, 3, 4...
# 		beneficiary_account_number = row.get("beneficiary_account_number")
# 		instrument_amount = row.get("instrument_amount")
# 		beneficiary_name = row.get("beneficiary_name")
# 		bene_address_1 = row.get("bene_address_1")
# 		bene_address_2 = row.get("bene_address_2")
# 		bene_address_3 = row.get("bene_address_3")
# 		bene_address_4 = row.get("bene_address_4")
# 		bene_address_5 = row.get("bene_address_5")
# 		instruction_reference_number = row.get("instruction_reference_number")
# 		customer_reference_number = row.get("customer_reference_number")
# 		payment_details_1 = row.get("payment_details_1")
# 		payment_details_2 = row.get("payment_details_2")
# 		payment_details_3 = row.get("payment_details_3")
# 		payment_details_4 = row.get("payment_details_4")
# 		payment_details_5 = row.get("payment_details_5")
# 		payment_details_6 = row.get("payment_details_6")
# 		payment_details_7 = row.get("payment_details_7")
# 		transaction_date = row.get("transaction_date")
# 		ifsc_code = row.get("ifsc_code")
# 		bene_bank_name = row.get("bene_bank_name")
# 		bene_bank_branch_name = row.get("bene_bank_branch_name")
# 		beneficiary_email = row.get("beneficiary_email")

# 		# The 4 "Blank" spacer positions required by RBI_ADAPTER_2022.xlsx are
# 		# kept as empty strings here too - same positions as the visible
# 		# blank_1 / blank_2 / blank_3 / blank_4 columns above.
# 		notepad_data = ",".join(
# 			[
# 				cstr(transaction_type),
# 				cstr(beneficiary_code),
# 				cstr(beneficiary_account_number),
# 				cstr(instrument_amount),
# 				cstr(beneficiary_name),
# 				"",
# 				"",
# 				cstr(bene_address_1),
# 				cstr(bene_address_2),
# 				cstr(bene_address_3),
# 				cstr(bene_address_4),
# 				cstr(bene_address_5),
# 				cstr(instruction_reference_number),
# 				cstr(customer_reference_number),
# 				cstr(payment_details_1),
# 				cstr(payment_details_2),
# 				cstr(payment_details_3),
# 				cstr(payment_details_4),
# 				cstr(payment_details_5),
# 				cstr(payment_details_6),
# 				cstr(payment_details_7),
# 				"",
# 				cstr(transaction_date),
# 				"",
# 				cstr(ifsc_code),
# 				cstr(bene_bank_name),
# 				cstr(bene_bank_branch_name),
# 				cstr(beneficiary_email),
# 			]
# 		)

# 		data.append(
# 			{
# 				# Hidden reference field - not in get_columns(), so it never
# 				# renders as its own visible column, but the JS formatter
# 				# uses it to know which Salary Slip to update when
# 				# Transaction Type is changed in this row.
# 				"salary_slip": row.get("salary_slip"),
# 				"transaction_type": transaction_type,
# 				"beneficiary_code": beneficiary_code,
# 				"beneficiary_account_number": beneficiary_account_number,
# 				"instrument_amount": instrument_amount,
# 				"beneficiary_name": beneficiary_name,
# 				"blank_1": "",
# 				"blank_2": "",
# 				"bene_address_1": bene_address_1,
# 				"bene_address_2": bene_address_2,
# 				"bene_address_3": bene_address_3,
# 				"bene_address_4": bene_address_4,
# 				"bene_address_5": bene_address_5,
# 				"instruction_reference_number": instruction_reference_number,
# 				"customer_reference_number": customer_reference_number,
# 				"payment_details_1": payment_details_1,
# 				"payment_details_2": payment_details_2,
# 				"payment_details_3": payment_details_3,
# 				"payment_details_4": payment_details_4,
# 				"payment_details_5": payment_details_5,
# 				"payment_details_6": payment_details_6,
# 				"payment_details_7": payment_details_7,
# 				"blank_3": "",
# 				"transaction_date": transaction_date,
# 				"blank_4": "",
# 				"ifsc_code": ifsc_code,
# 				"bene_bank_name": bene_bank_name,
# 				"bene_bank_branch_name": bene_bank_branch_name,
# 				"beneficiary_email": beneficiary_email,
# 				"notepad_data": notepad_data,
# 			}
# 		)

# 	return data


# def get_raw_rows(filters):
# 	"""
# 	CONFIRMED via System Console diagnostics on the live site:

# 	- Journal Entry is NOT linked per employee (0 rows anywhere have
# 	  Party Type = Employee). It is a single bulk JE per payroll run.
# 	- That bulk JE is linked to its Payroll Entry through the child table
# 	  Journal Entry Account, using reference_type = "Payroll Entry" and
# 	  reference_name = <payroll entry name>.
# 	- Salary Slip reliably has employee, net_pay, payroll_entry, and its
# 	  own custom_transaction_type field (visible directly on the Salary
# 	  Slip form's Details tab). This is now the single source of truth
# 	  for Transaction Type - manual edits made in the report grid are
# 	  saved back onto this same field via update_transaction_type(), so
# 	  the value persists across refreshes and shows correctly in Excel
# 	  export and the notepad download too.
# 	- Bank details (bank_name, bank_ac_no, ifsc_code) are stored directly
# 	  on the Employee master (Salary tab -> Bank Details section), NOT on
# 	  a separate Bank Account doctype record.

# 	Field mapping:
# 		transaction_type            -> Salary Slip.custom_transaction_type  (derived to I/N/R/M, editable + saved back)
# 		beneficiary_account_number  -> Employee.bank_ac_no
# 		instrument_amount           -> Salary Slip.net_pay
# 		beneficiary_name            -> Employee.employee_name
# 		bene_address_1              -> Employee.current_accommodation_type
# 		bene_address_2              -> Employee.permanent_accommodation_type
# 		bene_address_3              -> Employee.custom_city
# 		bene_address_4              -> Employee.custom_state
# 		bene_address_5              -> Employee.custom_country
# 		instruction_reference_number-> Journal Entry.cheque_no
# 		customer_reference_number   -> Journal Entry.user_remark
# 		payment_details_1..7        -> left blank (not mapped yet)
# 		transaction_date            -> Journal Entry.posting_date
# 		ifsc_code                   -> Employee.ifsc_code
# 		bene_bank_name              -> Employee.bank_name
# 		bene_bank_branch_name       -> left blank (no branch field on Employee)
# 		beneficiary_email           -> Employee.personal_email
# 	"""

# 	rows = []

# 	salary_slips = frappe.get_all(
# 		"Salary Slip",
# 		filters={
# 			"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
# 			"docstatus": 1,
# 		},
# 		fields=["name", "employee", "employee_name", "net_pay", "payroll_entry", "custom_transaction_type"],
# 	)

# 	if not salary_slips:
# 		return rows

# 	# Build a Payroll Entry -> submitted Journal Entry lookup, using the
# 	# Journal Entry Account reference table (the real link on this site).
# 	payroll_entry_names = list({s.payroll_entry for s in salary_slips if s.payroll_entry})

# 	je_refs = (
# 		frappe.get_all(
# 			"Journal Entry Account",
# 			filters={
# 				"reference_type": "Payroll Entry",
# 				"reference_name": ["in", payroll_entry_names],
# 			},
# 			fields=["parent", "reference_name"],
# 		)
# 		if payroll_entry_names
# 		else []
# 	)

# 	je_names = list({r.parent for r in je_refs})

# 	je_details = (
# 		frappe.get_all(
# 			"Journal Entry",
# 			filters={"name": ["in", je_names], "docstatus": 1},
# 			fields=["name", "posting_date", "cheque_no", "user_remark"],
# 		)
# 		if je_names
# 		else []
# 	)
# 	je_by_name = {je.name: je for je in je_details}

# 	# If more than one submitted JE is linked to the same Payroll Entry
# 	# (e.g. an amended entry), keep the one with the latest posting date.
# 	payroll_entry_to_je = {}
# 	for ref in je_refs:
# 		je = je_by_name.get(ref.parent)
# 		if not je:
# 			continue
# 		existing = payroll_entry_to_je.get(ref.reference_name)
# 		if not existing or je.posting_date >= existing.posting_date:
# 			payroll_entry_to_je[ref.reference_name] = je

# 	for slip in salary_slips:
# 		employee = slip.employee
# 		if not employee:
# 			continue

# 		emp = (
# 			frappe.db.get_value(
# 				"Employee",
# 				employee,
# 				[
# 					"employee_name",
# 					"current_accommodation_type",
# 					"permanent_accommodation_type",
# 					"custom_city",
# 					"custom_state",
# 					"custom_country",
# 					"personal_email",
# 					"bank_name",
# 					"bank_ac_no",
# 					"ifsc_code",
# 				],
# 				as_dict=True,
# 			)
# 			or frappe._dict()
# 		)

# 		je = payroll_entry_to_je.get(slip.payroll_entry) or frappe._dict()

# 		rows.append(
# 			{
# 				"salary_slip": slip.name,
# 				"transaction_type": derive_transaction_type(slip.get("custom_transaction_type")),
# 				"beneficiary_account_number": emp.get("bank_ac_no"),
# 				"instrument_amount": slip.net_pay,
# 				"beneficiary_name": emp.get("employee_name") or slip.employee_name,
# 				"bene_address_1": emp.get("current_accommodation_type"),
# 				"bene_address_2": emp.get("permanent_accommodation_type"),
# 				"bene_address_3": emp.get("custom_city"),
# 				"bene_address_4": emp.get("custom_state"),
# 				"bene_address_5": emp.get("custom_country"),
# 				"instruction_reference_number": je.get("cheque_no"),
# 				"customer_reference_number": je.get("user_remark"),
# 				"payment_details_1": "",
# 				"payment_details_2": "",
# 				"payment_details_3": "",
# 				"payment_details_4": "",
# 				"payment_details_5": "",
# 				"payment_details_6": "",
# 				"payment_details_7": "",
# 				"transaction_date": formatdate(je.get("posting_date"), "dd/mm/yyyy") if je.get("posting_date") else "",
# 				"ifsc_code": emp.get("ifsc_code"),
# 				"bene_bank_name": emp.get("bank_name"),
# 				"bene_bank_branch_name": "",
# 				"beneficiary_email": emp.get("personal_email"),
# 			}
# 		)

# 	return rows


# def derive_transaction_type(raw_value):
# 	"""
# 	Maps Salary Slip.custom_transaction_type to the single-letter RBI
# 	code (I = IMPS, N = NEFT, R = RTGS, M = Mobile/UPI). Passed through
# 	unchanged if it's already a single letter.
# 	"""
# 	if not raw_value:
# 		return ""

# 	value = cstr(raw_value).strip().upper()

# 	if value in ("I", "N", "R", "M"):
# 		return value

# 	mapping = {
# 		"IMPS": "I",
# 		"NEFT": "N",
# 		"RTGS": "R",
# 		"MOBILE": "M",
# 		"UPI": "M",
# 	}
# 	return mapping.get(value, value[:1])


# @frappe.whitelist()
# def update_transaction_type(salary_slip, transaction_type):
# 	"""
# 	Called from the report's JS (formatter's <select> onchange) the
# 	moment a user picks a Transaction Type in the grid. Saves the picked
# 	value directly onto Salary Slip.custom_transaction_type via a raw
# 	db.set_value (works even though the Salary Slip is submitted, since
# 	this is a plain field update, not a document save/workflow
# 	transition) - same pattern as update_awb_number / update_remark in
# 	SO vs PO Report.

# 	This is what makes the manual selection persist across a report
# 	refresh, and show correctly in the notepad download and Excel
# 	export - both are generated fresh from this same field.
# 	"""
# 	if not salary_slip:
# 		frappe.throw(_("Salary Slip is required"))

# 	allowed_values = ("", "I", "N", "R", "M")
# 	transaction_type = cstr(transaction_type).strip().upper()

# 	if transaction_type not in allowed_values:
# 		frappe.throw(_("Transaction Type must be one of I, N, R, M"))

# 	if not frappe.db.exists("Salary Slip", salary_slip):
# 		frappe.throw(_("Salary Slip {0} not found").format(salary_slip))

# 	if not frappe.has_permission("Salary Slip", "write", doc=salary_slip):
# 		frappe.throw(_("Not permitted to update this Salary Slip"), frappe.PermissionError)

# 	frappe.db.set_value("Salary Slip", salary_slip, "custom_transaction_type", transaction_type)
# 	frappe.db.commit()

# 	return {"salary_slip": salary_slip, "transaction_type": transaction_type}

import frappe
from frappe import _
from frappe.utils import cstr, formatdate


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	"""
	The 4 'Blank' spacer columns required by the RBI_ADAPTER_2022.xlsx
	format are shown again as real (currently empty) columns, in the
	exact positions the bank template expects:
		- 2 blanks right after Beneficiary Name
		- 1 blank right after Payment Details 7
		- 1 blank right after Transaction Date

	Transaction Type is plain Data here - the manual I/N/R/M dropdown is
	rendered client-side via the report's formatter() (same pattern as
	the AWB Number / Remark columns in SO vs PO Report). Whatever value
	is picked is saved back onto the underlying Salary Slip
	(custom_transaction_type) via the update_transaction_type API below,
	so it survives a report refresh and shows correctly in Excel export
	and the notepad download - all three read it from the same saved
	field.
	"""
	return [
		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 130},
		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 130},
		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 200},
		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 150},
		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 220},
		{"label": _("Blank"), "fieldname": "blank_1", "fieldtype": "Data", "width": 100},
		{"label": _("Blank"), "fieldname": "blank_2", "fieldtype": "Data", "width": 100},
		{"label": _("Bene Address 1"), "fieldname": "bene_address_1", "fieldtype": "Data", "width": 160},
		{"label": _("Bene Address 2"), "fieldname": "bene_address_2", "fieldtype": "Data", "width": 160},
		{"label": _("Bene Address 3"), "fieldname": "bene_address_3", "fieldtype": "Data", "width": 150},
		{"label": _("Bene Address 4"), "fieldname": "bene_address_4", "fieldtype": "Data", "width": 150},
		{"label": _("Bene Address 5"), "fieldname": "bene_address_5", "fieldtype": "Data", "width": 150},
		{"label": _("Instruction Reference Number"), "fieldname": "instruction_reference_number", "fieldtype": "Data", "width": 200},
		{"label": _("Customer Reference Number"), "fieldname": "customer_reference_number", "fieldtype": "Data", "width": 200},
		{"label": _("Payment Details 1"), "fieldname": "payment_details_1", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 2"), "fieldname": "payment_details_2", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 3"), "fieldname": "payment_details_3", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 4"), "fieldname": "payment_details_4", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 5"), "fieldname": "payment_details_5", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 6"), "fieldname": "payment_details_6", "fieldtype": "Data", "width": 140},
		{"label": _("Payment Details 7"), "fieldname": "payment_details_7", "fieldtype": "Data", "width": 140},
		{"label": _("Blank"), "fieldname": "blank_3", "fieldtype": "Data", "width": 100},
		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 140},
		{"label": _("Blank"), "fieldname": "blank_4", "fieldtype": "Data", "width": 100},
		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 140},
		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 200},
		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 200},
		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 220},
		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 500},
	]


def get_data(filters):
	data = []

	raw_rows = get_raw_rows(filters)

	serial_no = 0
	for row in raw_rows:
		serial_no += 1

		transaction_type = row.get("transaction_type")
		beneficiary_code = serial_no  # running serial number 1, 2, 3, 4...
		beneficiary_account_number = row.get("beneficiary_account_number")
		instrument_amount = row.get("instrument_amount")
		beneficiary_name = row.get("beneficiary_name")
		bene_address_1 = row.get("bene_address_1")
		bene_address_2 = row.get("bene_address_2")
		bene_address_3 = row.get("bene_address_3")
		bene_address_4 = row.get("bene_address_4")
		bene_address_5 = row.get("bene_address_5")
		instruction_reference_number = row.get("instruction_reference_number")
		customer_reference_number = row.get("customer_reference_number")
		payment_details_1 = row.get("payment_details_1")
		payment_details_2 = row.get("payment_details_2")
		payment_details_3 = row.get("payment_details_3")
		payment_details_4 = row.get("payment_details_4")
		payment_details_5 = row.get("payment_details_5")
		payment_details_6 = row.get("payment_details_6")
		payment_details_7 = row.get("payment_details_7")
		transaction_date = row.get("transaction_date")
		ifsc_code = row.get("ifsc_code")
		bene_bank_name = row.get("bene_bank_name")
		bene_bank_branch_name = row.get("bene_bank_branch_name")
		beneficiary_email = row.get("beneficiary_email")

		# The 4 "Blank" spacer positions required by RBI_ADAPTER_2022.xlsx are
		# kept as empty strings here too - same positions as the visible
		# blank_1 / blank_2 / blank_3 / blank_4 columns above.
		notepad_data = ",".join(
			[
				cstr(transaction_type),
				cstr(beneficiary_code),
				cstr(beneficiary_account_number),
				cstr(instrument_amount),
				cstr(beneficiary_name),
				"",
				"",
				cstr(bene_address_1),
				cstr(bene_address_2),
				cstr(bene_address_3),
				cstr(bene_address_4),
				cstr(bene_address_5),
				cstr(instruction_reference_number),
				cstr(customer_reference_number),
				cstr(payment_details_1),
				cstr(payment_details_2),
				cstr(payment_details_3),
				cstr(payment_details_4),
				cstr(payment_details_5),
				cstr(payment_details_6),
				cstr(payment_details_7),
				"",
				cstr(transaction_date),
				"",
				cstr(ifsc_code),
				cstr(bene_bank_name),
				cstr(bene_bank_branch_name),
				cstr(beneficiary_email),
			]
		)

		data.append(
			{
				# Hidden reference field - not in get_columns(), so it never
				# renders as its own visible column, but the JS formatter
				# uses it to know which Salary Slip to update when
				# Transaction Type is changed in this row.
				"salary_slip": row.get("salary_slip"),
				"transaction_type": transaction_type,
				"beneficiary_code": beneficiary_code,
				"beneficiary_account_number": beneficiary_account_number,
				"instrument_amount": instrument_amount,
				"beneficiary_name": beneficiary_name,
				"blank_1": "",
				"blank_2": "",
				"bene_address_1": bene_address_1,
				"bene_address_2": bene_address_2,
				"bene_address_3": bene_address_3,
				"bene_address_4": bene_address_4,
				"bene_address_5": bene_address_5,
				"instruction_reference_number": instruction_reference_number,
				"customer_reference_number": customer_reference_number,
				"payment_details_1": payment_details_1,
				"payment_details_2": payment_details_2,
				"payment_details_3": payment_details_3,
				"payment_details_4": payment_details_4,
				"payment_details_5": payment_details_5,
				"payment_details_6": payment_details_6,
				"payment_details_7": payment_details_7,
				"blank_3": "",
				"transaction_date": transaction_date,
				"blank_4": "",
				"ifsc_code": ifsc_code,
				"bene_bank_name": bene_bank_name,
				"bene_bank_branch_name": bene_bank_branch_name,
				"beneficiary_email": beneficiary_email,
				"notepad_data": notepad_data,
			}
		)

	return data


def get_raw_rows(filters):
	"""
	CONFIRMED via System Console diagnostics on the live site:

	- Journal Entry is NOT linked per employee (0 rows anywhere have
	  Party Type = Employee). It is a single bulk JE per payroll run.
	- That bulk JE is linked to its Payroll Entry through the child table
	  Journal Entry Account, using reference_type = "Payroll Entry" and
	  reference_name = <payroll entry name>.
	- Salary Slip reliably has employee, net_pay, payroll_entry, and its
	  own custom_transaction_type field (visible directly on the Salary
	  Slip form's Details tab). This is now the single source of truth
	  for Transaction Type - manual edits made in the report grid are
	  saved back onto this same field via update_transaction_type(), so
	  the value persists across refreshes and shows correctly in Excel
	  export and the notepad download too.
	- Bank details (bank_name, bank_ac_no, ifsc_code) are stored directly
	  on the Employee master (Salary tab -> Bank Details section), NOT on
	  a separate Bank Account doctype record.

	Field mapping:
		transaction_type            -> Salary Slip.custom_transaction_type  (derived to I/N/R/M, editable + saved back)
		beneficiary_account_number  -> Employee.bank_ac_no
		instrument_amount           -> Salary Slip.net_pay
		beneficiary_name            -> Employee.employee_name
		bene_address_1              -> Employee.current_accommodation_type
		bene_address_2              -> Employee.permanent_accommodation_type
		bene_address_3              -> Employee.custom_city
		bene_address_4              -> Employee.custom_state
		bene_address_5              -> Employee.custom_country
		instruction_reference_number-> Journal Entry.cheque_no
		customer_reference_number   -> Journal Entry.user_remark
		payment_details_1..7        -> left blank (not mapped yet)
		transaction_date            -> Journal Entry.posting_date
		ifsc_code                   -> Employee.ifsc_code
		bene_bank_name              -> Employee.bank_name
		bene_bank_branch_name       -> left blank (no branch field on Employee)
		beneficiary_email           -> Employee.personal_email
	"""

	rows = []

	salary_slips = frappe.get_all(
		"Salary Slip",
		filters={
			"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
			"docstatus": 1,
		},
		fields=["name", "employee", "employee_name", "net_pay", "payroll_entry", "custom_transaction_type"],
	)

	if not salary_slips:
		return rows

	# Build a Payroll Entry -> submitted Journal Entry lookup, using the
	# Journal Entry Account reference table (the real link on this site).
	payroll_entry_names = list({s.payroll_entry for s in salary_slips if s.payroll_entry})

	je_refs = (
		frappe.get_all(
			"Journal Entry Account",
			filters={
				"reference_type": "Payroll Entry",
				"reference_name": ["in", payroll_entry_names],
			},
			fields=["parent", "reference_name"],
		)
		if payroll_entry_names
		else []
	)

	je_names = list({r.parent for r in je_refs})

	je_details = (
		frappe.get_all(
			"Journal Entry",
			filters={"name": ["in", je_names], "docstatus": 1},
			fields=["name", "posting_date", "cheque_no", "user_remark"],
		)
		if je_names
		else []
	)
	je_by_name = {je.name: je for je in je_details}

	# If more than one submitted JE is linked to the same Payroll Entry
	# (e.g. an amended entry), keep the one with the latest posting date.
	payroll_entry_to_je = {}
	for ref in je_refs:
		je = je_by_name.get(ref.parent)
		if not je:
			continue
		existing = payroll_entry_to_je.get(ref.reference_name)
		if not existing or je.posting_date >= existing.posting_date:
			payroll_entry_to_je[ref.reference_name] = je

	for slip in salary_slips:
		employee = slip.employee
		if not employee:
			continue

		emp = (
			frappe.db.get_value(
				"Employee",
				employee,
				[
					"employee_name",
					"current_accommodation_type",
					"permanent_accommodation_type",
					"custom_city",
					"custom_state",
					"custom_country",
					"personal_email",
					"bank_name",
					"bank_ac_no",
					"ifsc_code",
				],
				as_dict=True,
			)
			or frappe._dict()
		)

		je = payroll_entry_to_je.get(slip.payroll_entry) or frappe._dict()

		rows.append(
			{
				"salary_slip": slip.name,
				"transaction_type": derive_transaction_type(slip.get("custom_transaction_type")),
				"beneficiary_account_number": emp.get("bank_ac_no"),
				"instrument_amount": slip.net_pay,
				"beneficiary_name": emp.get("employee_name") or slip.employee_name,
				"bene_address_1": emp.get("current_accommodation_type"),
				"bene_address_2": emp.get("permanent_accommodation_type"),
				"bene_address_3": emp.get("custom_city"),
				"bene_address_4": emp.get("custom_state"),
				"bene_address_5": emp.get("custom_country"),
				"instruction_reference_number": je.get("cheque_no"),
				"customer_reference_number": je.get("user_remark"),
				"payment_details_1": "",
				"payment_details_2": "",
				"payment_details_3": "",
				"payment_details_4": "",
				"payment_details_5": "",
				"payment_details_6": "",
				"payment_details_7": "",
				"transaction_date": formatdate(je.get("posting_date"), "dd/mm/yyyy") if je.get("posting_date") else "",
				"ifsc_code": emp.get("ifsc_code"),
				"bene_bank_name": emp.get("bank_name"),
				"bene_bank_branch_name": "",
				"beneficiary_email": emp.get("personal_email"),
			}
		)

	return rows


def derive_transaction_type(raw_value):
	"""
	Maps Salary Slip.custom_transaction_type to the single-letter RBI
	code (I = IMPS, N = NEFT, R = RTGS, M = Mobile/UPI). Passed through
	unchanged if it's already a single letter.
	"""
	if not raw_value:
		return ""

	value = cstr(raw_value).strip().upper()

	if value in ("I", "N", "R", "M"):
		return value

	mapping = {
		"IMPS": "I",
		"NEFT": "N",
		"RTGS": "R",
		"MOBILE": "M",
		"UPI": "M",
	}
	return mapping.get(value, value[:1])


@frappe.whitelist()
def update_transaction_type(salary_slip, transaction_type):
	"""
	Called from the report's JS (formatter's <select> onchange) the
	moment a user picks a Transaction Type in the grid. Saves the picked
	value directly onto Salary Slip.custom_transaction_type via a raw
	db.set_value (works even though the Salary Slip is submitted, since
	this is a plain field update, not a document save/workflow
	transition) - same pattern as update_awb_number / update_remark in
	SO vs PO Report.

	This is what makes the manual selection persist across a report
	refresh, and show correctly in the notepad download and Excel
	export - both are generated fresh from this same field.
	"""
	if not salary_slip:
		frappe.throw(_("Salary Slip is required"))

	allowed_values = ("", "I", "N", "R", "M")
	transaction_type = cstr(transaction_type).strip().upper()

	if transaction_type not in allowed_values:
		frappe.throw(_("Transaction Type must be one of I, N, R, M"))

	if not frappe.db.exists("Salary Slip", salary_slip):
		frappe.throw(_("Salary Slip {0} not found").format(salary_slip))

	if not frappe.has_permission("Salary Slip", "write", doc=salary_slip):
		frappe.throw(_("Not permitted to update this Salary Slip"), frappe.PermissionError)

	frappe.db.set_value("Salary Slip", salary_slip, "custom_transaction_type", transaction_type)
	frappe.db.commit()

	return {"salary_slip": salary_slip, "transaction_type": transaction_type}