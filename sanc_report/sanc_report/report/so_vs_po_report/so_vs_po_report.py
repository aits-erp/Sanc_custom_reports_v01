# # import frappe

# # def execute(filters=None): 
# #     columns = get_columns()
# #     data = get_data(filters)
# #     return columns, data


# # def get_columns():
# #     return [
# #         # {"label": "Sel", "fieldname": "idx", "width": 50},

# #         {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100},
# #         {"label": "Customer PO Number", "fieldname": "po_no", "width": 150},
# #         {"label": "SO Category", "fieldname": "order_type", "width": 140},
# #         {"label": "Sales Order", "fieldname": "so", "fieldtype": "Link", "options": "Sales Order", "width": 150},
# #         {"label": "Customer Name", "fieldname": "customer_name", "width": 180},

# #         # ✅ Certificate from Sales Order (parent)
# #         {"label": "Certificate", "fieldname": "custom_certificate", "fieldtype": "Select", "options": "\nTC\nCC\nTC/CC", "width": 120},

# #         {"label": "Part Number", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 120},
# #         {"label": "Qty", "fieldname": "qty", "fieldtype": "Float", "width": 80},
# #         {"label": "Unit Price", "fieldname": "rate", "fieldtype": "Currency", "width": 100},
# #         {"label": "Total Price", "fieldname": "amount", "fieldtype": "Currency", "width": 120},

# #         {"label": "Sales EDD", "fieldname": "custom_edd", "fieldtype": "Date", "width": 120},

# #         {"label": "Qty Billed", "fieldname": "qty_billed", "fieldtype": "Float", "width": 100},
# #         {"label": "Qty Pending", "fieldname": "qty_pending", "fieldtype": "Float", "width": 100},
# #         {"label": "Amount Billed", "fieldname": "amount_billed", "fieldtype": "Currency", "width": 120},
# #         {"label": "Amount Pending", "fieldname": "amount_pending", "fieldtype": "Currency", "width": 120},

# #         {"label": "Supplier Code", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 150},
# #         {"label": "Supplier Name", "fieldname": "supplier_name", "width": 180},
# #         {"label": "PO Number", "fieldname": "po", "fieldtype": "Link", "options": "Purchase Order", "width": 150},

# #         {"label": "PO Date", "fieldname": "po_date", "fieldtype": "Date", "width": 100},
# #         {"label": "PO Item", "fieldname": "po_item", "width": 120},
# #         {"label": "PO Qty", "fieldname": "po_qty", "fieldtype": "Float", "width": 100},

# #         {"label": "Purchase EDD", "fieldname": "expected_delivery_date", "fieldtype": "Date", "width": 120},

# #         {"label": "In Transit", "fieldname": "in_transit", "fieldtype": "Check", "width": 100},
# #         {"label": "AWB/MAWB Number", "fieldname": "awb_number", "width": 180},

# #         {"label": "Remark", "fieldname": "custom_remark", "width": 200},
# #     ]


# # def get_data(filters):

# #     return frappe.db.sql("""
# #         SELECT
# #             ROW_NUMBER() OVER (ORDER BY so.transaction_date DESC) as idx,

# #             so.transaction_date as date,
# #             so.po_no,
# #             so.order_type,
# #             so.name as so,
# #             so.customer_name,

# #             -- ✅ FIXED: from tabSales Order (not soi)
# #             so.custom_certificate as custom_certificate,

# #             soi.item_code,
# #             soi.qty,
# #             soi.rate,
# #             soi.amount,

# #             soi.custom_edd as custom_edd,

# #             soi.delivered_qty AS qty_billed,
# #             (soi.qty - soi.delivered_qty) AS qty_pending,

# #             IFNULL(SUM(sii.amount), 0) as amount_billed,
# #             (soi.amount - IFNULL(SUM(sii.amount), 0)) as amount_pending,

# #             sup.name as supplier,
# #             sup.supplier_name,
# #             po.name as po,
# #             po.transaction_date as po_date,

# #             poi.item_code as po_item,
# #             poi.qty as po_qty,

# #             poi.expected_delivery_date as expected_delivery_date,

# #             poi.custom_good_in_transit as in_transit,
# #             poi.custom_awbmawb_number as awb_number,

# #             poi.custom_remark as custom_remark,

# #             poi.name as poi_name

# #         FROM `tabSales Order` so

# #         INNER JOIN `tabSales Order Item` soi
# #             ON so.name = soi.parent

# #         LEFT JOIN `tabPurchase Order Item` poi
# #             ON poi.sales_order = so.name
# #             AND poi.item_code = soi.item_code

# #         LEFT JOIN `tabPurchase Order` po
# #             ON po.name = poi.parent
# #             AND po.docstatus = 1

# #         LEFT JOIN `tabSupplier` sup
# #             ON sup.name = po.supplier

# #         LEFT JOIN `tabSales Invoice Item` sii
# #             ON sii.sales_order = so.name
# #             AND sii.item_code = soi.item_code
# #             AND sii.docstatus = 1

# #         WHERE
# #             so.docstatus = 1
# #             AND so.status NOT IN ('Cancelled', 'Close', 'Hold')

# #         GROUP BY
# #             soi.name

# #         HAVING
# #             (soi.qty - IFNULL(SUM(sii.qty), 0)) > 0

# #         ORDER BY
# #             so.transaction_date DESC
# #     """, as_dict=1)


# # # -------------------------
# # # UPDATE FUNCTIONS
# # # -------------------------
# # @frappe.whitelist()
# # def update_in_transit(poi_name, value):
# #     frappe.db.set_value(
# #         "Purchase Order Item",
# #         poi_name,
# #         "custom_good_in_transit",
# #         value
# #     )
# #     frappe.db.commit()


# # @frappe.whitelist()
# # def update_awb_number(poi_name, awb_number):
# #     frappe.db.set_value(
# #         "Purchase Order Item",
# #         poi_name,
# #         "custom_awbmawb_number",
# #         awb_number
# #     )
# #     frappe.db.commit()


# # @frappe.whitelist()
# # def update_remark(poi_name, remark):
# #     frappe.db.set_value(
# #         "Purchase Order Item",
# #         poi_name,
# #         "custom_remark",
# #         remark
# #     )
# #     frappe.db.commit()


# import frappe


# def execute(filters=None):
#     columns = get_columns()
#     data = get_data(filters)

#     # ✅ Append totals row at the bottom
#     if data:
#         totals = get_totals_row(data)
#         data.append(totals)

#     return columns, data


# def get_columns():
#     return [
#         {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100},
#         {"label": "Customer PO Number", "fieldname": "po_no", "width": 150},
#         {"label": "SO Category", "fieldname": "order_type", "width": 140},
#         {"label": "Sales Order", "fieldname": "so", "fieldtype": "Link", "options": "Sales Order", "width": 150},
#         {"label": "Customer Name", "fieldname": "customer_name", "width": 180},

#         # Certificate from Sales Order (parent)
#         {"label": "Certificate", "fieldname": "custom_certificate", "fieldtype": "Select", "options": "\nTC\nCC\nTC/CC", "width": 120},

#         {"label": "Part Number", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 120},
#         {"label": "Qty", "fieldname": "qty", "fieldtype": "Float", "width": 80},
#         {"label": "Unit Price", "fieldname": "rate", "fieldtype": "Currency", "width": 100},
#         {"label": "Total Price", "fieldname": "amount", "fieldtype": "Currency", "width": 120},

#         {"label": "Sales EDD", "fieldname": "custom_edd", "fieldtype": "Date", "width": 120},

#         {"label": "Qty Billed", "fieldname": "qty_billed", "fieldtype": "Float", "width": 100},
#         {"label": "Qty Pending", "fieldname": "qty_pending", "fieldtype": "Float", "width": 100},
#         {"label": "Amount Billed", "fieldname": "amount_billed", "fieldtype": "Currency", "width": 120},

#         # ✅ FIXED: pending_amount now uses billed_amt * conversion_rate (same as Sales Order Analysis)
#         {"label": "Amount Pending", "fieldname": "amount_pending", "fieldtype": "Currency", "width": 120},

#         {"label": "Supplier Code", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 150},
#         {"label": "Supplier Name", "fieldname": "supplier_name", "width": 180},
#         {"label": "PO Number", "fieldname": "po", "fieldtype": "Link", "options": "Purchase Order", "width": 150},

#         {"label": "PO Date", "fieldname": "po_date", "fieldtype": "Date", "width": 100},
#         {"label": "PO Item", "fieldname": "po_item", "width": 120},
#         {"label": "PO Qty", "fieldname": "po_qty", "fieldtype": "Float", "width": 100},

#         {"label": "Purchase EDD", "fieldname": "expected_delivery_date", "fieldtype": "Date", "width": 120},

#         {"label": "In Transit", "fieldname": "in_transit", "fieldtype": "Check", "width": 100},
#         {"label": "AWB/MAWB Number", "fieldname": "awb_number", "width": 180},

#         {"label": "Remark", "fieldname": "custom_remark", "width": 200},
#     ]


# def get_conditions(filters):
#     """Build dynamic WHERE conditions from filters — mirrors Sales Order Analysis pattern."""
#     conditions = ""

#     if filters.get("from_date") and filters.get("to_date"):
#         conditions += " AND so.transaction_date BETWEEN %(from_date)s AND %(to_date)s"

#     if filters.get("company"):
#         conditions += " AND so.company = %(company)s"

#     if filters.get("sales_order"):
#         conditions += " AND so.name IN %(sales_order)s"

#     if filters.get("status"):
#         conditions += " AND so.status IN %(status)s"

#     if filters.get("purchase_order"):
#         conditions += " AND po.name IN %(purchase_order)s"

#     return conditions


# def get_data(filters):
#     if not filters:
#         filters = {}

#     # Ensure tuple for IN clause if list is passed
#     if filters.get("sales_order") and isinstance(filters["sales_order"], list):
#         filters["sales_order"] = tuple(filters["sales_order"])

#     if filters.get("purchase_order") and isinstance(filters["purchase_order"], list):
#         filters["purchase_order"] = tuple(filters["purchase_order"])

#     if filters.get("status") and isinstance(filters["status"], list):
#         filters["status"] = tuple(filters["status"])

#     conditions = get_conditions(filters)

#     return frappe.db.sql("""
#         SELECT
#             ROW_NUMBER() OVER (ORDER BY so.transaction_date DESC) AS idx,

#             so.transaction_date AS date,
#             so.po_no,
#             so.order_type,
#             so.name AS so,
#             so.customer_name,

#             -- Certificate from Sales Order (parent)
#             so.custom_certificate AS custom_certificate,

#             soi.item_code,
#             soi.qty,
#             soi.rate,
#             soi.amount,

#             soi.custom_edd AS custom_edd,

#             -- Qty Billed: sum from Sales Invoice Items
#            soi.billed_qty AS qty_billed,

#             -- Qty Pending: ordered qty minus billed qty
#             (soi.qty - soi.billed_qty) AS qty_pending,

#             -- Amount Billed: billed_amt * conversion_rate (same as Sales Order Analysis standard report)
#             (soi.billed_amt * IFNULL(so.conversion_rate, 1)) AS amount_billed,

#             -- FIXED Amount Pending: base_amount minus (billed_amt * conversion_rate)
#             -- Previously used SUM(sii.amount) which double-counts on multiple invoice lines.
#             -- Standard ERPNext Sales Order Analysis uses soi.billed_amt (already aggregated on the SO item)
#             -- so no GROUP BY inflation occurs.
#             (soi.base_amount - (soi.billed_amt * IFNULL(so.conversion_rate, 1))) AS amount_pending,

#             sup.name AS supplier,
#             sup.supplier_name,
#             po.name AS po,
#             po.transaction_date AS po_date,

#             poi.item_code AS po_item,
#             poi.qty AS po_qty,

#             poi.expected_delivery_date AS expected_delivery_date,

#             poi.custom_good_in_transit AS in_transit,
#             poi.custom_awbmawb_number AS awb_number,

#             poi.custom_remark AS custom_remark,

#             poi.name AS poi_name

#         FROM `tabSales Order` so

#         INNER JOIN `tabSales Order Item` soi
#             ON so.name = soi.parent

#         LEFT JOIN `tabPurchase Order Item` poi
#             ON poi.sales_order = so.name
#             AND poi.item_code = soi.item_code

#         LEFT JOIN `tabPurchase Order` po
#             ON po.name = poi.parent
#             AND po.docstatus = 1

#         LEFT JOIN `tabSupplier` sup
#             ON sup.name = po.supplier

#         LEFT JOIN `tabSales Invoice Item` sii
#             ON sii.sales_order = so.name
#             AND sii.item_code = soi.item_code
#             AND sii.docstatus = 1

#         WHERE
#             so.docstatus = 1
#             AND so.status NOT IN ('Cancelled', 'Close', 'Hold')
#             {conditions}

#         GROUP BY
#             soi.name

#         HAVING
#             (soi.qty - IFNULL(SUM(sii.qty), 0)) > 0

#         ORDER BY
#             so.transaction_date DESC
#     """.format(conditions=conditions), filters, as_dict=1)


# def get_totals_row(data):
#     """
#     Build a totals summary row (same pattern as ERPNext Sales Order Analysis).
#     Only numeric/currency fields are summed; label fields show a bold 'Total' marker.
#     """
#     totals = {
#         "date": None,
#         "po_no": None,
#         "order_type": None,
#         "so": None,
#         "customer_name": "Total",
#         "custom_certificate": None,
#         "item_code": None,
#         "qty": 0,
#         "rate": None,
#         "amount": 0,
#         "custom_edd": None,
#         "qty_billed": 0,
#         "qty_pending": 0,
#         "amount_billed": 0,
#         "amount_pending": 0,
#         "supplier": None,
#         "supplier_name": None,
#         "po": None,
#         "po_date": None,
#         "po_item": None,
#         "po_qty": 0,
#         "expected_delivery_date": None,
#         "in_transit": None,
#         "awb_number": None,
#         "custom_remark": None,
#         "poi_name": None,
#         "is_total_row": True,
#     }

#     for row in data:
#         totals["qty"]            += (row.get("qty") or 0)
#         totals["amount"]         += (row.get("amount") or 0)
#         totals["qty_billed"]     += (row.get("qty_billed") or 0)
#         totals["qty_pending"]    += (row.get("qty_pending") or 0)
#         totals["amount_billed"]  += (row.get("amount_billed") or 0)
#         totals["amount_pending"] += (row.get("amount_pending") or 0)
#         totals["po_qty"]         += (row.get("po_qty") or 0)

#     return totals


# # -------------------------
# # UPDATE FUNCTIONS
# # -------------------------

# @frappe.whitelist()
# def update_in_transit(poi_name, value):
#     frappe.db.set_value(
#         "Purchase Order Item",
#         poi_name,
#         "custom_good_in_transit",
#         value
#     )
#     frappe.db.commit()


# @frappe.whitelist()
# def update_awb_number(poi_name, awb_number):
#     frappe.db.set_value(
#         "Purchase Order Item",
#         poi_name,
#         "custom_awbmawb_number",
#         awb_number
#     )
#     frappe.db.commit()


# @frappe.whitelist()
# def update_remark(poi_name, remark):
#     frappe.db.set_value(
#         "Purchase Order Item",
#         poi_name,
#         "custom_remark",
#         remark
#     )
#     frappe.db.commit()





import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    if data:
        totals = get_totals_row(data)
        data.append(totals)

    return columns, data


def get_columns():
    return [
        {"label": "Date",                "fieldname": "date",                   "fieldtype": "Date",     "width": 100},
        {"label": "Customer PO Number",  "fieldname": "po_no",                  "fieldtype": "Data",     "width": 150},
        {"label": "SO Category",         "fieldname": "order_type",             "fieldtype": "Data",     "width": 140},
        {"label": "Sales Order",         "fieldname": "so",                     "fieldtype": "Link",     "options": "Sales Order",  "width": 150},
        {"label": "Customer Name",       "fieldname": "customer_name",          "fieldtype": "Data",     "width": 180},
        {"label": "Certificate",         "fieldname": "custom_certificate",     "fieldtype": "Select",   "options": "\nTC\nCC\nTC/CC", "width": 120},
        {"label": "Part Number",         "fieldname": "item_code",              "fieldtype": "Link",     "options": "Item",         "width": 120},
        {"label": "Qty",                 "fieldname": "qty",                    "fieldtype": "Float",    "width": 80},
        {"label": "Unit Price",          "fieldname": "rate",                   "fieldtype": "Currency", "width": 100},
        {"label": "Total Price",         "fieldname": "amount",                 "fieldtype": "Currency", "width": 120},
        {"label": "Sales EDD",           "fieldname": "custom_edd",             "fieldtype": "Date",     "width": 120},

        # ── Billed / Pending — same formula as Sales Order Analysis ──
        {"label": "Qty Billed",          "fieldname": "qty_billed",             "fieldtype": "Float",    "width": 100},
        {"label": "Qty Pending",         "fieldname": "qty_pending",            "fieldtype": "Float",    "width": 100},
        {"label": "Amount Billed",       "fieldname": "amount_billed",          "fieldtype": "Currency", "width": 120},
        {"label": "Amount Pending",      "fieldname": "amount_pending",         "fieldtype": "Currency", "width": 120},

        {"label": "Supplier Code",       "fieldname": "supplier",               "fieldtype": "Link",     "options": "Supplier",     "width": 150},
        {"label": "Supplier Name",       "fieldname": "supplier_name",          "fieldtype": "Data",     "width": 180},
        {"label": "PO Number",           "fieldname": "po",                     "fieldtype": "Link",     "options": "Purchase Order","width": 150},
        {"label": "PO Date",             "fieldname": "po_date",                "fieldtype": "Date",     "width": 100},
        {"label": "PO Item",             "fieldname": "po_item",                "fieldtype": "Data",     "width": 120},
        {"label": "PO Qty",              "fieldname": "po_qty",                 "fieldtype": "Float",    "width": 100},
        {"label": "Purchase EDD",        "fieldname": "expected_delivery_date", "fieldtype": "Date",     "width": 120},
        {"label": "In Transit",          "fieldname": "in_transit",             "fieldtype": "Check",    "width": 100},
        {"label": "AWB/MAWB Number",     "fieldname": "awb_number",             "fieldtype": "Data",     "width": 180},
        {"label": "Remark",              "fieldname": "custom_remark",          "fieldtype": "Data",     "width": 200},
    ]


def get_conditions(filters):
    conditions = ""

    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND so.transaction_date BETWEEN %(from_date)s AND %(to_date)s"

    if filters.get("company"):
        conditions += " AND so.company = %(company)s"

    if filters.get("sales_order") and len(filters.get("sales_order")) > 0:
        conditions += " AND so.name IN %(sales_order)s"

    if filters.get("status") and len(filters.get("status")) > 0:
        conditions += " AND so.status IN %(status)s"
    if filters.get("purchase_order") and len(filters.get("purchase_order")) > 0:
        conditions += " AND po.name IN %(purchase_order)s"
    return conditions


def get_data(filters):
    if not filters:
        filters = {}

    # Convert lists to tuples for SQL IN clause
    for key in ("sales_order", "purchase_order", "status"):
        if filters.get(key) and isinstance(filters[key], list):
            filters[key] = tuple(filters[key])

    conditions = get_conditions(filters)

    data = frappe.db.sql("""
        SELECT
            so.transaction_date                                         AS date,
            so.po_no,
            so.order_type,
            so.name                                                     AS so,
            so.customer_name,
            so.custom_certificate,

            soi.item_code,
            soi.qty,
            soi.rate,
            soi.base_amount                                             AS amount,
            soi.custom_edd,

soi.delivered_qty AS qty_billed,

(soi.qty - IFNULL(soi.delivered_qty, 0)) AS qty_pending,
0 AS amount_billed,

soi.base_amount AS amount_pending,

            sup.name                                                    AS supplier,
            sup.supplier_name,
            po.name                                                     AS po,
            po.transaction_date                                         AS po_date,

            poi.item_code                                               AS po_item,
            poi.qty                                                     AS po_qty,
            poi.expected_delivery_date,
            poi.custom_good_in_transit                                  AS in_transit,
            poi.custom_awbmawb_number                                   AS awb_number,
            poi.custom_remark,
            poi.name                                                    AS poi_name

        FROM `tabSales Order` so

        -- ── Join SO items — same as standard report ──
        INNER JOIN `tabSales Order Item` soi
            ON soi.parent = so.name

        -- ── PO item matched by SO name + item code ──
        LEFT JOIN `tabPurchase Order Item` poi
             ON poi.sales_order = so.name
            AND poi.sales_order_item = soi.name

        -- ── PO header — only submitted ──
        LEFT JOIN `tabPurchase Order` po
            ON po.name      = poi.parent
            AND po.docstatus = 1

        LEFT JOIN `tabSupplier` sup
            ON sup.name = po.supplier

        -- ── SI items joined on so_detail (soi.name) — same as standard report ──
        -- This avoids double-counting when multiple invoice lines exist
        
       WHERE
    so.docstatus = 1
    AND so.status NOT IN ('Cancelled', 'Closed')
    {conditions}

GROUP BY soi.name

HAVING
(
    (soi.qty - IFNULL(soi.delivered_qty, 0)) > 0
    OR
    soi.base_amount > 0
)
ORDER BY so.transaction_date DESC, so.name, soi.idx

    """.format(conditions=conditions), filters, as_dict=1)

    return data


def get_totals_row(data):
    totals = {
        "date":                   None,
        "po_no":                  None,
        "order_type":             None,
        "so":                     None,
        "customer_name":          "Total",
        "custom_certificate":     None,
        "item_code":              None,
        "qty":                    0,
        "rate":                   None,
        "amount":                 0,
        "custom_edd":             None,
        "qty_billed":             0,
        "qty_pending":            0,
        "amount_billed":          0,
        "amount_pending":         0,
        "supplier":               None,
        "supplier_name":          None,
        "po":                     None,
        "po_date":                None,
        "po_item":                None,
        "po_qty":                 0,
        "expected_delivery_date": None,
        "in_transit":             None,
        "awb_number":             None,
        "custom_remark":          None,
        "poi_name":               None,
        "is_total_row":           True,
    }

    for row in data:
        totals["qty"]            += (row.get("qty")            or 0)
        totals["amount"]         += (row.get("amount")         or 0)
        totals["qty_billed"]     += (row.get("qty_billed")     or 0)
        totals["qty_pending"]    += (row.get("qty_pending")    or 0)
        totals["amount_billed"]  += (row.get("amount_billed")  or 0)
        totals["amount_pending"] += (row.get("amount_pending") or 0)
        totals["po_qty"]         += (row.get("po_qty")         or 0)

    return totals


# ── Whitelisted update helpers ─────────────────────────────────────────────────

@frappe.whitelist()
def update_in_transit(poi_name, value):
    frappe.db.set_value("Purchase Order Item", poi_name, "custom_good_in_transit", value)
    frappe.db.commit()


@frappe.whitelist()
def update_awb_number(poi_name, awb_number):
    frappe.db.set_value("Purchase Order Item", poi_name, "custom_awbmawb_number", awb_number)
    frappe.db.commit()

# hi
@frappe.whitelist()
def update_remark(poi_name, remark):
    frappe.db.set_value("Purchase Order Item", poi_name, "custom_remark", remark)
    frappe.db.commit()