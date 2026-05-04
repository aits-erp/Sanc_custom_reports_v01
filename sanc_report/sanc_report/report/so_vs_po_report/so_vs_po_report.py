# import frappe


# def execute(filters=None):
#     columns = get_columns()
#     data = get_data(filters)
#     return columns, data


# def get_columns():
#     return [
#         {"label": "Sel", "fieldname": "idx", "width": 50},

#         {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100},
#         {"label": "Customer PO Number", "fieldname": "po_no", "width": 150},
#         {"label": "SO Category", "fieldname": "order_type", "width": 140},
#         {"label": "Sales Order", "fieldname": "so", "fieldtype": "Link", "options": "Sales Order", "width": 150},
#         {"label": "Customer Name", "fieldname": "customer_name", "width": 180},

#         {"label": "Part Number", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 120},
#         {"label": "Qty", "fieldname": "qty", "fieldtype": "Float", "width": 80},
#         {"label": "Unit Price", "fieldname": "rate", "fieldtype": "Currency", "width": 100},
#         {"label": "Total Price", "fieldname": "amount", "fieldtype": "Currency", "width": 120},

#         {"label": "Sales EDD", "fieldname": "sales_edd", "fieldtype": "Date", "width": 120},

#         {"label": "Qty Billed", "fieldname": "qty_billed", "fieldtype": "Float", "width": 100},
#         {"label": "Qty Pending", "fieldname": "qty_pending", "fieldtype": "Float", "width": 100},
#         {"label": "Amount Billed", "fieldname": "amount_billed", "fieldtype": "Currency", "width": 120},
#         {"label": "Amount Pending", "fieldname": "amount_pending", "fieldtype": "Currency", "width": 120},

#         {"label": "Supplier Code", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 150},
#         {"label": "Supplier Name", "fieldname": "supplier_name", "width": 180},
#         {"label": "PO Number", "fieldname": "po", "fieldtype": "Link", "options": "Purchase Order", "width": 150},

#         {"label": "PO Date", "fieldname": "po_date", "fieldtype": "Date", "width": 100},
#         {"label": "PO Item", "fieldname": "po_item", "width": 120},
#         {"label": "PO Qty", "fieldname": "po_qty", "fieldtype": "Float", "width": 100},

#         {"label": "Purchase EDD", "fieldname": "purchase_edd", "fieldtype": "Date", "width": 120},

#         # ✅ CUSTOM FIELDS
#         {"label": "In Transit", "fieldname": "in_transit", "fieldtype": "Check", "width": 100},
#         {"label": "AWB/MAWB Number", "fieldname": "awb_number", "width": 180},
#     ]


# def get_data(filters):

#     return frappe.db.sql("""
#         SELECT
#             ROW_NUMBER() OVER (ORDER BY so.transaction_date DESC) as idx,

#             so.transaction_date as date,
#             so.po_no,
#             so.order_type,
#             so.name as so,
#             so.customer_name,

#             soi.item_code,
#             soi.qty,
#             soi.rate,
#             soi.amount,

#             # MAX(soi.custom_edd) as sales_edd,
#             NULL as sales_edd,

#             IFNULL(SUM(sii.qty), 0) as qty_billed,
#             (soi.qty - IFNULL(SUM(sii.qty), 0)) as qty_pending,

#             IFNULL(SUM(sii.amount), 0) as amount_billed,
#             (soi.amount - IFNULL(SUM(sii.amount), 0)) as amount_pending,

#             sup.name as supplier,
#             sup.supplier_name,
#             po.name as po,
#             po.transaction_date as po_date,

#             poi.item_code as po_item,
#             poi.qty as po_qty,  
#             poi.expected_delivery_date as purchase_edd,

#             -- ✅ YOUR FIELDS
#             poi.custom_good_in_transit as in_transit,
#             po.custom_awbmawb_number as awb_number,

#             soi.name as soi_name

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
#             AND so.status NOT IN ('Cancelled', 'Closed')

#         GROUP BY
#             soi.name

#         HAVING
#             (soi.qty - IFNULL(SUM(sii.qty), 0)) > 0

#         ORDER BY
#             so.transaction_date DESC
#     """, as_dict=1)

# @frappe.whitelist()
# def update_in_transit(po_name, value):
#     frappe.db.set_value(
#         "Purchase Order",
#         po_name,
#         "custom__good_in_transit",
#         value
#     )
#     frappe.db.commit()





import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "Sel", "fieldname": "idx", "width": 50},

        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100},
        {"label": "Customer PO Number", "fieldname": "po_no", "width": 150},
        {"label": "SO Category", "fieldname": "order_type", "width": 140},
        {"label": "Sales Order", "fieldname": "so", "fieldtype": "Link", "options": "Sales Order", "width": 150},
        {"label": "Customer Name", "fieldname": "customer_name", "width": 180},

        {"label": "Part Number", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 120},
        {"label": "Qty", "fieldname": "qty", "fieldtype": "Float", "width": 80},
        {"label": "Unit Price", "fieldname": "rate", "fieldtype": "Currency", "width": 100},
        {"label": "Total Price", "fieldname": "amount", "fieldtype": "Currency", "width": 120},

        {"label": "Sales EDD", "fieldname": "sales_edd", "fieldtype": "Date", "width": 120},

        {"label": "Qty Billed", "fieldname": "qty_billed", "fieldtype": "Float", "width": 100},
        {"label": "Qty Pending", "fieldname": "qty_pending", "fieldtype": "Float", "width": 100},
        {"label": "Amount Billed", "fieldname": "amount_billed", "fieldtype": "Currency", "width": 120},
        {"label": "Amount Pending", "fieldname": "amount_pending", "fieldtype": "Currency", "width": 120},

        {"label": "Supplier Code", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 150},
        {"label": "Supplier Name", "fieldname": "supplier_name", "width": 180},
        {"label": "PO Number", "fieldname": "po", "fieldtype": "Link", "options": "Purchase Order", "width": 150},

        {"label": "PO Date", "fieldname": "po_date", "fieldtype": "Date", "width": 100},
        {"label": "PO Item", "fieldname": "po_item", "width": 120},
        {"label": "PO Qty", "fieldname": "po_qty", "fieldtype": "Float", "width": 100},

        {"label": "Purchase EDD", "fieldname": "purchase_edd", "fieldtype": "Date", "width": 120},

        {"label": "In Transit", "fieldname": "in_transit", "fieldtype": "Check", "width": 100},
        {"label": "AWB/MAWB Number", "fieldname": "awb_number", "width": 180},
    ]


def get_data(filters):

    return frappe.db.sql("""
        SELECT
            ROW_NUMBER() OVER (ORDER BY so.transaction_date DESC) as idx,

            so.transaction_date as date,
            so.po_no,
            so.order_type,
            so.name as so,
            so.customer_name,

            soi.item_code,
            soi.qty,
            soi.rate,
            soi.amount,

            NULL as sales_edd,

            IFNULL(SUM(sii.qty), 0) as qty_billed,
            (soi.qty - IFNULL(SUM(sii.qty), 0)) as qty_pending,

            IFNULL(SUM(sii.amount), 0) as amount_billed,
            (soi.amount - IFNULL(SUM(sii.amount), 0)) as amount_pending,

            sup.name as supplier,
            sup.supplier_name,
            po.name as po,
            po.transaction_date as po_date,

            poi.item_code as po_item,
            poi.qty as po_qty,
            poi.expected_delivery_date as purchase_edd,

            -- ✅ FIX: ITEM LEVEL FIELD
            poi.custom_good_in_transit as in_transit,
            po.custom_awbmawb_number as awb_number,

            -- ✅ REQUIRED FOR ROW UPDATE
            poi.name as poi_name

        FROM `tabSales Order` so

        INNER JOIN `tabSales Order Item` soi
            ON so.name = soi.parent

        LEFT JOIN `tabPurchase Order Item` poi
            ON poi.sales_order = so.name
            AND poi.item_code = soi.item_code

        LEFT JOIN `tabPurchase Order` po
            ON po.name = poi.parent
            AND po.docstatus = 1

        LEFT JOIN `tabSupplier` sup
            ON sup.name = po.supplier

        LEFT JOIN `tabSales Invoice Item` sii
            ON sii.sales_order = so.name
            AND sii.item_code = soi.item_code
            AND sii.docstatus = 1

        WHERE
            so.docstatus = 1
            AND so.status NOT IN ('Cancelled', 'Closed')

        GROUP BY
            soi.name

        HAVING
            (soi.qty - IFNULL(SUM(sii.qty), 0)) > 0

        ORDER BY
            so.transaction_date DESC
    """, as_dict=1)


# ✅ UPDATED FUNCTION (ROW LEVEL)
@frappe.whitelist()
def update_in_transit(poi_name, value):
    frappe.db.set_value(
        "Purchase Order Item",
        poi_name,
        "custom_good_in_transit",
        value
    )
    frappe.db.commit()
