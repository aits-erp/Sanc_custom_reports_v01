frappe.query_reports["SANC New Report"] = {

    // ---------------- FILTERS ----------------
    filters: [
        {
            fieldname: "stock_category",
            label: "Stock Categorization",
            fieldtype: "Select",
            options: [
                "",
                "Fast Moving Stock",
                "Standard Stock",
                "Non-Standard Stock"
            ]
        },
        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date",
            default: frappe.datetime.get_today()
        },
        {
            fieldname: "month",
            label: "Month",
            fieldtype: "Select",
            default: frappe.datetime.str_to_user(frappe.datetime.get_today()).split(" ")[0], // auto current month
            options: [
                "", "January","February","March","April","May","June",
                "July","August","September","October","November","December"
            ]
        }
    ],

    // ---------------- FORMATTER ----------------
    formatter: function(value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        if (column.fieldname === "pending_po" && data && data.pending_po > 0) {
            value = `<a href="#" onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">${data.pending_po}</a>`;
        }

        if (column.fieldname === "in_transit" && data && data.in_transit > 0) {
            value = `<a href="#" onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">${data.in_transit}</a>`;
        }

        return value;
    },

    // ---------------- POPUP ----------------
    show_po: function(item_code) {

        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Purchase Order Item",
                filters: { item_code: item_code },
                fields: ["parent", "qty", "received_qty"]
            },
            callback: function(r) {

                let html = `<b>Pending Purchase Orders for ${item_code}</b><br><br>`;

                if (!r.message || r.message.length === 0) {
                    html += "No records found";
                } else {
                    r.message.forEach(d => {
                        let pending = (d.qty || 0) - (d.received_qty || 0);
                        if (pending > 0) {
                            html += `
                                <div>
                                    <b>PO:</b> ${d.parent} |
                                    <b>Qty:</b> ${d.qty} |
                                    <b>Received:</b> ${d.received_qty || 0} |
                                    <b>Pending:</b> ${pending}
                                </div>
                            `;
                        }
                    });
                }

                frappe.msgprint({
                    title: "Pending Purchase Orders",
                    message: html,
                    wide: true
                });
            }
        });
    }
};




frappe.query_reports["SANC New Report"] = {

    // ---------------- FILTERS ----------------
    filters: [
        {
            fieldname: "stock_category",
            label: "Stock Categorization",
            fieldtype: "Select",
            options: ["", "Fast Moving Stock", "Standard Stock", "Non-Standard Stock"]
        },
        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date",
            default: frappe.datetime.get_today()
        },
        {
            fieldname: "month",
            label: "Month",
            fieldtype: "Select",
            options: [
                "", "January","February","March","April","May","June",
                "July","August","September","October","November","December"
            ]
        }
    ],

    // ---------------- FORMATTER ----------------
    formatter: function(value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        // STOCK CLICK
        if (column.fieldname === "stock" && data.stock != 0) {
            value = `<a style="color:#1f77b4;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_stock('${data.item_code}')">
                ${data.stock}
            </a>`;
        }

        // PENDING PO CLICK
        if (column.fieldname === "pending_po" && data.pending_po > 0) {
            value = `<a style="color:#e67e22;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
                ${data.pending_po}
            </a>`;
        }

        // IN TRANSIT CLICK
        if (column.fieldname === "in_transit" && data.in_transit > 0) {
            value = `<a style="color:#27ae60;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_in_transit('${data.item_code}')">
                ${data.in_transit}
            </a>`;
        }

        return value;
    },

    // ---------------- COMMON TABLE STYLE ----------------
    get_table_style: function() {
        return `
            <style>
                .sanc-table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 13px;
                }
                .sanc-table th {
                    background: #f4f4f4;
                    padding: 8px;
                    border: 1px solid #ddd;
                    text-align: left;
                }
                .sanc-table td {
                    padding: 6px;
                    border: 1px solid #ddd;
                }
                .sanc-table a {
                    color: #007bff;
                    font-weight: bold;
                    cursor: pointer;
                }
            </style>
        `;
    },

    // ---------------- STOCK POPUP ----------------
    show_stock: function(item_code) {

        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Stock Ledger Entry",
                filters: { item_code: item_code },
                fields: [
                    "posting_date",
                    "voucher_type",
                    "voucher_no",
                    "actual_qty",
                    "qty_after_transaction"
                ],
                order_by: "posting_date desc",
                limit_page_length: 100
            },
            callback: function(r) {

                let html = frappe.query_reports["SANC New Report"].get_table_style();

                html += `<h3>Stock Ledger - ${item_code}</h3>
                <div style="max-height:400px;overflow:auto;">
                <table class="sanc-table">
                    <tr>
                        <th>Date</th>
                        <th>Voucher</th>
                        <th>Type</th>
                        <th>Qty</th>
                        <th>Balance</th>
                    </tr>`;

                r.message.forEach(d => {
                    html += `<tr>
                        <td>${d.posting_date}</td>
                        <td>
                            <a onclick="frappe.set_route('Form','${d.voucher_type}','${d.voucher_no}')">
                                ${d.voucher_no}
                            </a>
                        </td>
                        <td>${d.voucher_type}</td>
                        <td>${d.actual_qty}</td>
                        <td>${d.qty_after_transaction || ""}</td>
                    </tr>`;
                });

                html += `</table></div>`;

                frappe.msgprint({
                    title: "Stock Details",
                    message: html,
                    wide: true
                });
            }
        });
    },

    // ---------------- PENDING PO POPUP ----------------
    show_po: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
            args: { item_code: item_code },
            callback: function(r) {

                let data = r.message.pending_po;

                let html = frappe.query_reports["SANC New Report"].get_table_style();

                html += `<h3>Pending PO - ${item_code}</h3>
                <div style="max-height:400px;overflow:auto;">
                <table class="sanc-table">
                    <tr>
                        <th>PO No</th>
                        <th>Supplier</th>
                        <th>Qty</th>
                        <th>Received</th>
                        <th>Pending</th>
                    </tr>`;

                data.forEach(d => {
                    html += `<tr>
                        <td>
                            <a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">
                                ${d.parent}
                            </a>
                        </td>
                        <td>${d.supplier || ""}</td>
                        <td>${d.qty}</td>
                        <td>${d.received_qty}</td>
                        <td>${d.pending}</td>
                    </tr>`;
                });

                html += `</table></div>`;

                frappe.msgprint({
                    title: "Pending Purchase Orders",
                    message: html,
                    wide: true
                });
            }
        });
    },

    // ---------------- IN TRANSIT POPUP ----------------
    show_in_transit: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
            args: { item_code: item_code },
            callback: function(r) {

                let data = r.message.in_transit;

                let html = frappe.query_reports["SANC New Report"].get_table_style();

                html += `<h3>In Transit - ${item_code}</h3>
                <div style="max-height:400px;overflow:auto;">
                <table class="sanc-table">
                    <tr>
                        <th>PO No</th>
                        <th>Supplier</th>
                        <th>Ordered Qty</th>
                        <th>Pending Qty</th>
                    </tr>`;

                data.forEach(d => {
                    html += `<tr>
                        <td>
                            <a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">
                                ${d.parent}
                            </a>
                        </td>
                        <td>${d.supplier || ""}</td>
                        <td>${d.qty}</td>
                        <td>${d.pending}</td>
                    </tr>`;
                });

                html += `</table></div>`;

                frappe.msgprint({
                    title: "In Transit",
                    message: html,
                    wide: true
                });
            }
        });
    }
};


