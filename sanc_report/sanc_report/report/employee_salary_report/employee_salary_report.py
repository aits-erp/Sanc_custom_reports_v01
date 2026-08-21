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
from frappe.utils import cstr


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	"""
	Column order/labels are kept EXACTLY as in RBI_ADAPTER_2022.xlsx
	(including the two 'BLANK' spacer columns required by the RBI format).
	"""
	return [
		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 100},
		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
		{"label": _("Blank"), "fieldname": "blank_1", "fieldtype": "Data", "width": 60},
		{"label": _("Blank"), "fieldname": "blank_2", "fieldtype": "Data", "width": 60},
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
		{"label": _("Blank"), "fieldname": "blank_3", "fieldtype": "Data", "width": 60},
		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 110},
		{"label": _("Blank"), "fieldname": "blank_4", "fieldtype": "Data", "width": 60},
		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 110},
		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 160},
		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 160},
		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 180},
		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 450},
	]


def get_data(filters):
	data = []

	# ------------------------------------------------------------------------
	# STRUCTURE ONLY - field mapping to be filled in next.
	#
	# Planned source mapping (per your instructions):
	#   transaction_type              -> Journal Entry  -> derive I/N/R/M
	#   beneficiary_code               -> running serial number (1,2,3,4...)
	#   beneficiary_account_number     -> Bank Account
	#   instrument_amount              -> Salary Slip.net_pay
	#   beneficiary_name               -> Employee.employee_name
	#   bene_address_1..5              -> (optional, mapped later)
	#   instruction_reference_number   -> (optional, mapped later)
	#   customer_reference_number      -> Journal Entry.remark
	#   payment_details_1..7           -> (optional, mapped later)
	#   transaction_date               -> Journal Entry.posting_date (dd/mm/yyyy)
	#   ifsc_code                      -> Bank Account
	#   bene_bank_name                 -> Bank Account
	#   bene_bank_branch_name          -> Bank Account
	#   beneficiary_email              -> Employee (personal/company email)
	# ------------------------------------------------------------------------

	raw_rows = get_raw_rows(filters)

	serial_no = 0
	for row in raw_rows:
		serial_no += 1

		transaction_type = row.get("transaction_type")  # TODO: map -> I/N/R/M
		beneficiary_code = serial_no
		beneficiary_account_number = row.get("beneficiary_account_number")  # TODO: map -> Bank Account
		instrument_amount = row.get("instrument_amount")  # TODO: map -> Salary Slip.net_pay
		beneficiary_name = row.get("beneficiary_name")  # TODO: map -> Employee.employee_name
		bene_address_1 = row.get("bene_address_1")
		bene_address_2 = row.get("bene_address_2")
		bene_address_3 = row.get("bene_address_3")
		bene_address_4 = row.get("bene_address_4")
		bene_address_5 = row.get("bene_address_5")
		instruction_reference_number = row.get("instruction_reference_number")
		customer_reference_number = row.get("customer_reference_number")  # TODO: map -> JV.remark
		payment_details_1 = row.get("payment_details_1")
		payment_details_2 = row.get("payment_details_2")
		payment_details_3 = row.get("payment_details_3")
		payment_details_4 = row.get("payment_details_4")
		payment_details_5 = row.get("payment_details_5")
		payment_details_6 = row.get("payment_details_6")
		payment_details_7 = row.get("payment_details_7")
		transaction_date = row.get("transaction_date")  # TODO: map -> JV.posting_date (dd/mm/yyyy)
		ifsc_code = row.get("ifsc_code")  # TODO: map -> Bank Account.ifsc_code
		bene_bank_name = row.get("bene_bank_name")  # TODO: map -> Bank Account.bank
		bene_bank_branch_name = row.get("bene_bank_branch_name")  # TODO: map -> Bank Account.branch
		beneficiary_email = row.get("beneficiary_email")  # TODO: map -> Employee email

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
	TEMPORARY TEST DATA - matches the 5 sample rows from RBI_ADAPTER_2022.xlsx
	so you can confirm all 29 columns + the notepad string render correctly
	before the real Journal Entry / Salary Slip / Bank Account mapping is
	wired in.

	>>> REMOVE this dummy block and replace with the real query once field
	mapping is confirmed (see commented example below). <<<
	"""
	return [
		{
			"transaction_type": "I",
			"beneficiary_account_number": "11111111111",
			"instrument_amount": 10000,
			"beneficiary_name": "NAVREET KAUR BRAR",
			"bene_address_1": "",
			"bene_address_2": "",
			"bene_address_3": "",
			"bene_address_4": "",
			"bene_address_5": "",
			"instruction_reference_number": "",
			"customer_reference_number": "Salary",
			"payment_details_1": "",
			"payment_details_2": "",
			"payment_details_3": "",
			"payment_details_4": "",
			"payment_details_5": "",
			"payment_details_6": "",
			"payment_details_7": "",
			"transaction_date": "21/08/2026",
			"ifsc_code": "HDFC0000701",
			"bene_bank_name": "HDFC BANK LTD",
			"bene_bank_branch_name": "",
			"beneficiary_email": "navreet@sanc.in",
		},
		{
			"transaction_type": "R",
			"beneficiary_account_number": "22255358257",
			"instrument_amount": 9999,
			"beneficiary_name": "Vishal Mishra",
			"bene_address_1": "",
			"bene_address_2": "",
			"bene_address_3": "",
			"bene_address_4": "",
			"bene_address_5": "",
			"instruction_reference_number": "",
			"customer_reference_number": "SANC-VM-001",
			"payment_details_1": "",
			"payment_details_2": "",
			"payment_details_3": "",
			"payment_details_4": "",
			"payment_details_5": "",
			"payment_details_6": "",
			"payment_details_7": "",
			"transaction_date": "19/08/2026",
			"ifsc_code": "KKBK0001425",
			"bene_bank_name": "KOTAK BANK LTD",
			"bene_bank_branch_name": "",
			"beneficiary_email": "vishal@sanc.in",
		},
		{
			"transaction_type": "I",
			"beneficiary_account_number": "99225558812",
			"instrument_amount": 9500,
			"beneficiary_name": "Prachi Modi",
			"bene_address_1": "",
			"bene_address_2": "",
			"bene_address_3": "",
			"bene_address_4": "",
			"bene_address_5": "",
			"instruction_reference_number": "",
			"customer_reference_number": "Interest",
			"payment_details_1": "",
			"payment_details_2": "",
			"payment_details_3": "",
			"payment_details_4": "",
			"payment_details_5": "",
			"payment_details_6": "",
			"payment_details_7": "",
			"transaction_date": "18/08/2026",
			"ifsc_code": "HDFC0000703",
			"bene_bank_name": "HDFC BANK LTD",
			"bene_bank_branch_name": "",
			"beneficiary_email": "hr@sanc.in",
		},
		{
			"transaction_type": "N",
			"beneficiary_account_number": "45842541256",
			"instrument_amount": 8000,
			"beneficiary_name": "Hitesh Rana",
			"bene_address_1": "",
			"bene_address_2": "",
			"bene_address_3": "",
			"bene_address_4": "",
			"bene_address_5": "",
			"instruction_reference_number": "",
			"customer_reference_number": "Salary",
			"payment_details_1": "",
			"payment_details_2": "",
			"payment_details_3": "",
			"payment_details_4": "",
			"payment_details_5": "",
			"payment_details_6": "",
			"payment_details_7": "",
			"transaction_date": "03/08/2026",
			"ifsc_code": "HDFC0880703",
			"bene_bank_name": "HDFC BANK LTD",
			"bene_bank_branch_name": "",
			"beneficiary_email": "hitesh@sanc.in",
		},
		{
			"transaction_type": "M",
			"beneficiary_account_number": "88225672366",
			"instrument_amount": 10000,
			"beneficiary_name": "Nikunj Rane",
			"bene_address_1": "",
			"bene_address_2": "",
			"bene_address_3": "",
			"bene_address_4": "",
			"bene_address_5": "",
			"instruction_reference_number": "",
			"customer_reference_number": "Interest",
			"payment_details_1": "",
			"payment_details_2": "",
			"payment_details_3": "",
			"payment_details_4": "",
			"payment_details_5": "",
			"payment_details_6": "",
			"payment_details_7": "",
			"transaction_date": "21/08/2026",
			"ifsc_code": "KKBK0001436",
			"bene_bank_name": "KOTAK BANK LTD",
			"bene_bank_branch_name": "",
			"beneficiary_email": "nikunj@sanc.in",
		},
	]

	# ------------------------------------------------------------------------
	# REAL QUERY (to be enabled once field mapping is confirmed) - example:
	#
	# payroll_entries = frappe.get_all(
	# 	"Payroll Entry",
	# 	filters={"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]]},
	# 	fields=["name"],
	# )
	#
	# rows = []
	# for pe in payroll_entries:
	# 	salary_slips = frappe.get_all(
	# 		"Salary Slip",
	# 		filters={"payroll_entry": pe.name},
	# 		fields=["employee", "employee_name", "net_pay"],
	# 	)
	# 	journal_entries = frappe.get_all(
	# 		"Journal Entry",
	# 		filters={"payroll_entry": pe.name},   # exact link field to confirm
	# 		fields=["name", "posting_date", "remark"],
	# 	)
	# 	# ... join Salary Slip -> Employee -> Bank Account, etc.
	#
	# return rows
	# ------------------------------------------------------------------------