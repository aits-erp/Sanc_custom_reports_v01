# # Copyright (c) 2026, Sanc and contributors
# # For license information, please see license.txt

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
# 	#                                       (Bank Account found by filtering
# 	#                                       party_type = "Supplier",
# 	#                                       party = Payment Entry.party -
# 	#                                       NOT via Payment Entry.party_bank_account,
# 	#                                       since that link is not populated)
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
# 	#   bene_bank_branch_name            -> Bank Account.branch_code
# 	#   beneficiary_email                -> Supplier.email_id (Primary Email,
# 	#                                       from the Supplier's Address & Contact tab)
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
# 	Bank details (account no / IFSC / bank name) are pulled from the Bank
# 	Account record found by filtering party_type = "Supplier" and
# 	party = Payment Entry.party (the same filter you use manually in the
# 	Bank Account list view) - NOT via Payment Entry.party_bank_account,
# 	since that link field is not populated on your entries.
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
# 		],
# 		order_by="posting_date asc",
# 	)

# 	rows = []
# 	for pe in payment_entries:
# 		address = get_party_address(pe.party_type, pe.party)
# 		pincode = address.get("pincode") if address else ""
# 		bank_acc_details = get_bank_account_details(pe.party_type, pe.party)
# 		beneficiary_email = get_supplier_email(pe.party)

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
# 				"bene_bank_branch_name": bank_acc_details.get("branch_code"),
# 				"beneficiary_email": beneficiary_email,
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


# def get_bank_account_details(party_type, party):
# 	"""
# 	Finds the Bank Account record for this party by filtering
# 	party_type = "Supplier", party = <supplier> - same as filtering
# 	manually in the Bank Account list view - and returns:
# 		- bank_account_no   -> Beneficiary Account Number
# 		- bank              -> Bene Bank Name (e.g. "UNION BANK OF INDIA")
# 		- custom_ifsc_code  -> IFSC Code

# 	If a supplier has more than one Bank Account, the enabled/default one
# 	is preferred; otherwise the first match found is used.
# 	"""
# 	if not party_type or not party:
# 		return {}

# 	bank_accounts = frappe.get_all(
# 		"Bank Account",
# 		filters={"party_type": party_type, "party": party},
# 		fields=["name", "bank_account_no", "bank", "custom_ifsc_code", "branch_code", "is_default", "disabled"],
# 	)

# 	if not bank_accounts:
# 		return {}

# 	# Prefer an enabled, default account if one exists
# 	for acc in bank_accounts:
# 		if acc.get("is_default") and not acc.get("disabled"):
# 			return acc

# 	# Otherwise prefer any enabled account
# 	for acc in bank_accounts:
# 		if not acc.get("disabled"):
# 			return acc

# 	# Fall back to the first record found
# 	return bank_accounts[0]


# def get_supplier_email(party):
# 	"""
# 	Fetches the Contact.email_id for this Supplier.

# 	Contacts created against a Supplier are named as "-<supplier_id>"
# 	(e.g. Supplier "V00000037" -> Contact "-V00000037"), as seen under
# 	CRM > Contact. We try that direct lookup first (fast, single query),
# 	and fall back to searching via the Dynamic Link table (in case a
# 	supplier's contact doesn't follow that naming pattern, or has
# 	multiple linked contacts).
# 	"""
# 	if not party:
# 		return ""

# 	# 1) Fast path: direct guess based on the "-<supplier_id>" naming convention
# 	direct_contact_name = f"-{party}"
# 	email = frappe.db.get_value("Contact", direct_contact_name, "email_id")
# 	if email:
# 		return email

# 	# 2) Fallback: search via Dynamic Link (covers contacts not following
# 	#    the "-<supplier_id>" naming convention, or multiple linked contacts)
# 	contact_links = frappe.get_all(
# 		"Dynamic Link",
# 		filters={"link_doctype": "Supplier", "link_name": party, "parenttype": "Contact"},
# 		fields=["parent"],
# 	)

# 	if not contact_links:
# 		return ""

# 	contact_names = [c.parent for c in contact_links]

# 	contacts = frappe.get_all(
# 		"Contact",
# 		filters={"name": ["in", contact_names]},
# 		fields=["name", "email_id", "is_primary_contact"],
# 	)

# 	if not contacts:
# 		return ""

# 	for contact in contacts:
# 		if contact.get("is_primary_contact") and contact.get("email_id"):
# 			return contact.get("email_id")

# 	for contact in contacts:
# 		if contact.get("email_id"):
# 			return contact.get("email_id")

# 	return ""


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
	Same column order as RBI_ADAPTER_2022.xlsx.

	The 4 'BLANK' spacer columns are back in the grid (per request), kept
	empty for now - to be mapped to a real field later. They sit in the
	exact same positions as the original RBI adapter layout:
		- 2 blanks right after "Beneficiary Name"
		- 1 blank right after "Payment Details 7"
		- 1 blank right after "Transaction Date"

	"Transaction Type" is plain Data here - the manual I/N/R/M dropdown is
	rendered client-side via the report's formatter() (same pattern used
	in SO vs PO Report for AWB Number / Remark, and in Employee Salary
	Report). Whatever value is picked is saved back onto the underlying
	Payment Entry (custom_transaction_type) via the update_transaction_type
	API below, so it survives a report refresh and shows correctly in
	Excel export and the notepad download - all three read it from the
	same saved field.
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
	# SOURCE: Payment Entry, filtered to Supplier payments only (party_type = Supplier)
	#
	# Confirmed mapping:
	#   transaction_type              -> Payment Entry.custom_transaction_type
	#                                     (IMPS/RTGS/NEFT/HDFC) -> I/N/R/M
	#                                     (shown as an editable dropdown in the
	#                                     grid - manual picks are saved back
	#                                     onto Payment Entry.custom_transaction_type)
	#   beneficiary_code                -> running serial number
	#   beneficiary_account_number      -> Bank Account.bank_account_no
	#                                       (Bank Account found by filtering
	#                                       party_type = "Supplier",
	#                                       party = Payment Entry.party)
	#   instrument_amount                -> Payment Entry.paid_amount
	#   beneficiary_name                 -> Payment Entry.party_name
	#   blank_1, blank_2                 -> not mapped (kept empty, RBI spacer slots)
	#   bene_address_1                   -> Address.address_line1
	#   bene_address_2                   -> Address.address_line2 (pincode stripped out)
	#   bene_address_3                   -> Address.city
	#   bene_address_4                   -> Address.county
	#   bene_address_5                   -> Address.pincode
	#   instruction_reference_number     -> (TODO - not yet mapped)
	#   customer_reference_number        -> Payment Entry.remarks
	#   payment_details_1..7             -> blank for now (TODO - not yet mapped)
	#   blank_3                          -> not mapped (kept empty, RBI spacer slot)
	#   transaction_date                 -> Payment Entry.posting_date (dd/mm/yyyy)
	#   blank_4                          -> not mapped (kept empty, RBI spacer slot)
	#   ifsc_code                        -> Bank Account.custom_ifsc_code
	#   bene_bank_name                   -> Bank Account.bank
	#   bene_bank_branch_name            -> Bank Account.branch_code
	#   beneficiary_email                -> Contact.email_id (Contact linked to Supplier)
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
		# including the 4 blank slots (as blank commas), matching the same
		# positions as the Blank columns shown in the grid.
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
				# uses it to know which Payment Entry to update when
				# Transaction Type is changed in this row.
				"payment_entry": row.get("payment_entry"),
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
	Real query against Payment Entry, restricted to Supplier payments only.
	Bank details (account no / IFSC / bank name / branch code) are pulled
	from the Bank Account record found by filtering party_type = "Supplier"
	and party = Payment Entry.party.
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
				"payment_entry": pe.name,
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
				"bene_bank_branch_name": bank_acc_details.get("branch_code"),
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

	This is used as the DEFAULT value shown in the grid - the Transaction
	Type column is manually editable (dropdown via formatter), and any
	pick is translated back with TRANSACTION_TYPE_CODE_TO_LABEL below and
	saved onto Payment Entry.custom_transaction_type.
	"""
	mapping = {
		"HDFC": "I",
		"NEFT": "N",
		"RTGS": "R",
		"IMPS": "M",
	}
	return mapping.get(custom_transaction_type, "")


# Reverse of get_transaction_type_code() - used by update_transaction_type()
# to translate a manually picked I/N/R/M code back into the word value that
# Payment Entry.custom_transaction_type actually stores.
TRANSACTION_TYPE_CODE_TO_LABEL = {
	"I": "HDFC",
	"N": "NEFT",
	"R": "RTGS",
	"M": "IMPS",
	"": "",
}


def get_bank_account_details(party_type, party):
	"""
	Finds the Bank Account record for this party by filtering
	party_type = "Supplier", party = <supplier> - same as filtering
	manually in the Bank Account list view - and returns:
		- bank_account_no   -> Beneficiary Account Number
		- bank              -> Bene Bank Name (e.g. "UNION BANK OF INDIA")
		- custom_ifsc_code  -> IFSC Code
		- branch_code       -> Bene Bank Branch Name

	If a supplier has more than one Bank Account, the enabled/default one
	is preferred; otherwise the first match found is used.
	"""
	if not party_type or not party:
		return {}

	bank_accounts = frappe.get_all(
		"Bank Account",
		filters={"party_type": party_type, "party": party},
		fields=["name", "bank_account_no", "bank", "custom_ifsc_code", "branch_code", "is_default", "disabled"],
	)

	if not bank_accounts:
		return {}

	# Prefer an enabled, default account if one exists
	for acc in bank_accounts:
		if acc.get("is_default") and not acc.get("disabled"):
			return acc

	# Otherwise prefer any enabled account
	for acc in bank_accounts:
		if not acc.get("disabled"):
			return acc

	# Fall back to the first record found
	return bank_accounts[0]


def get_supplier_email(party):
	"""
	Fetches the Contact.email_id for this Supplier.

	Contacts created against a Supplier are named as "-<supplier_id>"
	(e.g. Supplier "V00000037" -> Contact "-V00000037"), as seen under
	CRM > Contact. We try that direct lookup first (fast, single query),
	and fall back to searching via the Dynamic Link table (in case a
	supplier's contact doesn't follow that naming pattern, or has
	multiple linked contacts).
	"""
	if not party:
		return ""

	# 1) Fast path: direct guess based on the "-<supplier_id>" naming convention
	direct_contact_name = f"-{party}"
	email = frappe.db.get_value("Contact", direct_contact_name, "email_id")
	if email:
		return email

	# 2) Fallback: search via Dynamic Link (covers contacts not following
	#    the "-<supplier_id>" naming convention, or multiple linked contacts)
	contact_links = frappe.get_all(
		"Dynamic Link",
		filters={"link_doctype": "Supplier", "link_name": party, "parenttype": "Contact"},
		fields=["parent"],
	)

	if not contact_links:
		return ""

	contact_names = [c.parent for c in contact_links]

	contacts = frappe.get_all(
		"Contact",
		filters={"name": ["in", contact_names]},
		fields=["name", "email_id", "is_primary_contact"],
	)

	if not contacts:
		return ""

	for contact in contacts:
		if contact.get("is_primary_contact") and contact.get("email_id"):
			return contact.get("email_id")

	for contact in contacts:
		if contact.get("email_id"):
			return contact.get("email_id")

	return ""


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


@frappe.whitelist()
def update_transaction_type(payment_entry, transaction_type):
	"""
	Called from the report's JS (formatter's <select> onchange) the
	moment a user picks a Transaction Type in the grid. Translates the
	picked I/N/R/M code back into the word value Payment Entry actually
	stores (HDFC/NEFT/RTGS/IMPS) and saves it directly onto
	Payment Entry.custom_transaction_type via a raw db.set_value (works
	even though the Payment Entry is submitted, since this is a plain
	field update, not a document save/workflow transition) - same
	pattern as update_awb_number / update_remark in SO vs PO Report, and
	update_transaction_type in Employee Salary Report.

	This is what makes the manual selection persist across a report
	refresh, and show correctly in the notepad download and Excel
	export - both are generated fresh from this same field.
	"""
	if not payment_entry:
		frappe.throw(_("Payment Entry is required"))

	transaction_type = cstr(transaction_type).strip().upper()

	if transaction_type not in TRANSACTION_TYPE_CODE_TO_LABEL:
		frappe.throw(_("Transaction Type must be one of I, N, R, M"))

	if not frappe.db.exists("Payment Entry", payment_entry):
		frappe.throw(_("Payment Entry {0} not found").format(payment_entry))

	if not frappe.has_permission("Payment Entry", "write", doc=payment_entry):
		frappe.throw(_("Not permitted to update this Payment Entry"), frappe.PermissionError)

	stored_value = TRANSACTION_TYPE_CODE_TO_LABEL.get(transaction_type, "")

	frappe.db.set_value("Payment Entry", payment_entry, "custom_transaction_type", stored_value)
	frappe.db.commit()

	return {"payment_entry": payment_entry, "transaction_type": transaction_type}