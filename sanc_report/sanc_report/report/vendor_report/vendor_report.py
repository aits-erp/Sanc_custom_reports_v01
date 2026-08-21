# Copyright (c) 2026, Sukku and contributors
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

		# NOTE: the 2 "Blank" spacer fields required by RBI_ADAPTER_2022.xlsx
		# between beneficiary_name/instrument_amount block and address block,
		# and the other 2 spacer fields (before transaction_date, before
		# ifsc_code) still exist ONLY in this comma string, because the bank
		# file format itself requires them - they are not shown as report
		# columns anymore.
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
	Real mapping, driven off Journal Entry (source of the payment run),
	joined to Employee, Bank Account, and Salary Slip.

	Field mapping (as confirmed):
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

	journal_entries = frappe.get_all(
		"Journal Entry",
		filters={
			"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
			"docstatus": 1,
		},
		fields=["name", "posting_date", "cheque_no", "user_remark", "custom_transaction_type"],
	)

	for je in journal_entries:
		# One Journal Entry can carry payments for more than one employee -
		# pick up every accounting line in this JE where the party is an Employee.
		je_employee_rows = frappe.get_all(
			"Journal Entry Account",
			filters={"parent": je.name, "party_type": "Employee"},
			fields=["party"],
		)

		for jea in je_employee_rows:
			employee = jea.party
			if not employee:
				continue

			emp = frappe.db.get_value(
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
			if not emp:
				continue

			bank_account = frappe.db.get_value(
				"Bank Account",
				{"party_type": "Employee", "party": employee},
				["bank_account_no", "custom_ifsc_code", "account_name", "bank"],
				as_dict=True,
			) or frappe._dict()

			net_pay = frappe.db.get_value(
				"Salary Slip",
				{
					"employee": employee,
					"docstatus": 1,
					"posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
				},
				"net_pay",
			)

			rows.append(
				{
					"transaction_type": derive_transaction_type(je.get("custom_transaction_type")),
					"beneficiary_account_number": bank_account.get("bank_account_no"),
					"instrument_amount": net_pay,
					"beneficiary_name": emp.get("employee_name"),
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
					"transaction_date": formatdate(je.get("posting_date"), "dd/mm/yyyy"),
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
	code (I = IMPS, N = NEFT, R = RTGS, M = Mobile/UPI).
	If custom_transaction_type is already stored as a single letter,
	it is passed through unchanged.
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