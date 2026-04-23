import frappe
from datetime import datetime
from dateutil.relativedelta import relativedelta


def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data


# ---------------- BASE DATE ----------------
def get_base_date(filters):

    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    if filters.get("month"):
        month = month_map.get(filters.get("month"))
        year = datetime.now().year
        return datetime(year, month, 1)

    elif filters.get("to_date"):
        return datetime.strptime(filters.get("to_date"), "%Y-%m-%d")

    return datetime.now()


# ---------------- COLUMNS ----------------
def get_columns(filters):

    base_date = get_base_date(filters)

    m1 = (base_date - relativedelta(months=1)).strftime("%b-%y")
    m2 = (base_date - relativedelta(months=2)).strftime("%b-%y")
    m3 = (base_date - relativedelta(months=3)).strftime("%b-%y")

    return [
        {"label": "MODEL CODE", "fieldname": "item_code", "width": 180},

        {"label": f"Sales {m3}", "fieldname": "m3", "fieldtype": "Float", "width": 110},
        {"label": f"Sales {m2}", "fieldname": "m2", "fieldtype": "Float", "width": 110},
        {"label": f"Sales {m1}", "fieldname": "m1", "fieldtype": "Float", "width": 110},

        {"label": "SANC STOCK", "fieldname": "stock", "fieldtype": "Float", "width": 140},

        {"label": "PENDING SALES ORDER QTY", "fieldname": "pending_so", "fieldtype": "Float", "width": 200},

        {"label": "PENDING PURCHASE ORDER", "fieldname": "pending_po", "fieldtype": "Float", "width": 200},

        {"label": "IN TRANSIT", "fieldname": "in_transit", "fieldtype": "Float", "width": 150},

        {"label": "FREE STOCK", "fieldname": "free_stock", "fieldtype": "Float", "width": 140},
    ]


# ---------------- DATA ----------------
def get_data(filters):

    base_date = get_base_date(filters)

    m1_start = base_date - relativedelta(months=1)
    m2_start = base_date - relativedelta(months=2)
    m3_start = base_date - relativedelta(months=3)

    conditions = ""
    if filters.get("stock_category"):
        conditions += " AND i.custom_stock_categorization = %(stock_category)s"

    items = frappe.db.sql(f"""
        SELECT item_code
        FROM `tabItem` i
        WHERE i.disabled = 0 {conditions}
    """, filters, as_dict=True)

    data = []

    for item in items:
        code = item.item_code

        m1 = get_sales(code, m1_start, base_date)
        m2 = get_sales(code, m2_start, m1_start)
        m3 = get_sales(code, m3_start, m2_start)

        stock = frappe.db.sql("""
            SELECT SUM(actual_qty)
            FROM `tabStock Ledger Entry`
            WHERE item_code=%s AND posting_date <= %s
        """, (code, base_date))[0][0] or 0

        pending_so = frappe.db.sql("""
            SELECT SUM(qty - delivered_qty)
            FROM `tabSales Order Item`
            WHERE item_code=%s AND docstatus=1
        """, (code,))[0][0] or 0

        pending_po = frappe.db.sql("""
            SELECT SUM(qty - received_qty)
            FROM `tabPurchase Order Item`
            WHERE item_code=%s AND docstatus=1
        """, (code,))[0][0] or 0

        in_transit = pending_po
        free_stock = stock - pending_so

        data.append({
            "item_code": code,
            "m1": m1,
            "m2": m2,
            "m3": m3,
            "stock": stock,
            "pending_so": pending_so,
            "pending_po": pending_po,
            "in_transit": in_transit,
            "free_stock": free_stock
        })

    return data


# ---------------- SALES ----------------
def get_sales(item_code, start, end):
    return frappe.db.sql("""
        SELECT SUM(qty - delivered_qty)
        FROM `tabSales Order Item` soi
        JOIN `tabSales Order` so ON so.name = soi.parent
        WHERE soi.item_code=%s
        AND so.transaction_date >= %s
        AND so.transaction_date < %s
        AND so.docstatus=1
    """, (item_code, start, end))[0][0] or 0