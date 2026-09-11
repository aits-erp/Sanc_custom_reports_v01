
# import frappe
# def execute(filters=None):
#     columns = get_columns()
#     data = get_data(filters)

#     report_summary = []

#     if data:
#         totals = get_totals_row(data)

#         currency = None
#         if filters and filters.get("company"):
#             currency = frappe.get_cached_value("Company", filters.get("company"), "default_currency")

#         report_summary = [
#             {
#                 "label": "Total Qty",
#                 "value": totals["qty"],
#                 "indicator": "Blue",
#                 "datatype": "Float",
#             },
#             {
#                 "label": "Total Amount",
#                 "value": totals["amount"],
#                 "indicator": "Blue",
#                 "datatype": "Currency",
#                 "currency": currency,
#             },
#             {
#                 "label": "Delivered Qty",
#                 "value": totals["qty_billed"],
#                 "indicator": "Green",
#                 "datatype": "Float",
#             },
#             {
#                 "label": "Qty Pending",
#                 "value": totals["qty_pending"],
#                 "indicator": "Orange",
#                 "datatype": "Float",
#             },
#             {
#                 "label": "Amount Billed",
#                 "value": totals["amount_billed"],
#                 "indicator": "Green",
#                 "datatype": "Currency",
#                 "currency": currency,
#             },
#             {
#                 "label": "Amount Pending",
#                 "value": totals["amount_pending"],
#                 "indicator": "Red",
#                 "datatype": "Currency",
#                 "currency": currency,
#             },
#             {
#                 "label": "PO Qty",
#                 "value": totals["po_qty"],
#                 "indicator": "Blue",
#                 "datatype": "Float",
#             },
#         ]

#         # ✅ Append totals row at the bottom of the data table
#         data.append(totals)

#     return columns, data, None, None, report_summary



# def get_columns():
#     return [
#         {"label": "Date",                "fieldname": "date",                   "fieldtype": "Date",     "width": 100},
#         {"label": "Customer PO Number",  "fieldname": "po_no",                  "fieldtype": "Data",     "width": 150},
#         {"label": "SO Category",         "fieldname": "order_type",             "fieldtype": "Data",     "width": 140},
#         {"label": "Sales Order",         "fieldname": "so",                     "fieldtype": "Link",     "options": "Sales Order",  "width": 150},
#         {"label": "Sales Person",        "fieldname": "sales_person",           "fieldtype": "Data",     "width": 150},
#         {"label": "Customer Name",       "fieldname": "customer_name",          "fieldtype": "Data",     "width": 180},
#         {"label": "Certificate",         "fieldname": "custom_certificate",     "fieldtype": "Select",   "options": "\nTC\nCC\nTC/CC", "width": 120},
#         {"label": "Part Number",         "fieldname": "item_code",              "fieldtype": "Link",     "options": "Item",         "width": 120},
#         {"label": "Qty",                 "fieldname": "qty",                    "fieldtype": "Float",    "width": 80},
#         {"label": "Unit Price",          "fieldname": "rate",                   "fieldtype": "Currency", "width": 100},
#         {"label": "Total Price",         "fieldname": "amount",                 "fieldtype": "Currency", "width": 120},
#         {"label": "Sales EDD",           "fieldname": "custom_edd",             "fieldtype": "Date",     "width": 120},

#         # ── Billed / Pending — same formula as Sales Order Analysis ──
#         {"label": "Qty Billed",          "fieldname": "qty_billed",             "fieldtype": "Float",    "width": 100},
#         {"label": "Qty Pending",         "fieldname": "qty_pending",            "fieldtype": "Float",    "width": 100},
#         {"label": "Amount Billed",       "fieldname": "amount_billed",          "fieldtype": "Currency", "width": 120},
#         {"label": "Amount Pending",      "fieldname": "amount_pending",         "fieldtype": "Currency", "width": 120},

#         {"label": "Supplier Code",       "fieldname": "supplier",               "fieldtype": "Link",     "options": "Supplier",     "width": 150},
#         {"label": "Supplier Name",       "fieldname": "supplier_name",          "fieldtype": "Data",     "width": 180},
#         {"label": "PO Number",           "fieldname": "po",                     "fieldtype": "Link",     "options": "Purchase Order","width": 150},
#         {"label": "PO Date",             "fieldname": "po_date",                "fieldtype": "Date",     "width": 100},
#         {"label": "PO Item",             "fieldname": "po_item",                "fieldtype": "Data",     "width": 120},
#         {"label": "PO Qty",              "fieldname": "po_qty",                 "fieldtype": "Float",    "width": 100},
#         {"label": "Purchase EDD",        "fieldname": "expected_delivery_date", "fieldtype": "Date",     "width": 120},
#         {"label": "In Transit",          "fieldname": "in_transit",             "fieldtype": "Check",    "width": 100},
#         {"label": "AWB/MAWB Number",     "fieldname": "awb_number",             "fieldtype": "Data",     "width": 180},
#         {"label": "Remark",              "fieldname": "custom_remark",          "fieldtype": "Data",     "width": 200},
#     ]


# def get_conditions(filters):
#     conditions = ""

#     if filters.get("from_date") and filters.get("to_date"):
#         conditions += " AND so.transaction_date BETWEEN %(from_date)s AND %(to_date)s"

#     if filters.get("company"):
#         conditions += " AND so.company = %(company)s"

#     if filters.get("sales_order") and len(filters.get("sales_order")) > 0:
#         conditions += " AND so.name IN %(sales_order)s"

#     if filters.get("status") and len(filters.get("status")) > 0:
#         conditions += " AND so.status IN %(status)s"

#     if filters.get("purchase_order") and len(filters.get("purchase_order")) > 0:
#         conditions += " AND po.name IN %(purchase_order)s"

#     return conditions


# def get_data(filters):
#     if not filters:
#         filters = {}

#     # Convert lists to tuples for SQL IN clause
#     for key in ("sales_order", "purchase_order", "status"):
#         if filters.get(key) and isinstance(filters[key], list):
#             filters[key] = tuple(filters[key])

#     conditions = get_conditions(filters)

#     data = frappe.db.sql("""
#         SELECT
#             so.transaction_date                                             AS date,
#             so.po_no,
#             so.order_type,
#             so.name                                                         AS so,

#             -- ✅ Correlated subquery — fetches sales persons without JOIN row multiplication
#             (
#                 SELECT GROUP_CONCAT(DISTINCT st.sales_person ORDER BY st.idx SEPARATOR ', ')
#                 FROM `tabSales Team` st
#                 WHERE st.parent     = so.name
#                   AND st.parenttype = 'Sales Order'
#             )                                                               AS sales_person,

#             so.customer_name,
#             so.custom_certificate,

#             soi.item_code,
#             soi.qty,
#             soi.rate,
#             soi.base_amount                                                 AS amount,
#             soi.custom_edd,

#             IFNULL(soi.delivered_qty, 0)                                    AS qty_billed,

#             (soi.qty - IFNULL(soi.delivered_qty, 0))                        AS qty_pending,

#             (soi.billed_amt * IFNULL(so.conversion_rate, 1))                AS amount_billed,

#             (soi.base_amount - (soi.billed_amt * IFNULL(so.conversion_rate, 1))) AS amount_pending,

#             sup.name                                                        AS supplier,
#             sup.supplier_name,
#             po.name                                                         AS po,
#             po.transaction_date                                             AS po_date,

#             poi.item_code                                                   AS po_item,
#             poi.qty                                                         AS po_qty,
#             poi.expected_delivery_date,
#             poi.custom_good_in_transit                                      AS in_transit,
#             poi.custom_awbmawb_number                                       AS awb_number,
#             poi.custom_remark,
#             poi.name                                                        AS poi_name

#         FROM `tabSales Order` so

#         -- ── Join SO items — same as standard report ──
#         INNER JOIN `tabSales Order Item` soi
#             ON soi.parent = so.name

#         -- ── PO item matched by SO name + SO item ──
#         LEFT JOIN `tabPurchase Order Item` poi
#              ON poi.sales_order      = so.name
#             AND poi.sales_order_item = soi.name

#         -- ── PO header — only submitted ──
#         LEFT JOIN `tabPurchase Order` po
#             ON po.name      = poi.parent
#            AND po.docstatus = 1

#         LEFT JOIN `tabSupplier` sup
#             ON sup.name = po.supplier

#         WHERE
#             so.docstatus = 1
#             AND so.status NOT IN ('Cancelled', 'Closed', 'Completed')
#             {conditions}

#         GROUP BY soi.name

#         ORDER BY so.transaction_date DESC, so.name, soi.idx

#     """.format(conditions=conditions), filters, as_dict=1)

#     return data


# def get_totals_row(data):
#     totals = {
#         "date":                   None,
#         "po_no":                  None,
#         "order_type":             None,
#         "so":                     None,
#         "sales_person":           None,
#         "customer_name":          "Total",
#         "custom_certificate":     None,
#         "item_code":              None,
#         "qty":                    0,
#         "rate":                   None,
#         "amount":                 0,
#         "custom_edd":             None,
#         "qty_billed":             0,
#         "qty_pending":            0,
#         "amount_billed":          0,
#         "amount_pending":         0,
#         "supplier":               None,
#         "supplier_name":          None,
#         "po":                     None,
#         "po_date":                None,
#         "po_item":                None,
#         "po_qty":                 0,
#         "expected_delivery_date": None,
#         "in_transit":             None,
#         "awb_number":             None,
#         "custom_remark":          None,
#         "poi_name":               None,
#         "is_total_row":           True,
#     }

#     for row in data:
#         totals["qty"]            += (row.get("qty")            or 0)
#         totals["amount"]         += (row.get("amount")         or 0)
#         totals["qty_billed"]     += (row.get("qty_billed")     or 0)
#         totals["qty_pending"]    += (row.get("qty_pending")    or 0)
#         totals["amount_billed"]  += (row.get("amount_billed")  or 0)
#         totals["amount_pending"] += (row.get("amount_pending") or 0)
#         totals["po_qty"]         += (row.get("po_qty")         or 0)

#     return totals


# # ── Whitelisted update helpers ─────────────────────────────────────────────────

# @frappe.whitelist()
# def update_in_transit(poi_name, value):
#     frappe.db.set_value("Purchase Order Item", poi_name, "custom_good_in_transit", value)
#     frappe.db.commit()


# @frappe.whitelist()
# def update_awb_number(poi_name, awb_number):
#     frappe.db.set_value("Purchase Order Item", poi_name, "custom_awbmawb_number", awb_number)
#     frappe.db.commit()

# # hi
# @frappe.whitelist()
# def update_remark(poi_name, remark):
#     frappe.db.set_value("Purchase Order Item", poi_name, "custom_remark", remark)
#     frappe.db.commit()



// Copyright (c) 2024, Your Company
// SO vs PO Report — filters mirror Sales Order Analysis + Purchase Order filter

frappe.query_reports["SO vs PO REPORT"] = {

    // ─────────────────────────────────────────────
    // FILTERS
    // ─────────────────────────────────────────────
    filters: [
        {
            fieldname: "company",
            label: __("Company"),
            fieldtype: "Link",
            width: "80",
            options: "Company",
            reqd: 1,
            default: frappe.defaults.get_default("company"),
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            width: "80",
            reqd: 1,
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            on_change: (report) => {
                report.set_filter_value("sales_order", []);
                report.set_filter_value("purchase_order", []);
                report.refresh();
            },
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            width: "80",
            reqd: 1,
            default: frappe.datetime.get_today(),
            on_change: (report) => {
                report.set_filter_value("sales_order", []);
                report.set_filter_value("purchase_order", []);
                report.refresh();
            },
        },
        {
            fieldname: "sales_order",
            label: __("Sales Order"),
            fieldtype: "MultiSelectList",
            width: "80",
            options: "Sales Order",
            get_data: function (txt) {
                let filters = { docstatus: 1 };

                const from_date = frappe.query_report.get_filter_value("from_date");
                const to_date   = frappe.query_report.get_filter_value("to_date");
                if (from_date && to_date) {
                    filters["transaction_date"] = ["between", [from_date, to_date]];
                }

                return frappe.db.get_link_options("Sales Order", txt, filters);
            },
        },
        {
            fieldname: "purchase_order",
            label: __("Purchase Order"),
            fieldtype: "MultiSelectList",
            width: "80",
            options: "Purchase Order",
            get_data: function (txt) {
                let filters = { docstatus: 1 };

                const from_date = frappe.query_report.get_filter_value("from_date");
                const to_date   = frappe.query_report.get_filter_value("to_date");
                if (from_date && to_date) {
                    filters["transaction_date"] = ["between", [from_date, to_date]];
                }

                return frappe.db.get_link_options("Purchase Order", txt, filters);
            },
        },
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "MultiSelectList",
            width: "80",
            get_data: function (txt) {
                let statuses = [
                    "Draft",
                    "On Hold",
                    "To Deliver and Bill",
                    "To Bill",
                    "To Deliver",
                    "Completed",
                    "Cancelled",
                    "Closed",
                ];
                return statuses.map((s) => ({ value: s, label: __(s), description: "" }));
            },
        },
    ],


    // ─────────────────────────────────────────────
    // ✅ Force client-side inline column filtering
    // ─────────────────────────────────────────────
    get_datatable_options: function (options) {
        return Object.assign(options, {
            inlineFilters: true,
        });
    },


    // ─────────────────────────────────────────────
    // FORMATTER
    // ─────────────────────────────────────────────
    formatter: function (value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        // ✅ Bold totals row
        if (data && data.is_total_row) {
            if (column.fieldname === "customer_name") {
                return `<strong style="color:#333;">Totals</strong>`;
            }
            let numeric_fields = [
                "qty", "amount", "qty_billed", "qty_pending",
                "amount_billed", "amount_pending", "po_qty"
            ];
            if (in_list(numeric_fields, column.fieldname) && data[column.fieldname] != null) {
                return `<strong>${value}</strong>`;
            }
            return value;
        }

        // ✅ CERTIFICATE SELECT — color-coded badge
        if (column.fieldname === "custom_certificate") {

            let val = data.custom_certificate || "";

            let colorMap = {
                "TC":    "#5b7fff",
                "CC":    "#28a745",
                "TC/CC": "#fd7e14"
            };

            let color = colorMap[val] || "#aaa";

            if (!val) {
                return `<span style="color:#aaa; font-style:italic;">—</span>`;
            }

            return `
                <span style="
                    background:${color};
                    color:#fff;
                    padding:2px 8px;
                    border-radius:4px;
                    font-size:11px;
                    font-weight:600;
                    letter-spacing:0.4px;
                ">${val}</span>
            `;
        }

        // ✅ CHECKBOX — In Transit
        if (column.fieldname === "in_transit") {

            let checked = data.in_transit ? "checked" : "";
            let poi = data.poi_name || "";

            if (!poi) {
                return `<input type="checkbox" ${checked} disabled>`;
            }

            return `
                <input type="checkbox" ${checked}
                    onclick="so_vs_po_update_in_transit('${poi}', this.checked)">
            `;
        }

        // ✅ EDITABLE AWB FIELD
        if (column.fieldname === "awb_number") {

            let val = (data.awb_number || "").replace(/"/g, "&quot;");
            let poi = data.poi_name || "";

            if (!poi) {
                return `<span>${val}</span>`;
            }

            return `
                <input type="text" value="${val}"
                    style="width:150px; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px;"
                    onchange="so_vs_po_update_awb('${poi}', this.value)">
            `;
        }

        // ✅ EDITABLE REMARK FIELD
        if (column.fieldname === "custom_remark") {

            let val = (data.custom_remark || "").replace(/"/g, "&quot;");
            let poi = data.poi_name || "";

            if (!poi) {
                return `<span style="color:#aaa; font-style:italic;">${val || "—"}</span>`;
            }

            return `
                <input type="text" value="${val}"
                    style="width:180px; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px;"
                    placeholder="Add remark..."
                    onchange="so_vs_po_update_remark('${poi}', this.value)">
            `;
        }

        // ✅ Highlight amount_pending in red if > 0
        if (column.fieldname === "amount_pending" && data && data.amount_pending > 0) {
            return `<span style="color:red;">${value}</span>`;
        }

        // ✅ Highlight amount_billed in green if > 0
        if (column.fieldname === "amount_billed" && data && data.amount_billed > 0) {
            return `<span style="color:green;">${value}</span>`;
        }

        return value;
    },
};


// ─────────────────────────────────────────────
// WHITELISTED UPDATE HELPERS
// ─────────────────────────────────────────────

window.so_vs_po_update_in_transit = function (poi_name, checked) {
    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_in_transit",
        args: {
            poi_name: poi_name,
            value: checked ? 1 : 0
        },
        callback: function () {
            frappe.show_alert({ message: __("In Transit Updated"), indicator: "green" });
        }
    });
};

window.so_vs_po_update_awb = function (poi_name, value) {
    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_awb_number",
        args: {
            poi_name: poi_name,
            awb_number: value
        },
        callback: function () {
            frappe.show_alert({ message: __("AWB Updated"), indicator: "green" });
        }
    });
};

window.so_vs_po_update_remark = function (poi_name, value) {
    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_remark",
        args: {
            poi_name: poi_name,
            remark: value
        },
        callback: function () {
            frappe.show_alert({ message: __("Remark Updated"), indicator: "green" });
        }
    });
};