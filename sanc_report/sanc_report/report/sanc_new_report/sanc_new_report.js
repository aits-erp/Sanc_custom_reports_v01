
// frappe.query_reports["SANC New Report"] = {

//     filters: [
//         {
//             fieldname: "stock_category",
//             label: "Stock Categorization",
//             fieldtype: "Select",
//             options: ["", "Fast Moving Stock", "Standard Stock", "Non-Standard Stock"]
//         },
//         { fieldname: "from_date", label: "From Date", fieldtype: "Date" },
//         { fieldname: "to_date", label: "To Date", fieldtype: "Date", default: frappe.datetime.get_today() },
//         {
//             fieldname: "month",
//             label: "Month",
//             fieldtype: "Select",
//             options: ["", "January","February","March","April","May","June","July","August","September","October","November","December"]
//         }
//     ],

//     onload: function(report) {
//         report.page.main.prepend(`<div id="sanc_kpi_cards" style="display:flex;gap:15px;margin-bottom:15px;"></div>`);
//     },

//     formatter: function(value, row, column, data, default_formatter) {

//         value = default_formatter(value, row, column, data);

//         // ❌ STOCK hyperlink removed

//         // ✅ SALES ORDER hyperlink
//         if (column.fieldname === "pending_so" && data.pending_so > 0) {
//             value = `<a style="color:#8e44ad;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_so('${data.item_code}')">
//                 ${data.pending_so}
//             </a>`;
//         }

//         // PO
//         if (column.fieldname === "pending_po" && data.pending_po > 0) {
//             value = `<a style="color:#e67e22;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
//                 ${data.pending_po}
//             </a>`;
//         }

//         return value;
//     },

//     // ---------------- SALES ORDER POPUP ----------------
//     show_so: function(item_code) {

//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_so_details",
//             args: { item_code: item_code },
//             callback: function(r) {

//                 let html = `<h3>Sales Orders - ${item_code}</h3><table class="table table-bordered">
//                 <tr><th>SO</th><th>Qty</th><th>Delivered</th><th>Pending</th></tr>`;

//                 (r.message || []).forEach(d => {
//                     html += `<tr>
//                         <td><a onclick="frappe.set_route('Form','Sales Order','${d.parent}')">${d.parent}</a></td>
//                         <td>${d.qty}</td>
//                         <td>${d.delivered_qty}</td>
//                         <td>${d.pending}</td>
//                     </tr>`;
//                 });

//                 html += "</table>";

//                 frappe.msgprint({ title: "Sales Orders", message: html, wide: true });
//             }
//         });
//     },

//     // ---------------- PO POPUP ----------------
//     show_po: function(item_code) {

//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
//             args: { item_code: item_code },
//             callback: function(r) {

//                 let html = `<h3>Purchase Orders - ${item_code}</h3><table class="table table-bordered">
//                 <tr><th>PO</th><th>Supplier</th><th>Qty</th><th>Received</th><th>Pending</th></tr>`;

//                 (r.message.pending_po || []).forEach(d => {
//                     html += `<tr>
//                         <td><a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">${d.parent}</a></td>
//                         <td>${d.supplier}</td>
//                         <td>${d.qty}</td>
//                         <td>${d.received_qty}</td>
//                         <td>${d.pending}</td>
//                     </tr>`;
//                 });

//                 html += "</table>";

//                 frappe.msgprint({ title: "PO Details", message: html, wide: true });
//             }
//         });
//     },

//     refresh: function(report) {
//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_kpis",
//             args: { filters: report.get_values() },
//             callback: function(r) {
//                 let total = (r.message || []).reduce((acc, d) => acc + (d.stock || 0), 0);
//                 document.getElementById("sanc_kpi_cards").innerHTML =
//                     `<div style="padding:10px;background:#fff;border-radius:8px">Total Stock: ${total}</div>`;
//             }
//         });
//     }
// }; 



frappe.query_reports["SANC New Report"] = {

    filters: [
        {
            fieldname: "stock_category",
            label: "Stock Categorization",
            fieldtype: "Select",
            options: ["", "Fast Moving Stock", "Standard Stock", "Non-Standard Stock"]
        },
        { fieldname: "from_date", label: "From Date", fieldtype: "Date" },
        { fieldname: "to_date", label: "To Date", fieldtype: "Date", default: frappe.datetime.get_today() },
        {
            fieldname: "month",
            label: "Month",
            fieldtype: "Select",
            options: ["", "January","February","March","April","May","June","July","August","September","October","November","December"]
        }
    ],

    onload: function(report) {
        report.page.main.prepend(`<div id="sanc_kpi_cards" style="display:flex;gap:15px;margin-bottom:15px;"></div>`);
    },

    formatter: function(value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        if (column.fieldname === "pending_so" && data.pending_so > 0) {
            value = `<a style="color:#8e44ad;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_so('${data.item_code}')">
                ${data.pending_so}
            </a>`;
        }

        if (column.fieldname === "pending_po" && data.pending_po > 0) {
            value = `<a style="color:#e67e22;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
                ${data.pending_po}
            </a>`;
        }

        if (column.fieldname === "in_transit" && data.in_transit > 0) {
            value = `<a style="color:#16a085;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_in_transit('${data.item_code}')">
                ${data.in_transit}
            </a>`;
        }

        return value;
    },

    // ---------------- SALES ORDER ----------------
    show_so: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_so_details",
            args: { item_code: item_code },
            callback: function(r) {

                let html = `<h3>Sales Orders - ${item_code}</h3>
                <table class="table table-bordered">
                <tr><th>SO</th><th>Customer</th><th>Qty</th><th>Delivered</th><th>Pending</th></tr>`;

                (r.message || []).forEach(d => {
                    html += `<tr>
                        <td><a onclick="frappe.set_route('Form','Sales Order','${d.parent}')">${d.parent}</a></td>
                        <td>${d.customer || ""}</td>
                        <td>${d.qty}</td>
                        <td>${d.delivered_qty}</td>
                        <td>${d.pending}</td>
                    </tr>`;
                });

                html += "</table>";

                frappe.msgprint({ title: "Sales Orders", message: html, wide: true });
            }
        });
    },

    // ---------------- PURCHASE ORDER ----------------
    show_po: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
            args: { item_code: item_code },
            callback: function(r) {

                let html = `<h3>Purchase Orders - ${item_code}</h3>
                <table class="table table-bordered">
                <tr><th>PO</th><th>Supplier</th><th>Qty</th><th>Received</th><th>Pending</th></tr>`;

                (r.message.pending_po || []).forEach(d => {
                    html += `<tr>
                        <td><a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">${d.parent}</a></td>
                        <td>${d.supplier_name || d.supplier}</td>
                        <td>${d.qty}</td>
                        <td>${d.received_qty}</td>
                        <td>${d.pending}</td>
                    </tr>`;
                });

                html += "</table>";

                frappe.msgprint({ title: "PO Details", message: html, wide: true });
            }
        });
    },

    // ---------------- IN TRANSIT ----------------
    show_in_transit: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
            args: { item_code: item_code },
            callback: function(r) {

                let html = `<h3>In Transit - ${item_code}</h3>
                <table class="table table-bordered">
                <tr><th>PO</th><th>Supplier</th><th>Qty</th></tr>`;

                (r.message.in_transit || []).forEach(d => {
                    html += `<tr>
                        <td><a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">${d.parent}</a></td>
                        <td>${d.supplier_name || d.supplier}</td>
                        <td>${d.qty}</td>
                    </tr>`;
                });

                html += "</table>";

                frappe.msgprint({ title: "In Transit", message: html, wide: true });
            }
        });
    },

    refresh: function(report) {
        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_kpis",
            args: { filters: report.get_values() },
            callback: function(r) {
                let total = (r.message || []).reduce((acc, d) => acc + (d.stock || 0), 0);
                document.getElementById("sanc_kpi_cards").innerHTML =
                    `<div style="padding:10px;background:#fff;border-radius:8px">Total Stock: ${total}</div>`;
            }
        });
    }
};