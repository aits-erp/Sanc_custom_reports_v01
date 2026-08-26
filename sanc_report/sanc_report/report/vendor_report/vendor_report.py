# # # Copyright (c) 2026, Sukku and contributors
# # # For license information, please see license.txt

# import re

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
# 	Same column order as RBI_ADAPTER_2022.xlsx, minus the 4 'BLANK' spacer
# 	columns (removed from the report grid on request - they are still
# 	represented as empty positions inside the Notepad export string below,
# 	since the bank file format still needs those fixed positions).
# 	"""
# 	return [
# 		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 100},
# 		{"label": _("Beneficiary Code"), "fieldname": "beneficiary_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Beneficiary Account Number"), "fieldname": "beneficiary_account_number", "fieldtype": "Data", "width": 170},
# 		{"label": _("Instrument Amount"), "fieldname": "instrument_amount", "fieldtype": "Currency", "width": 130},
# 		{"label": _("Beneficiary Name"), "fieldname": "beneficiary_name", "fieldtype": "Data", "width": 200},
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
# 		{"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Data", "width": 110},
# 		{"label": _("IFSC Code"), "fieldname": "ifsc_code", "fieldtype": "Data", "width": 110},
# 		{"label": _("Bene Bank Name"), "fieldname": "bene_bank_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Bene Bank Branch Name"), "fieldname": "bene_bank_branch_name", "fieldtype": "Data", "width": 160},
# 		{"label": _("Beneficiary Email ID"), "fieldname": "beneficiary_email", "fieldtype": "Data", "width": 180},
# 		{"label": _("Open Notepad and Copy Below Data"), "fieldname": "notepad_data", "fieldtype": "Data", "width": 450},
# 	]


# def get_data(filters):
# 	data = []

# 	# ------------------------------------------------------------------------
# 	# SOURCE: Payment Entry, filtered to Supplier payments only (party_type = Supplier)
# 	#
# 	# Confirmed mapping:
# 	#   transaction_type              -> Payment Entry.custom_transaction_type
# 	#                                     (IMPS/RTGS/NEFT/HDFC) -> I/N/R/M
# 	#   beneficiary_code                -> running serial number
# 	#   beneficiary_account_number      -> Bank Account.bank_account_no
# 	#                                       (Bank Account linked via
# 	#                                       Payment Entry.party_bank_account)
# 	#   instrument_amount                -> Payment Entry.paid_amount
# 	#   beneficiary_name                 -> Payment Entry.party_name
# 	#   bene_address_1                   -> Address.address_line1
# 	#   bene_address_2                   -> Address.address_line2 (pincode stripped out)
# 	#   bene_address_3                   -> Address.city
# 	#   bene_address_4                   -> Address.county
# 	#   bene_address_5                   -> Address.pincode
# 	#   instruction_reference_number     -> (TODO - not yet mapped)
# 	#   customer_reference_number        -> Payment Entry.remarks
# 	#   payment_details_1..7             -> blank for now (TODO - not yet mapped)
# 	#   transaction_date                 -> Payment Entry.posting_date (dd/mm/yyyy)
# 	#   ifsc_code                        -> Bank Account.custom_ifsc_code
# 	#   bene_bank_name                   -> Bank Account.bank
# 	#   bene_bank_branch_name            -> Payment Entry.bank_account
# 	#   beneficiary_email                -> Payment Entry.contact_email
# 	# ------------------------------------------------------------------------

# 	raw_rows = get_raw_rows(filters)

# 	serial_no = 0
# 	for row in raw_rows:
# 		serial_no += 1

# 		transaction_type = row.get("transaction_type")
# 		beneficiary_code = serial_no
# 		beneficiary_account_number = row.get("beneficiary_account_number")
# 		instrument_amount = row.get("instrument_amount")
# 		beneficiary_name = row.get("beneficiary_name")
# 		bene_address_1 = row.get("bene_address_1")
# 		bene_address_2 = row.get("bene_address_2")
# 		bene_address_3 = row.get("bene_address_3")
# 		bene_address_4 = row.get("bene_address_4")
# 		bene_address_5 = row.get("bene_address_5")
# 		instruction_reference_number = row.get("instruction_reference_number")  # TODO: not yet mapped
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

# 		# Notepad export string keeps the original RBI fixed-position layout,
# 		# including the 4 blank slots (as blank commas), even though those
# 		# 4 columns are no longer shown as separate columns in the report grid.
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
# 				"transaction_date": transaction_date,
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
# 	Real query against Payment Entry, restricted to Supplier payments only.
# 	Bank details (account no / IFSC / bank name) are pulled from the linked
# 	Bank Account record (Payment Entry.party_bank_account), not from
# 	Payment Entry fields directly.
# 	"""
# 	conditions = {
# 		"docstatus": 1,
# 		"party_type": "Supplier",
# 	}

# 	if filters.get("from_date") and filters.get("to_date"):
# 		conditions["posting_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]

# 	payment_entries = frappe.get_all(
# 		"Payment Entry",
# 		filters=conditions,
# 		fields=[
# 			"name",
# 			"custom_transaction_type",
# 			"party_type",
# 			"party",
# 			"party_name",
# 			"paid_amount",
# 			"remarks",
# 			"posting_date",
# 			"party_bank_account",
# 			"bank_account",
# 			"contact_email",
# 		],
# 		order_by="posting_date asc",
# 	)

# 	rows = []
# 	for pe in payment_entries:
# 		address = get_party_address(pe.party_type, pe.party)
# 		pincode = address.get("pincode") if address else ""
# 		bank_acc_details = get_bank_account_details(pe.party_bank_account)

# 		rows.append(
# 			{
# 				"transaction_type": get_transaction_type_code(pe.custom_transaction_type),
# 				"beneficiary_account_number": bank_acc_details.get("bank_account_no"),
# 				"instrument_amount": pe.paid_amount,
# 				"beneficiary_name": pe.party_name,
# 				"bene_address_1": address.get("address_line1") if address else "",
# 				"bene_address_2": strip_pincode(address.get("address_line2") if address else "", pincode),
# 				"bene_address_3": address.get("city") if address else "",
# 				"bene_address_4": address.get("county") if address else "",
# 				"bene_address_5": pincode,
# 				"instruction_reference_number": "",  # TODO: not yet mapped
# 				"customer_reference_number": pe.remarks,
# 				"payment_details_1": "",
# 				"payment_details_2": "",
# 				"payment_details_3": "",
# 				"payment_details_4": "",
# 				"payment_details_5": "",
# 				"payment_details_6": "",
# 				"payment_details_7": "",
# 				"transaction_date": formatdate(pe.posting_date, "dd/mm/yyyy") if pe.posting_date else "",
# 				"ifsc_code": bank_acc_details.get("custom_ifsc_code"),
# 				"bene_bank_name": bank_acc_details.get("bank"),
# 				"bene_bank_branch_name": pe.bank_account,
# 				"beneficiary_email": pe.contact_email,
# 			}
# 		)

# 	return rows


# def get_transaction_type_code(custom_transaction_type):
# 	"""
# 	Maps Payment Entry.custom_transaction_type (IMPS / RTGS / NEFT / HDFC)
# 	to the single-letter RBI adapter code:
# 		I = HDFC to HDFC
# 		N = NEFT
# 		R = RTGS
# 		M = IMPS
# 	"""
# 	mapping = {
# 		"HDFC": "I",
# 		"NEFT": "N",
# 		"RTGS": "R",
# 		"IMPS": "M",
# 	}
# 	return mapping.get(custom_transaction_type, "")


# def get_bank_account_details(bank_account_name):
# 	"""
# 	Fetches the beneficiary's Bank Account record (linked via
# 	Payment Entry.party_bank_account) and returns:
# 		- bank_account_no   -> Beneficiary Account Number
# 		- bank              -> Bene Bank Name (e.g. "UNION BANK OF INDIA")
# 		- custom_ifsc_code  -> IFSC Code
# 	"""
# 	if not bank_account_name:
# 		return {}

# 	return (
# 		frappe.db.get_value(
# 			"Bank Account",
# 			bank_account_name,
# 			["bank_account_no", "bank", "custom_ifsc_code"],
# 			as_dict=True,
# 		)
# 		or {}
# 	)


# def get_party_address(party_type, party):
# 	"""
# 	Fetches the Address linked to the Payment Entry's party (Supplier, via
# 	the Dynamic Link child table) and returns address_line1, address_line2,
# 	city, county and pincode.
# 	"""
# 	if not party_type or not party:
# 		return {}

# 	address_name = frappe.db.get_value(
# 		"Dynamic Link",
# 		{"link_doctype": party_type, "link_name": party, "parenttype": "Address"},
# 		"parent",
# 	)

# 	if not address_name:
# 		return {}

# 	return (
# 		frappe.db.get_value(
# 			"Address",
# 			address_name,
# 			["address_line1", "address_line2", "city", "county", "pincode"],
# 			as_dict=True,
# 		)
# 		or {}
# 	)


# def strip_pincode(address_text, pincode):
# 	"""
# 	Bene Address 2 (address_line2) often already has the pincode baked into
# 	the free text (e.g. 'Kaman Bhiwandi Road Poman, Vasai - 401208'). Since
# 	Bene Address 5 already carries the pincode separately, this removes the
# 	pincode number from address_line2 and cleans up any leftover trailing
# 	punctuation (dash, comma, period, spaces) so it doesn't look broken.
# 	"""
# 	if not address_text:
# 		return address_text

# 	text = address_text

# 	if pincode:
# 		text = text.replace(str(pincode), "")

# 	# Clean up trailing separators left behind after removing the pincode
# 	# e.g. "Vasai - " -> "Vasai", "Ahmedabad -, Gujarat," -> "Ahmedabad, Gujarat"
# 	text = re.sub(r"[\s,\-]+$", "", text)
# 	text = re.sub(r"\s{2,}", " ", text)

# 	return text.strip()


# Copyright (c) 2026, Sanc and contributors
# For license information, please see license.txt

import re

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
	Same column order as RBI_ADAPTER_2022.xlsx, minus the 4 'BLANK' spacer
	columns (removed from the report grid on request - they are still
	represented as empty positions inside the Notepad export string below,
	since the bank file format still needs those fixed positions).
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

	# ------------------------------------------------------------------------
	# SOURCE: Payment Entry, filtered to Supplier payments only (party_type = Supplier)
	#
	# Confirmed mapping:
	#   transaction_type              -> Payment Entry.custom_transaction_type
	#                                     (IMPS/RTGS/NEFT/HDFC) -> I/N/R/M
	#   beneficiary_code                -> running serial number
	#   beneficiary_account_number      -> Bank Account.bank_account_no
	#                                       (Bank Account found by filtering
	#                                       party_type = "Supplier",
	#                                       party = Payment Entry.party -
	#                                       NOT via Payment Entry.party_bank_account,
	#                                       since that link is not populated)
	#   instrument_amount                -> Payment Entry.paid_amount
	#   beneficiary_name                 -> Payment Entry.party_name
	#   bene_address_1                   -> Address.address_line1
	#   bene_address_2                   -> Address.address_line2 (pincode stripped out)
	#   bene_address_3                   -> Address.city
	#   bene_address_4                   -> Address.county
	#   bene_address_5                   -> Address.pincode
	#   instruction_reference_number     -> (TODO - not yet mapped)
	#   customer_reference_number        -> Payment Entry.remarks
	#   payment_details_1..7             -> blank for now (TODO - not yet mapped)
	#   transaction_date                 -> Payment Entry.posting_date (dd/mm/yyyy)
	#   ifsc_code                        -> Bank Account.custom_ifsc_code
	#   bene_bank_name                   -> Bank Account.bank
	#   bene_bank_branch_name            -> Payment Entry.bank_account
	#   beneficiary_email                -> Supplier.email_id (Primary Email,
	#                                       from the Supplier's Address & Contact tab)
	# ------------------------------------------------------------------------

	raw_rows = get_raw_rows(filters)

	serial_no = 0
	for row in raw_rows:
		serial_no += 1

		transaction_type = row.get("transaction_type")
		beneficiary_code = serial_no
		beneficiary_account_number = row.get("beneficiary_account_number")
		instrument_amount = row.get("instrument_amount")
		beneficiary_name = row.get("beneficiary_name")
		bene_address_1 = row.get("bene_address_1")
		bene_address_2 = row.get("bene_address_2")
		bene_address_3 = row.get("bene_address_3")
		bene_address_4 = row.get("bene_address_4")
		bene_address_5 = row.get("bene_address_5")
		instruction_reference_number = row.get("instruction_reference_number")  # TODO: not yet mapped
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

		# Notepad export string keeps the original RBI fixed-position layout,
		# including the 4 blank slots (as blank commas), even though those
		# 4 columns are no longer shown as separate columns in the report grid.
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
	Real query against Payment Entry, restricted to Supplier payments only.
	Bank details (account no / IFSC / bank name) are pulled from the Bank
	Account record found by filtering party_type = "Supplier" and
	party = Payment Entry.party (the same filter you use manually in the
	Bank Account list view) - NOT via Payment Entry.party_bank_account,
	since that link field is not populated on your entries.
	"""
	conditions = {
		"docstatus": 1,
		"party_type": "Supplier",
	}

	if filters.get("from_date") and filters.get("to_date"):
		conditions["posting_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]

	payment_entries = frappe.get_all(
		"Payment Entry",
		filters=conditions,
		fields=[
			"name",
			"custom_transaction_type",
			"party_type",
			"party",
			"party_name",
			"paid_amount",
			"remarks",
			"posting_date",
			"bank_account",
		],
		order_by="posting_date asc",
	)

	rows = []
	for pe in payment_entries:
		address = get_party_address(pe.party_type, pe.party)
		pincode = address.get("pincode") if address else ""
		bank_acc_details = get_bank_account_details(pe.party_type, pe.party)
		beneficiary_email = get_supplier_email(pe.party)

		rows.append(
			{
				"transaction_type": get_transaction_type_code(pe.custom_transaction_type),
				"beneficiary_account_number": bank_acc_details.get("bank_account_no"),
				"instrument_amount": pe.paid_amount,
				"beneficiary_name": pe.party_name,
				"bene_address_1": address.get("address_line1") if address else "",
				"bene_address_2": strip_pincode(address.get("address_line2") if address else "", pincode),
				"bene_address_3": address.get("city") if address else "",
				"bene_address_4": address.get("county") if address else "",
				"bene_address_5": pincode,
				"instruction_reference_number": "",  # TODO: not yet mapped
				"customer_reference_number": pe.remarks,
				"payment_details_1": "",
				"payment_details_2": "",
				"payment_details_3": "",
				"payment_details_4": "",
				"payment_details_5": "",
				"payment_details_6": "",
				"payment_details_7": "",
				"transaction_date": formatdate(pe.posting_date, "dd/mm/yyyy") if pe.posting_date else "",
				"ifsc_code": bank_acc_details.get("custom_ifsc_code"),
				"bene_bank_name": bank_acc_details.get("bank"),
				"bene_bank_branch_name": pe.bank_account,
				"beneficiary_email": beneficiary_email,
			}
		)

	return rows


def get_transaction_type_code(custom_transaction_type):
	"""
	Maps Payment Entry.custom_transaction_type (IMPS / RTGS / NEFT / HDFC)
	to the single-letter RBI adapter code:
		I = HDFC to HDFC
		N = NEFT
		R = RTGS
		M = IMPS
	"""
	mapping = {
		"HDFC": "I",
		"NEFT": "N",
		"RTGS": "R",
		"IMPS": "M",
	}
	return mapping.get(custom_transaction_type, "")


def get_bank_account_details(party_type, party):
	"""
	Finds the Bank Account record for this party by filtering
	party_type = "Supplier", party = <supplier> - same as filtering
	manually in the Bank Account list view - and returns:
		- bank_account_no   -> Beneficiary Account Number
		- bank              -> Bene Bank Name (e.g. "UNION BANK OF INDIA")
		- custom_ifsc_code  -> IFSC Code

	If a supplier has more than one Bank Account, the enabled/default one
	is preferred; otherwise the first match found is used.
	"""
	if not party_type or not party:
		return {}

	bank_accounts = frappe.get_all(
		"Bank Account",
		filters={"party_type": party_type, "party": party},
		fields=["name", "bank_account_no", "bank", "custom_ifsc_code", "is_default_account", "disabled"],
	)

	if not bank_accounts:
		return {}

	# Prefer an enabled, default account if one exists
	for acc in bank_accounts:
		if acc.get("is_default_account") and not acc.get("disabled"):
			return acc

	# Otherwise prefer any enabled account
	for acc in bank_accounts:
		if not acc.get("disabled"):
			return acc

	# Fall back to the first record found
	return bank_accounts[0]


def get_supplier_email(party):
	"""
	Fetches the Supplier's Primary Email (Supplier.email_id, shown under
	the Address & Contact tab on the Supplier form).
	"""
	if not party:
		return ""

	return frappe.db.get_value("Supplier", party, "email_id") or ""


def get_party_address(party_type, party):
	"""
	Fetches the Address linked to the Payment Entry's party (Supplier, via
	the Dynamic Link child table) and returns address_line1, address_line2,
	city, county and pincode.
	"""
	if not party_type or not party:
		return {}

	address_name = frappe.db.get_value(
		"Dynamic Link",
		{"link_doctype": party_type, "link_name": party, "parenttype": "Address"},
		"parent",
	)

	if not address_name:
		return {}

	return (
		frappe.db.get_value(
			"Address",
			address_name,
			["address_line1", "address_line2", "city", "county", "pincode"],
			as_dict=True,
		)
		or {}
	)


def strip_pincode(address_text, pincode):
	"""
	Bene Address 2 (address_line2) often already has the pincode baked into
	the free text (e.g. 'Kaman Bhiwandi Road Poman, Vasai - 401208'). Since
	Bene Address 5 already carries the pincode separately, this removes the
	pincode number from address_line2 and cleans up any leftover trailing
	punctuation (dash, comma, period, spaces) so it doesn't look broken.
	"""
	if not address_text:
		return address_text

	text = address_text

	if pincode:
		text = text.replace(str(pincode), "")

	# Clean up trailing separators left behind after removing the pincode
	# e.g. "Vasai - " -> "Vasai", "Ahmedabad -, Gujarat," -> "Ahmedabad, Gujarat"
	text = re.sub(r"[\s,\-]+$", "", text)
	text = re.sub(r"\s{2,}", " ", text)

	return text.strip()