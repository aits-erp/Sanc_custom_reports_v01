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

	The 4 BLANK spacer columns are kept empty and remain
	in their original positions.

	Transaction Type is mapped from:
	Payment Entry.custom_transaction_type

	Mapping:
		HDFC -> I
		NEFT -> N
		RTGS -> R
		IMPS -> M
	"""
	return [
		{
			"label": _("Transaction Type"),
			"fieldname": "transaction_type",
			"fieldtype": "Select",
			"options": "\nI\nN\nR\nM",
			"editable": 1,
			"width": 100,
		},
		{
			"label": _("Beneficiary Code"),
			"fieldname": "beneficiary_code",
			"fieldtype": "Data",
			"width": 110,
		},
		{
			"label": _("Beneficiary Account Number"),
			"fieldname": "beneficiary_account_number",
			"fieldtype": "Data",
			"width": 170,
		},
		{
			"label": _("Instrument Amount"),
			"fieldname": "instrument_amount",
			"fieldtype": "Currency",
			"width": 130,
		},
		{
			"label": _("Beneficiary Name"),
			"fieldname": "beneficiary_name",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"label": _("Blank"),
			"fieldname": "blank_1",
			"fieldtype": "Data",
			"width": 60,
		},
		{
			"label": _("Blank"),
			"fieldname": "blank_2",
			"fieldtype": "Data",
			"width": 60,
		},
		{
			"label": _("Bene Address 1"),
			"fieldname": "bene_address_1",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Bene Address 2"),
			"fieldname": "bene_address_2",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Bene Address 3"),
			"fieldname": "bene_address_3",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Bene Address 4"),
			"fieldname": "bene_address_4",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Bene Address 5"),
			"fieldname": "bene_address_5",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Instruction Reference Number"),
			"fieldname": "instruction_reference_number",
			"fieldtype": "Data",
			"width": 160,
		},
		{
			"label": _("Customer Reference Number"),
			"fieldname": "customer_reference_number",
			"fieldtype": "Data",
			"width": 160,
		},
		{
			"label": _("Payment Details 1"),
			"fieldname": "payment_details_1",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 2"),
			"fieldname": "payment_details_2",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 3"),
			"fieldname": "payment_details_3",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 4"),
			"fieldname": "payment_details_4",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 5"),
			"fieldname": "payment_details_5",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 6"),
			"fieldname": "payment_details_6",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Payment Details 7"),
			"fieldname": "payment_details_7",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Blank"),
			"fieldname": "blank_3",
			"fieldtype": "Data",
			"width": 60,
		},
		{
			"label": _("Transaction Date"),
			"fieldname": "transaction_date",
			"fieldtype": "Data",
			"width": 110,
		},
		{
			"label": _("Blank"),
			"fieldname": "blank_4",
			"fieldtype": "Data",
			"width": 60,
		},
		{
			"label": _("IFSC Code"),
			"fieldname": "ifsc_code",
			"fieldtype": "Data",
			"width": 110,
		},
		{
			"label": _("Bene Bank Name"),
			"fieldname": "bene_bank_name",
			"fieldtype": "Data",
			"width": 160,
		},
		{
			"label": _("Bene Bank Branch Name"),
			"fieldname": "bene_bank_branch_name",
			"fieldtype": "Data",
			"width": 160,
		},
		{
			"label": _("Beneficiary Email ID"),
			"fieldname": "beneficiary_email",
			"fieldtype": "Data",
			"width": 180,
		},
		{
			"label": _("Open Notepad and Copy Below Data"),
			"fieldname": "notepad_data",
			"fieldtype": "Data",
			"width": 450,
		},
	]


def get_data(filters):
	data = []

	# ------------------------------------------------------------------------
	# SOURCE: Payment Entry
	# Only submitted Payment Entries for Suppliers are included.
	#
	# Transaction Type:
	# Payment Entry.custom_transaction_type
	#
	# Mapping:
	# HDFC -> I
	# NEFT -> N
	# RTGS -> R
	# IMPS -> M
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

		instruction_reference_number = row.get(
			"instruction_reference_number"
		)

		customer_reference_number = row.get(
			"customer_reference_number"
		)

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

		# RBI fixed-position notepad format.
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
	Fetch submitted Supplier Payment Entries.

	Transaction Type is taken directly from
	Payment Entry.custom_transaction_type and converted
	to the RBI single-letter code.
	"""

	conditions = {
		"docstatus": 1,
		"party_type": "Supplier",
	}

	if filters.get("from_date") and filters.get("to_date"):
		conditions["posting_date"] = [
			"between",
			[
				filters.get("from_date"),
				filters.get("to_date"),
			],
		]

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

		address = get_party_address(
			pe.party_type,
			pe.party,
		)

		pincode = (
			address.get("pincode")
			if address
			else ""
		)

		bank_acc_details = get_bank_account_details(
			pe.party_type,
			pe.party,
		)

		beneficiary_email = get_supplier_email(
			pe.party
		)

		# ------------------------------------------------------------
		# TRANSACTION TYPE
		# Source:
		# Payment Entry.custom_transaction_type
		#
		# HDFC -> I
		# NEFT -> N
		# RTGS -> R
		# IMPS -> M
		# ------------------------------------------------------------

		transaction_type = get_transaction_type_code(
			pe.custom_transaction_type
		)

		rows.append(
			{
				"transaction_type": transaction_type,

				"beneficiary_account_number":
					bank_acc_details.get(
						"bank_account_no"
					),

				"instrument_amount":
					pe.paid_amount,

				"beneficiary_name":
					pe.party_name,

				"bene_address_1":
					address.get("address_line1")
					if address
					else "",

				"bene_address_2":
					strip_pincode(
						address.get("address_line2")
						if address
						else "",
						pincode,
					),

				"bene_address_3":
					address.get("city")
					if address
					else "",

				"bene_address_4":
					address.get("county")
					if address
					else "",

				"bene_address_5":
					pincode,

				"instruction_reference_number":
					"",

				"customer_reference_number":
					pe.remarks,

				"payment_details_1": "",
				"payment_details_2": "",
				"payment_details_3": "",
				"payment_details_4": "",
				"payment_details_5": "",
				"payment_details_6": "",
				"payment_details_7": "",

				"transaction_date":
					formatdate(
						pe.posting_date,
						"dd/mm/yyyy"
					)
					if pe.posting_date
					else "",

				"ifsc_code":
					bank_acc_details.get(
						"custom_ifsc_code"
					),

				"bene_bank_name":
					bank_acc_details.get(
						"bank"
					),

				"bene_bank_branch_name":
					bank_acc_details.get(
						"branch_code"
					),

				"beneficiary_email":
					beneficiary_email,
			}
		)

	return rows


def get_transaction_type_code(custom_transaction_type):
	"""
	Map Payment Entry.custom_transaction_type
	to RBI Adapter Transaction Type.

	Payment Entry value -> RBI value

	HDFC -> I
	NEFT -> N
	RTGS -> R
	IMPS -> M
	"""

	mapping = {
		"HDFC": "I",
		"NEFT": "N",
		"RTGS": "R",
		"IMPS": "M",
	}

	return mapping.get(
		custom_transaction_type,
		"",
	)


def get_bank_account_details(party_type, party):
	"""
	Find Bank Account for the Supplier.

	Priority:
	1. Enabled + Default
	2. Enabled
	3. First available account
	"""

	if not party_type or not party:
		return {}

	bank_accounts = frappe.get_all(
		"Bank Account",
		filters={
			"party_type": party_type,
			"party": party,
		},
		fields=[
			"name",
			"bank_account_no",
			"bank",
			"custom_ifsc_code",
			"branch_code",
			"is_default",
			"disabled",
		],
	)

	if not bank_accounts:
		return {}

	# Prefer enabled default account.
	for acc in bank_accounts:
		if (
			acc.get("is_default")
			and not acc.get("disabled")
		):
			return acc

	# Otherwise prefer enabled account.
	for acc in bank_accounts:
		if not acc.get("disabled"):
			return acc

	# Fallback.
	return bank_accounts[0]


def get_supplier_email(party):
	"""
	Fetch Contact.email_id for the Supplier.

	First tries:
	-<supplier_id>

Then falls back to Dynamic Link.
	"""

	if not party:
		return ""

	# 1. Direct Contact naming convention.
	direct_contact_name = f"-{party}"

	email = frappe.db.get_value(
		"Contact",
		direct_contact_name,
		"email_id",
	)

	if email:
		return email

	# 2. Search through Dynamic Link.
	contact_links = frappe.get_all(
		"Dynamic Link",
		filters={
			"link_doctype": "Supplier",
			"link_name": party,
			"parenttype": "Contact",
		},
		fields=["parent"],
	)

	if not contact_links:
		return ""

	contact_names = [
		c.parent
		for c in contact_links
	]

	contacts = frappe.get_all(
		"Contact",
		filters={
			"name": ["in", contact_names],
		},
		fields=[
			"name",
			"email_id",
			"is_primary_contact",
		],
	)

	if not contacts:
		return ""

	# Prefer primary contact.
	for contact in contacts:
		if (
			contact.get("is_primary_contact")
			and contact.get("email_id")
		):
			return contact.get("email_id")

	# Otherwise first contact with email.
	for contact in contacts:
		if contact.get("email_id"):
			return contact.get("email_id")

	return ""


def get_party_address(party_type, party):
	"""
	Fetch Address linked to the Payment Entry party.
	"""

	if not party_type or not party:
		return {}

	address_name = frappe.db.get_value(
		"Dynamic Link",
		{
			"link_doctype": party_type,
			"link_name": party,
			"parenttype": "Address",
		},
		"parent",
	)

	if not address_name:
		return {}

	return (
		frappe.db.get_value(
			"Address",
			address_name,
			[
				"address_line1",
				"address_line2",
				"city",
				"county",
				"pincode",
			],
			as_dict=True,
		)
		or {}
	)


def strip_pincode(address_text, pincode):
	"""
	Remove pincode from Address Line 2 because
	pincode is separately shown in Bene Address 5.
	"""

	if not address_text:
		return address_text

	text = address_text

	if pincode:
		text = text.replace(
			str(pincode),
			"",
		)

	# Remove trailing separators.
	text = re.sub(
		r"[\s,\-]+$",
		"",
		text,
	)

	# Remove duplicate spaces.
	text = re.sub(
		r"\s{2,}",
		" ",
		text,
	)

	return text.strip()

