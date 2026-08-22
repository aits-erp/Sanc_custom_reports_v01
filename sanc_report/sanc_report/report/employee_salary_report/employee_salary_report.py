# # Copyright (c) 2026, Sukku and contributors
# # For license information, please see license.txt

# # import frappe
# # Copyright (c) 2026, Sanc and contributors
# # For license information, please see license.txt

# import frappe
# from frappe import _
# from frappe.utils import cstr


# def execute(filters=None):
# 	filters = filters or {}
# 	columns = get_columns()
# 	data = get_data(filters)
# 	return columns, data


# def get_columns():
# 	"""
# 	Column order/labels are kept EXACTLY as in RBI_ADAPTER_2022.xlsx
# 	(including the two 'BLANK' spacer columns required by the RBI format).
# 	"""
# 	return [
# 		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 100},
# 		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
# 		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
# 		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
# 		{"label": _("Blank"), "fieldname": "blank_1", "fieldtype": "Data", "width": 60},
# 		{"label": _("Blank"), "fieldname": "blank_2", "fieldtype": "Data", "width": 60},
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
# 		{"label": _("Blank"), "fieldname": "blank_3", "fieldtype": "Data", "width": 60},
# 		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 110},
# 		{"label": _("Blank"), "fieldname": "blank_4", "fieldtype": "Data", "width": 60},
# 		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 180},
# 		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 450},
# 	]


# def get_data(filters):
# 	data = []

# 	# ------------------------------------------------------------------------
# 	# STRUCTURE ONLY - field mapping to be filled in next.
# 	#
# 	# Planned source mapping (per your instructions):
# 	#   transaction_type              -> Journal Entry  -> derive I/N/R/M
# 	#   beneficiary_code               -> running serial number (1,2,3,4...)
# 	#   beneficiary_account_number     -> Bank Account
# 	#   instrument_amount              -> Salary Slip.net_pay
# 	#   beneficiary_name               -> Employee.employee_name
# 	#   bene_address_1..5              -> (optional, mapped later)
# 	#   instruction_reference_number   -> (optional, mapped later)
# 	#   customer_reference_number      -> Journal Entry.remark
# 	#   payment_details_1..7           -> (optional, mapped later)
# 	#   transaction_date               -> Journal Entry.posting_date (dd/mm/yyyy)
# 	#   ifsc_code                      -> Bank Account
# 	#   bene_bank_name                 -> Bank Account
# 	#   bene_bank_branch_name          -> Bank Account
# 	#   beneficiary_email              -> Employee (personal/company email)
# 	# ------------------------------------------------------------------------

# 	raw_rows = get_raw_rows(filters)

# 	serial_no = 0
# 	for row in raw_rows:
# 		serial_no += 1

# 		transaction_type = row.get("transaction_type")  # TODO: map -> I/N/R/M
# 		beneficiary_code = serial_no
# 		beneficiary_account_number = row.get("beneficiary_account_number")  # TODO: map -> Bank Account
# 		instrument_amount = row.get("instrument_amount")  # TODO: map -> Salary Slip.net_pay
# 		beneficiary_name = row.get("beneficiary_name")  # TODO: map -> Employee.employee_name
# 		bene_address_1 = row.get("bene_address_1")
# 		bene_address_2 = row.get("bene_address_2")
# 		bene_address_3 = row.get("bene_address_3")
# 		bene_address_4 = row.get("bene_address_4")
# 		bene_address_5 = row.get("bene_address_5")
# 		instruction_reference_number = row.get("instruction_reference_number")
# 		customer_reference_number = row.get("customer_reference_number")  # TODO: map -> JV.remark
# 		payment_details_1 = row.get("payment_details_1")
# 		payment_details_2 = row.get("payment_details_2")
# 		payment_details_3 = row.get("payment_details_3")
# 		payment_details_4 = row.get("payment_details_4")
# 		payment_details_5 = row.get("payment_details_5")
# 		payment_details_6 = row.get("payment_details_6")
# 		payment_details_7 = row.get("payment_details_7")
# 		transaction_date = row.get("transaction_date")  # TODO: map -> JV.posting_date (dd/mm/yyyy)
# 		ifsc_code = row.get("ifsc_code")  # TODO: map -> Bank Account.ifsc_code
# 		bene_bank_name = row.get("bene_bank_name")  # TODO: map -> Bank Account.bank
# 		bene_bank_branch_name = row.get("bene_bank_branch_name")  # TODO: map -> Bank Account.branch
# 		beneficiary_email = row.get("beneficiary_email")  # TODO: map -> Employee email

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
# 	PLACEHOLDER - returns an empty list for now so the report loads with the
# 	correct column structure and no errors.

# 	Once you confirm the field mapping, this function will be replaced with
# 	something like:

# 		payroll_entries = frappe.get_all(
# 			"Payroll Entry",
# 			filters={"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]]},
# 			fields=["name"],
# 		)

# 		for pe in payroll_entries:
# 			salary_slips = frappe.get_all(
# 				"Salary Slip",
# 				filters={"payroll_entry": pe.name},
# 				fields=["employee", "employee_name", "net_pay"],
# 			)
# 			journal_entries = frappe.get_all(
# 				"Journal Entry",
# 				filters={"payroll_entry": pe.name},   # exact link field to confirm
# 				fields=["name", "posting_date", "remark"],
# 			)
# 			# ... join Salary Slip -> Employee -> Bank Account, etc.
# 	"""
# 	return []


# Copyright (c) 2026, Sanc and contributors
# For license information, please see license.txt

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
	4 spacer 'Blank' columns removed as requested - only real, mapped
	columns remain.
	"""
	return [
		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 100},
		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
		{"label": _("Bene Address 1"), "fieldname": "bene_address_1", "fieldtype": "Data", "width": 130},
		{"label": _("Bene Address 2"), "fieldname": "bene_address_2", "fieldtype": "Data", "width": 130},
		{"label": _("Bene Address 3"), "fieldname": "bene_address_3", "fieldtype": "Data", "width": 130},
		{"label": _("Bene Address 4"), "fieldname": "bene_address_4", "fieldtype": "Data", "width": 130},
		{"label": _("Bene Address 5"), "fieldname": "bene_address_5", "fieldtype": "Data", "width": 130},
		{"label": _("Instruction Reference Number"), "fieldname": "instruction_reference_number", "fieldtype": "Data", "width": 160},
		{"label": _("Customer Reference Number"), "fieldname": "customer_reference_number", "fieldtype": "Data", "width": 160},
		{"label": _("Payment Details 1"), "fieldname": "payment_details_1", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 2"), "fieldname": "payment_details_2", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 3"), "fieldname": "payment_details_3", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 4"), "fieldname": "payment_details_4", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 5"), "fieldname": "payment_details_5", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 6"), "fieldname": "payment_details_6", "fieldtype": "Data", "width": 120},
		{"label": _("Payment Details 7"), "fieldname": "payment_details_7", "fieldtype": "Data", "width": 120},
		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 110},
		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 110},
		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 160},
		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 160},
		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 180},
		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 450},
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
		# kept ONLY inside this comma string (the bank file format needs
		# them) - they are not shown as report columns.
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
				"transaction_type": transaction_type,
				"beneficiary_code": beneficiary_code,
				"beneficiary_account_number": beneficiary_account_number,
				"instrument_amount": instrument_amount,
				"beneficiary_name": beneficiary_name,
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
				"transaction_date": transaction_date,
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
	- Salary Slip reliably has employee, net_pay, and payroll_entry.

	So the report is anchored on Salary Slip, and Journal Entry fields
	(transaction_date, cheque_no, user_remark, custom_transaction_type)
	are pulled via: Salary Slip.payroll_entry -> Journal Entry Account
	(reference_name = payroll_entry) -> parent Journal Entry.

	If a payroll run has no linked/submitted Journal Entry yet, those
	4 fields are simply left blank for that employee's row - the
	employee, amount, address, and bank details are still shown.

	Field mapping:
		transaction_type            -> Journal Entry.custom_transaction_type  (derived to I/N/R/M)
		beneficiary_account_number  -> Bank Account.bank_account_no
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
		ifsc_code                   -> Bank Account.custom_ifsc_code
		bene_bank_name              -> Bank Account.account_name
		bene_bank_branch_name       -> Bank Account.bank
		beneficiary_email           -> Employee.personal_email
	"""

	rows = []

	salary_slips = frappe.get_all(
		"Salary Slip",
		filters={
			"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
			"docstatus": 1,
		},
		fields=["name", "employee", "employee_name", "net_pay", "payroll_entry"],
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
			fields=["name", "posting_date", "cheque_no", "user_remark", "custom_transaction_type"],
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
				],
				as_dict=True,
			)
			or frappe._dict()
		)

		bank_account = (
			frappe.db.get_value(
				"Bank Account",
				{"party_type": "Employee", "party": employee},
				["bank_account_no", "custom_ifsc_code", "account_name", "bank"],
				as_dict=True,
			)
			or frappe._dict()
		)

		je = payroll_entry_to_je.get(slip.payroll_entry) or frappe._dict()

		rows.append(
			{
				"transaction_type": derive_transaction_type(je.get("custom_transaction_type")),
				"beneficiary_account_number": bank_account.get("bank_account_no"),
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
				"ifsc_code": bank_account.get("custom_ifsc_code"),
				"bene_bank_name": bank_account.get("account_name"),
				"bene_bank_branch_name": bank_account.get("bank"),
				"beneficiary_email": emp.get("personal_email"),
			}
		)

	return rows


def derive_transaction_type(raw_value):
	"""
	Maps Journal Entry.custom_transaction_type to the single-letter RBI
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