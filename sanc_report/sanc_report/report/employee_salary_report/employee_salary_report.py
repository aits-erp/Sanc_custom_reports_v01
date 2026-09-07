
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
# 	format are shown as real empty columns.

# 	Transaction Type is mapped from:
# 	Salary Slip.custom_transaction_type

# 	Mapping:
# 	IMPS -> I
# 	NEFT -> N
# 	RTGS -> R
# 	UPI -> M
# 	MOBILE -> M
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

# 		{
# 			"label": _("Beneficiary Code"),
# 			"fieldname": "beneficiary_code",
# 			"fieldtype": "Data",
# 			"width": 110,
# 		},

# 		{
# 			"label": _("Beneficiary Account Number"),
# 			"fieldname": "beneficiary_account_number",
# 			"fieldtype": "Data",
# 			"width": 170,
# 		},

# 		{
# 			"label": _("Instrument Amount"),
# 			"fieldname": "instrument_amount",
# 			"fieldtype": "Currency",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Beneficiary Name"),
# 			"fieldname": "beneficiary_name",
# 			"fieldtype": "Data",
# 			"width": 200,
# 		},

# 		# Blank 1
# 		{
# 			"label": _("Blank"),
# 			"fieldname": "blank_1",
# 			"fieldtype": "Data",
# 			"width": 80,
# 		},

# 		# Blank 2
# 		{
# 			"label": _("Blank"),
# 			"fieldname": "blank_2",
# 			"fieldtype": "Data",
# 			"width": 80,
# 		},

# 		{
# 			"label": _("Bene Address 1"),
# 			"fieldname": "bene_address_1",
# 			"fieldtype": "Data",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Bene Address 2"),
# 			"fieldname": "bene_address_2",
# 			"fieldtype": "Data",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Bene Address 3"),
# 			"fieldname": "bene_address_3",
# 			"fieldtype": "Data",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Bene Address 4"),
# 			"fieldname": "bene_address_4",
# 			"fieldtype": "Data",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Bene Address 5"),
# 			"fieldname": "bene_address_5",
# 			"fieldtype": "Data",
# 			"width": 130,
# 		},

# 		{
# 			"label": _("Instruction Reference Number"),
# 			"fieldname": "instruction_reference_number",
# 			"fieldtype": "Data",
# 			"width": 160,
# 		},

# 		{
# 			"label": _("Customer Reference Number"),
# 			"fieldname": "customer_reference_number",
# 			"fieldtype": "Data",
# 			"width": 160,
# 		},

# 		{
# 			"label": _("Payment Details 1"),
# 			"fieldname": "payment_details_1",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 2"),
# 			"fieldname": "payment_details_2",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 3"),
# 			"fieldname": "payment_details_3",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 4"),
# 			"fieldname": "payment_details_4",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 5"),
# 			"fieldname": "payment_details_5",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 6"),
# 			"fieldname": "payment_details_6",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		{
# 			"label": _("Payment Details 7"),
# 			"fieldname": "payment_details_7",
# 			"fieldtype": "Data",
# 			"width": 120,
# 		},

# 		# Blank 3
# 		{
# 			"label": _("Blank"),
# 			"fieldname": "blank_3",
# 			"fieldtype": "Data",
# 			"width": 80,
# 		},

# 		{
# 			"label": _("Transaction Date"),
# 			"fieldname": "transaction_date",
# 			"fieldtype": "Data",
# 			"width": 110,
# 		},

# 		# Blank 4
# 		{
# 			"label": _("Blank"),
# 			"fieldname": "blank_4",
# 			"fieldtype": "Data",
# 			"width": 80,
# 		},

# 		{
# 			"label": _("IFSC Code"),
# 			"fieldname": "ifsc_code",
# 			"fieldtype": "Data",
# 			"width": 110,
# 		},

# 		{
# 			"label": _("Bene Bank Name"),
# 			"fieldname": "bene_bank_name",
# 			"fieldtype": "Data",
# 			"width": 160,
# 		},

# 		{
# 			"label": _("Bene Bank Branch Name"),
# 			"fieldname": "bene_bank_branch_name",
# 			"fieldtype": "Data",
# 			"width": 160,
# 		},

# 		{
# 			"label": _("Beneficiary Email ID"),
# 			"fieldname": "beneficiary_email",
# 			"fieldtype": "Data",
# 			"width": 180,
# 		},

# 		{
# 			"label": _("Open Notepad and Copy Below Data"),
# 			"fieldname": "notepad_data",
# 			"fieldtype": "Data",
# 			"width": 450,
# 		},
# 	]


# def get_data(filters):
# 	data = []

# 	raw_rows = get_raw_rows(filters)

# 	serial_no = 0

# 	for row in raw_rows:
# 		serial_no += 1

# 		transaction_type = row.get("transaction_type")

# 		beneficiary_code = serial_no
# 		beneficiary_account_number = row.get(
# 			"beneficiary_account_number"
# 		)
# 		instrument_amount = row.get("instrument_amount")
# 		beneficiary_name = row.get("beneficiary_name")

# 		bene_address_1 = row.get("bene_address_1")
# 		bene_address_2 = row.get("bene_address_2")
# 		bene_address_3 = row.get("bene_address_3")
# 		bene_address_4 = row.get("bene_address_4")
# 		bene_address_5 = row.get("bene_address_5")

# 		instruction_reference_number = row.get(
# 			"instruction_reference_number"
# 		)

# 		customer_reference_number = row.get(
# 			"customer_reference_number"
# 		)

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
# 		bene_bank_branch_name = row.get(
# 			"bene_bank_branch_name"
# 		)
# 		beneficiary_email = row.get("beneficiary_email")

# 		# RBI fixed-position Notepad data.
# 		# The 4 blank positions are preserved.

# 		notepad_data = ",".join(
# 			[
# 				cstr(transaction_type),
# 				cstr(beneficiary_code),
# 				cstr(beneficiary_account_number),
# 				cstr(instrument_amount),
# 				cstr(beneficiary_name),

# 				# Blank 1
# 				"",

# 				# Blank 2
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

# 				# Blank 3
# 				"",

# 				cstr(transaction_date),

# 				# Blank 4
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
# 				"beneficiary_account_number":
# 					beneficiary_account_number,
# 				"instrument_amount": instrument_amount,
# 				"beneficiary_name": beneficiary_name,

# 				"blank_1": "",
# 				"blank_2": "",

# 				"bene_address_1": bene_address_1,
# 				"bene_address_2": bene_address_2,
# 				"bene_address_3": bene_address_3,
# 				"bene_address_4": bene_address_4,
# 				"bene_address_5": bene_address_5,

# 				"instruction_reference_number":
# 					instruction_reference_number,

# 				"customer_reference_number":
# 					customer_reference_number,

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
# 				"bene_bank_branch_name":
# 					bene_bank_branch_name,
# 				"beneficiary_email": beneficiary_email,

# 				"notepad_data": notepad_data,
# 			}
# 		)

# 	return data


# def get_raw_rows(filters):
# 	"""
# 	Report is anchored on Salary Slip.

# 	Transaction Type:
# 	Salary Slip.custom_transaction_type

# 	Employee bank details:
# 	Employee master

# 	Journal Entry details:
# 	Salary Slip.payroll_entry ->
# 	Journal Entry Account ->
# 	Journal Entry
# 	"""

# 	rows = []

# 	salary_slips = frappe.get_all(
# 		"Salary Slip",
# 		filters={
# 			"posting_date": [
# 				"between",
# 				[
# 					filters.get("from_date"),
# 					filters.get("to_date"),
# 				],
# 			],
# 			"docstatus": 1,
# 		},
# 		fields=[
# 			"name",
# 			"employee",
# 			"employee_name",
# 			"net_pay",
# 			"payroll_entry",
# 			"custom_transaction_type",
# 		],
# 	)

# 	if not salary_slips:
# 		return rows

# 	# Build Payroll Entry -> Journal Entry lookup.

# 	payroll_entry_names = list(
# 		{
# 			s.payroll_entry
# 			for s in salary_slips
# 			if s.payroll_entry
# 		}
# 	)

# 	je_refs = (
# 		frappe.get_all(
# 			"Journal Entry Account",
# 			filters={
# 				"reference_type": "Payroll Entry",
# 				"reference_name": [
# 					"in",
# 					payroll_entry_names,
# 				],
# 			},
# 			fields=[
# 				"parent",
# 				"reference_name",
# 			],
# 		)
# 		if payroll_entry_names
# 		else []
# 	)

# 	je_names = list(
# 		{
# 			r.parent
# 			for r in je_refs
# 		}
# 	)

# 	je_details = (
# 		frappe.get_all(
# 			"Journal Entry",
# 			filters={
# 				"name": ["in", je_names],
# 				"docstatus": 1,
# 			},
# 			fields=[
# 				"name",
# 				"posting_date",
# 				"cheque_no",
# 				"user_remark",
# 			],
# 		)
# 		if je_names
# 		else []
# 	)

# 	je_by_name = {
# 		je.name: je
# 		for je in je_details
# 	}

# 	# Payroll Entry -> Journal Entry

# 	payroll_entry_to_je = {}

# 	for ref in je_refs:

# 		je = je_by_name.get(ref.parent)

# 		if not je:
# 			continue

# 		existing = payroll_entry_to_je.get(
# 			ref.reference_name
# 		)

# 		if (
# 			not existing
# 			or je.posting_date >= existing.posting_date
# 		):
# 			payroll_entry_to_je[
# 				ref.reference_name
# 			] = je

# 	# Build report rows.

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

# 		je = (
# 			payroll_entry_to_je.get(
# 				slip.payroll_entry
# 			)
# 			or frappe._dict()
# 		)

# 		rows.append(
# 			{
# 				# ONLY TRANSACTION TYPE CHANGE/SOURCE:
# 				# Salary Slip.custom_transaction_type
# 				"transaction_type":
# 					derive_transaction_type(
# 						slip.get(
# 							"custom_transaction_type"
# 						)
# 					),

# 				"beneficiary_account_number":
# 					emp.get("bank_ac_no"),

# 				"instrument_amount":
# 					slip.net_pay,

# 				"beneficiary_name":
# 					emp.get("employee_name")
# 					or slip.employee_name,

# 				"bene_address_1":
# 					emp.get(
# 						"current_accommodation_type"
# 					),

# 				"bene_address_2":
# 					emp.get(
# 						"permanent_accommodation_type"
# 					),

# 				"bene_address_3":
# 					emp.get("custom_city"),

# 				"bene_address_4":
# 					emp.get("custom_state"),

# 				"bene_address_5":
# 					emp.get("custom_country"),

# 				"instruction_reference_number":
# 					je.get("cheque_no"),

# 				"customer_reference_number":
# 					je.get("user_remark"),

# 				"payment_details_1": "",
# 				"payment_details_2": "",
# 				"payment_details_3": "",
# 				"payment_details_4": "",
# 				"payment_details_5": "",
# 				"payment_details_6": "",
# 				"payment_details_7": "",

# 				"transaction_date":
# 					formatdate(
# 						je.get("posting_date"),
# 						"dd/mm/yyyy",
# 					)
# 					if je.get("posting_date")
# 					else "",

# 				"ifsc_code":
# 					emp.get("ifsc_code"),

# 				"bene_bank_name":
# 					emp.get("bank_name"),

# 				"bene_bank_branch_name":
# 					"",

# 				"beneficiary_email":
# 					emp.get("personal_email"),
# 			}
# 		)

# 	return rows


# def derive_transaction_type(raw_value):
# 	"""
# 	Map Salary Slip.custom_transaction_type
# 	to RBI Transaction Type.

# 	Salary Slip value -> Report value

# 	IMPS   -> I
# 	NEFT   -> N
# 	RTGS   -> R
# 	UPI    -> M
# 	MOBILE -> M

# 	If the Salary Slip already contains I/N/R/M,
# 	it is kept as-is.
# 	"""

# 	if not raw_value:
# 		return ""

# 	value = cstr(raw_value).strip().upper()

# 	# Already an RBI code.
# 	if value in ("I", "N", "R", "M"):
# 		return value

# 	mapping = {
# 		"IMPS": "I",
# 		"NEFT": "N",
# 		"RTGS": "R",
# 		"UPI": "M",
# 		"MOBILE": "M",
# 	}

# 	return mapping.get(
# 		value,
# 		"",
# 	)


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
	exact positions the bank template expects.

	Transaction Type:
	- Comes from Salary Slip.custom_transaction_type
	- It is a Data field
	- It is editable directly in the report
	- The edited value is saved back to the same Salary Slip
	"""

	return [
		{
			"label": _("Transaction Type"),
			"fieldname": "transaction_type",
			"fieldtype": "Data",
			"width": 110,
			"editable": 1,
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

		# Blank 1
		{
			"label": _("Blank"),
			"fieldname": "blank_1",
			"fieldtype": "Data",
			"width": 80,
		},

		# Blank 2
		{
			"label": _("Blank"),
			"fieldname": "blank_2",
			"fieldtype": "Data",
			"width": 80,
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

		# Blank 3
		{
			"label": _("Blank"),
			"fieldname": "blank_3",
			"fieldtype": "Data",
			"width": 80,
		},

		{
			"label": _("Transaction Date"),
			"fieldname": "transaction_date",
			"fieldtype": "Data",
			"width": 110,
		},

		# Blank 4
		{
			"label": _("Blank"),
			"fieldname": "blank_4",
			"fieldtype": "Data",
			"width": 80,
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

		# Hidden technical field.
		# It does NOT appear in the report.
		# It is only used to know exactly which Salary Slip
		# must be updated when Transaction Type is edited.
		{
			"label": _("Salary Slip"),
			"fieldname": "_salary_slip_name",
			"fieldtype": "Data",
			"hidden": 1,
		},
	]


def get_data(filters):
	data = []

	raw_rows = get_raw_rows(filters)

	serial_no = 0

	for row in raw_rows:
		serial_no += 1

		transaction_type = row.get("transaction_type")

		beneficiary_code = serial_no
		beneficiary_account_number = row.get(
			"beneficiary_account_number"
		)
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
		bene_bank_branch_name = row.get(
			"bene_bank_branch_name"
		)
		beneficiary_email = row.get("beneficiary_email")

		# ------------------------------------------------------------
		# NOTEPAD DATA
		#
		# Transaction Type is the value currently stored in:
		# Salary Slip.custom_transaction_type
		#
		# The JS will replace the first field with the edited
		# report value before downloading.
		# ------------------------------------------------------------

		notepad_data = ",".join(
			[
				cstr(transaction_type),
				cstr(beneficiary_code),
				cstr(beneficiary_account_number),
				cstr(instrument_amount),
				cstr(beneficiary_name),

				# Blank 1
				"",

				# Blank 2
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

				# Blank 3
				"",

				cstr(transaction_date),

				# Blank 4
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

				"beneficiary_account_number":
					beneficiary_account_number,

				"instrument_amount":
					instrument_amount,

				"beneficiary_name":
					beneficiary_name,

				"blank_1": "",
				"blank_2": "",

				"bene_address_1":
					bene_address_1,

				"bene_address_2":
					bene_address_2,

				"bene_address_3":
					bene_address_3,

				"bene_address_4":
					bene_address_4,

				"bene_address_5":
					bene_address_5,

				"instruction_reference_number":
					instruction_reference_number,

				"customer_reference_number":
					customer_reference_number,

				"payment_details_1":
					payment_details_1,

				"payment_details_2":
					payment_details_2,

				"payment_details_3":
					payment_details_3,

				"payment_details_4":
					payment_details_4,

				"payment_details_5":
					payment_details_5,

				"payment_details_6":
					payment_details_6,

				"payment_details_7":
					payment_details_7,

				"blank_3": "",

				"transaction_date":
					transaction_date,

				"blank_4": "",

				"ifsc_code":
					ifsc_code,

				"bene_bank_name":
					bene_bank_name,

				"bene_bank_branch_name":
					bene_bank_branch_name,

				"beneficiary_email":
					beneficiary_email,

				"notepad_data":
					notepad_data,

				# Technical value only.
				# Hidden from the report UI.
				"_salary_slip_name":
					row.get("_salary_slip_name"),
			}
		)

	return data


def get_raw_rows(filters):
	"""
	Report is anchored on Salary Slip.

	Transaction Type:
	Salary Slip.custom_transaction_type

	The raw value is NOT converted to I/N/R/M.
	It is displayed exactly as stored in the Salary Slip Data field.
	"""

	rows = []

	salary_slips = frappe.get_all(
		"Salary Slip",
		filters={
			"posting_date": [
				"between",
				[
					filters.get("from_date"),
					filters.get("to_date"),
				],
			],
			"docstatus": 1,
		},
		fields=[
			"name",
			"employee",
			"employee_name",
			"net_pay",
			"payroll_entry",
			"custom_transaction_type",
		],
	)

	if not salary_slips:
		return rows

	# ------------------------------------------------------------
	# Payroll Entry -> Journal Entry
	# ------------------------------------------------------------

	payroll_entry_names = list(
		{
			s.payroll_entry
			for s in salary_slips
			if s.payroll_entry
		}
	)

	je_refs = (
		frappe.get_all(
			"Journal Entry Account",
			filters={
				"reference_type": "Payroll Entry",
				"reference_name": [
					"in",
					payroll_entry_names,
				],
			},
			fields=[
				"parent",
				"reference_name",
			],
		)
		if payroll_entry_names
		else []
	)

	je_names = list(
		{
			r.parent
			for r in je_refs
		}
	)

	je_details = (
		frappe.get_all(
			"Journal Entry",
			filters={
				"name": ["in", je_names],
				"docstatus": 1,
			},
			fields=[
				"name",
				"posting_date",
				"cheque_no",
				"user_remark",
			],
		)
		if je_names
		else []
	)

	je_by_name = {
		je.name: je
		for je in je_details
	}

	payroll_entry_to_je = {}

	for ref in je_refs:

		je = je_by_name.get(ref.parent)

		if not je:
			continue

		existing = payroll_entry_to_je.get(
			ref.reference_name
		)

		if (
			not existing
			or je.posting_date >= existing.posting_date
		):
			payroll_entry_to_je[
				ref.reference_name
			] = je

	# ------------------------------------------------------------
	# Salary Slip rows
	# ------------------------------------------------------------

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

		je = (
			payroll_entry_to_je.get(
				slip.payroll_entry
			)
			or frappe._dict()
		)

		rows.append(
			{
				# ------------------------------------------------
				# TRANSACTION TYPE
				#
				# Directly from Salary Slip Data field:
				# custom_transaction_type
				#
				# NO I/N/R/M mapping is done.
				# ------------------------------------------------

				"transaction_type":
					cstr(
						slip.get(
							"custom_transaction_type"
						)
						or ""
					),

				"beneficiary_account_number":
					emp.get("bank_ac_no"),

				"instrument_amount":
					slip.net_pay,

				"beneficiary_name":
					emp.get("employee_name")
					or slip.employee_name,

				"bene_address_1":
					emp.get(
						"current_accommodation_type"
					),

				"bene_address_2":
					emp.get(
						"permanent_accommodation_type"
					),

				"bene_address_3":
					emp.get("custom_city"),

				"bene_address_4":
					emp.get("custom_state"),

				"bene_address_5":
					emp.get("custom_country"),

				"instruction_reference_number":
					je.get("cheque_no"),

				"customer_reference_number":
					je.get("user_remark"),

				"payment_details_1": "",
				"payment_details_2": "",
				"payment_details_3": "",
				"payment_details_4": "",
				"payment_details_5": "",
				"payment_details_6": "",
				"payment_details_7": "",

				"transaction_date":
					formatdate(
						je.get("posting_date"),
						"dd/mm/yyyy",
					)
					if je.get("posting_date")
					else "",

				"ifsc_code":
					emp.get("ifsc_code"),

				"bene_bank_name":
					emp.get("bank_name"),

				"bene_bank_branch_name":
					"",

				"beneficiary_email":
					emp.get("personal_email"),

				# Exact Salary Slip document name.
				# Used when saving the edited Transaction Type.
				"_salary_slip_name":
					slip.name,
			}
		)

	return rows


@frappe.whitelist()
def update_salary_slip_transaction_type(
	salary_slip,
	transaction_type,
):
	"""
	Save the edited Transaction Type back to
	the exact Salary Slip.

	Salary Slip.custom_transaction_type is a Data field,
	so any text value is accepted.
	"""

	if not salary_slip:
		frappe.throw(
			_("Salary Slip is required.")
		)

	if not frappe.db.exists(
		"Salary Slip",
		salary_slip,
	):
		frappe.throw(
			_("Salary Slip {0} does not exist.").format(
				salary_slip
			)
		)

	# Check write permission.
	if not frappe.has_permission(
		"Salary Slip",
		doc=salary_slip,
		pperm="write",
	):
		frappe.throw(
			_("You do not have permission to update Salary Slip {0}.").format(
				salary_slip
			),
			frappe.PermissionError,
		)

	transaction_type = cstr(
		transaction_type or ""
	).strip()

	# Save directly to the Salary Slip.
	#
	# db_set is intentional because Salary Slip is submitted
	# and this is only updating the custom Data field.
	frappe.db.set_value(
		"Salary Slip",
		salary_slip,
		"custom_transaction_type",
		transaction_type,
		update_modified=True,
	)

	return {
		"success": True,
		"salary_slip": salary_slip,
		"transaction_type": transaction_type,
	}