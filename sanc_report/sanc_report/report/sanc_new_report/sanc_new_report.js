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