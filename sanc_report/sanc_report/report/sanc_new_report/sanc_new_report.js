
// frappe.query_reports["SANC New Report"] = {

//     // ---------------- FILTERS ----------------
//     filters: [
//         {
//             fieldname: "stock_category",
//             label: "Stock Categorization",
//             fieldtype: "Select",
//             options: ["", "Fast Moving Stock", "Standard Stock", "Non-Standard Stock"]
//         },
//         {
//             fieldname: "from_date",
//             label: "From Date",
//             fieldtype: "Date"
//         },
//         {
//             fieldname: "to_date",
//             label: "To Date",
//             fieldtype: "Date",
//             default: frappe.datetime.get_today()
//         },
//         {
//             fieldname: "month",
//             label: "Month",
//             fieldtype: "Select",
//             options: [
//                 "", "January","February","March","April","May","June",
//                 "July","August","September","October","November","December"
//             ]
//         }
//     ],

//     // ---------------- FORMATTER ----------------
//     formatter: function(value, row, column, data, default_formatter) {

//         value = default_formatter(value, row, column, data);

//         // STOCK CLICK
//         if (column.fieldname === "stock" && data.stock != 0) {
//             value = `<a style="color:#1f77b4;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_stock('${data.item_code}')">
//                 ${data.stock}
//             </a>`;
//         }

//         // PENDING PO CLICK
//         if (column.fieldname === "pending_po" && data.pending_po > 0) {
//             value = `<a style="color:#e67e22;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
//                 ${data.pending_po}
//             </a>`;
//         }

//         // IN TRANSIT CLICK
//         if (column.fieldname === "in_transit" && data.in_transit > 0) {
//             value = `<a style="color:#27ae60;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_in_transit('${data.item_code}')">
//                 ${data.in_transit}
//             </a>`;
//         }

//         return value;
//     },

//     // ---------------- COMMON TABLE STYLE ----------------
//     get_table_style: function() {
//         return `
//             <style>
//                 .sanc-table {
//                     width: 100%;
//                     border-collapse: collapse;
//                     font-size: 13px;
//                 }
//                 .sanc-table th {
//                     background: #f4f4f4;
//                     padding: 8px;
//                     border: 1px solid #ddd;
//                     text-align: left;
//                 }
//                 .sanc-table td {
//                     padding: 6px;
//                     border: 1px solid #ddd;
//                 }
//                 .sanc-table a {
//                     color: #007bff;
//                     font-weight: bold;
//                     cursor: pointer;
//                 }
//             </style>
//         `;
//     },

//     // ---------------- STOCK POPUP ----------------
//     show_stock: function(item_code) {

//         frappe.call({
//             method: "frappe.client.get_list",
//             args: {
//                 doctype: "Stock Ledger Entry",
//                 filters: { item_code: item_code },
//                 fields: [
//                     "posting_date",
//                     "voucher_type",
//                     "voucher_no",
//                     "actual_qty",
//                     "qty_after_transaction"
//                 ],
//                 order_by: "posting_date desc",
//                 limit_page_length: 100
//             },
//             callback: function(r) {

//                 let html = frappe.query_reports["SANC New Report"].get_table_style();

//                 html += `<h3>Stock Ledger - ${item_code}</h3>
//                 <div style="max-height:400px;overflow:auto;">
//                 <table class="sanc-table">
//                     <tr>
//                         <th>Date</th>
//                         <th>Voucher</th>
//                         <th>Type</th>
//                         <th>Qty</th>
//                         <th>Balance</th>
//                     </tr>`;

//                 r.message.forEach(d => {
//                     html += `<tr>
//                         <td>${d.posting_date}</td>
//                         <td>
//                             <a onclick="frappe.set_route('Form','${d.voucher_type}','${d.voucher_no}')">
//                                 ${d.voucher_no}
//                             </a>
//                         </td>
//                         <td>${d.voucher_type}</td>
//                         <td>${d.actual_qty}</td>
//                         <td>${d.qty_after_transaction || ""}</td>
//                     </tr>`;
//                 });

//                 html += `</table></div>`;

//                 frappe.msgprint({
//                     title: "Stock Details",
//                     message: html,
//                     wide: true
//                 });
//             }
//         });
//     },

//     // ---------------- PENDING PO POPUP ----------------
//     show_po: function(item_code) {

//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
//             args: { item_code: item_code },
//             callback: function(r) {

//                 let data = r.message.pending_po;

//                 let html = frappe.query_reports["SANC New Report"].get_table_style();

//                 html += `<h3>Pending PO - ${item_code}</h3>
//                 <div style="max-height:400px;overflow:auto;">
//                 <table class="sanc-table">
//                     <tr>
//                         <th>PO No</th>
//                         <th>Supplier</th>
//                         <th>Qty</th>
//                         <th>Received</th>
//                         <th>Pending</th>
//                     </tr>`;

//                 data.forEach(d => {
//                     html += `<tr>
//                         <td>
//                             <a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">
//                                 ${d.parent}
//                             </a>
//                         </td>
//                         <td>${d.supplier || ""}</td>
//                         <td>${d.qty}</td>
//                         <td>${d.received_qty}</td>
//                         <td>${d.pending}</td>
//                     </tr>`;
//                 });

//                 html += `</table></div>`;

//                 frappe.msgprint({
//                     title: "Pending Purchase Orders",
//                     message: html,
//                     wide: true
//                 });
//             }
//         });
//     },

//     // ---------------- IN TRANSIT POPUP ----------------
//     show_in_transit: function(item_code) {

//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
//             args: { item_code: item_code },
//             callback: function(r) {

//                 let data = r.message.in_transit;

//                 let html = frappe.query_reports["SANC New Report"].get_table_style();

//                 html += `<h3>In Transit - ${item_code}</h3>
//                 <div style="max-height:400px;overflow:auto;">
//                 <table class="sanc-table">
//                     <tr>
//                         <th>PO No</th>
//                         <th>Supplier</th>
//                         <th>Ordered Qty</th>
//                         <th>Pending Qty</th>
//                     </tr>`;

//                 data.forEach(d => {
//                     html += `<tr>
//                         <td>
//                             <a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">
//                                 ${d.parent}
//                             </a>
//                         </td>
//                         <td>${d.supplier || ""}</td>
//                         <td>${d.qty}</td>
//                         <td>${d.pending}</td>
//                     </tr>`;
//                 });

//                 html += `</table></div>`;

//                 frappe.msgprint({
//                     title: "In Transit",
//                     message: html,
//                     wide: true
//                 });
//             }
//         });
//     }
// };



// frappe.query_reports["SANC New Report"] = {

//     // ---------------- FILTERS ----------------
//     filters: [
//         {
//             fieldname: "stock_category",
//             label: "Stock Categorization",
//             fieldtype: "Select",
//             options: ["", "Fast Moving Stock", "Standard Stock", "Non-Standard Stock"]
//         },
//         {
//             fieldname: "from_date",
//             label: "From Date",
//             fieldtype: "Date"
//         },
//         {
//             fieldname: "to_date",
//             label: "To Date",
//             fieldtype: "Date",
//             default: frappe.datetime.get_today()
//         },
//         {
//             fieldname: "month",
//             label: "Month",
//             fieldtype: "Select",
//             options: [
//                 "", "January","February","March","April","May","June",
//                 "July","August","September","October","November","December"
//             ]
//         }
//     ],

//     // ---------------- INIT (ONLY KPI CARDS) ----------------
//     onload: function(report) {

//         // KPI container
//         report.page.main.prepend(`
//             <div id="sanc_kpi_cards" style="
//                 display:flex;
//                 gap:15px;
//                 margin-bottom:15px;
//                 flex-wrap:wrap;
//             "></div>
//         `);
//     },

//     // ---------------- FORMATTER ----------------
//     formatter: function(value, row, column, data, default_formatter) {

//         value = default_formatter(value, row, column, data);

//         if (column.fieldname === "stock" && data.stock != 0) {
//             value = `<a style="color:#1f77b4;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_stock('${data.item_code}')">
//                 ${data.stock}
//             </a>`;
//         }

//         if (column.fieldname === "pending_po" && data.pending_po > 0) {
//             value = `<a style="color:#e67e22;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
//                 ${data.pending_po}
//             </a>`;
//         }

//         if (column.fieldname === "in_transit" && data.in_transit > 0) {
//             value = `<a style="color:#27ae60;font-weight:bold"
//                 onclick="frappe.query_reports['SANC New Report'].show_in_transit('${data.item_code}')">
//                 ${data.in_transit}
//             </a>`;
//         }

//         return value;
//     },

//     // ---------------- KPI CARDS (ANIMATION) ----------------
//     set_kpis: function(data) {

//         let total_stock = 0;
//         let total_so = 0;
//         let total_po = 0;
//         let total_free = 0;

//         data.forEach(d => {
//             total_stock += d.stock || 0;
//             total_so += d.pending_so || 0;
//             total_po += d.pending_po || 0;
//             total_free += d.free_stock || 0;
//         });

//         let html = `
//         <div class="sanc-kpi-card">📦 Stock<br><b>${total_stock}</b></div>
//         <div class="sanc-kpi-card">🧾 SO Pending<br><b>${total_so}</b></div>
//         <div class="sanc-kpi-card">🚚 PO Pending<br><b>${total_po}</b></div>
//         <div class="sanc-kpi-card">💰 Free Stock<br><b>${total_free}</b></div>

//         <style>
//             .sanc-kpi-card{
//                 flex:1;
//                 min-width:180px;
//                 padding:15px;
//                 background:white;
//                 border-radius:12px;
//                 box-shadow:0 4px 10px rgba(0,0,0,0.1);
//                 text-align:center;
//                 font-size:14px;
//                 transition:0.3s;
//                 animation: fadeInUp 0.6s ease-in-out;
//             }
//             .sanc-kpi-card:hover{
//                 transform:translateY(-5px);
//                 box-shadow:0 8px 18px rgba(0,0,0,0.15);
//             }
//             .sanc-kpi-card b{
//                 display:block;
//                 font-size:20px;
//                 margin-top:5px;
//                 color:#2c3e50;
//             }
//             @keyframes fadeInUp {
//                 from {opacity:0; transform:translateY(10px);}
//                 to {opacity:1; transform:translateY(0);}
//             }
//         </style>
//         `;

//         document.getElementById("sanc_kpi_cards").innerHTML = html;
//     },

//     // ---------------- TABLE STYLE ----------------
//     get_table_style: function() {
//         return `
//             <style>
//                 .sanc-table {
//                     width: 100%;
//                     border-collapse: collapse;
//                     font-size: 13px;
//                 }
//                 .sanc-table th {
//                     background: #f4f4f4;
//                     padding: 8px;
//                     border: 1px solid #ddd;
//                 }
//                 .sanc-table td {
//                     padding: 6px;
//                     border: 1px solid #ddd;
//                 }
//             </style>
//         `;
//     },

//     // ---------------- STOCK POPUP ----------------
//     show_stock: function(item_code) {

//         frappe.call({
//             method: "frappe.client.get_list",
//             args: {
//                 doctype: "Stock Ledger Entry",
//                 filters: { item_code: item_code },
//                 fields: ["posting_date","voucher_type","voucher_no","actual_qty","qty_after_transaction"],
//                 order_by: "posting_date desc",
//                 limit_page_length: 100
//             },
//             callback: function(r) {

//                 let html = frappe.query_reports["SANC New Report"].get_table_style();

//                 html += `<h3>Stock Ledger - ${item_code}</h3>
//                 <div style="max-height:400px;overflow:auto;">
//                 <table class="sanc-table">
//                     <tr>
//                         <th>Date</th><th>Voucher</th><th>Type</th><th>Qty</th><th>Balance</th>
//                     </tr>`;

//                 (r.message || []).forEach(d => {
//                     html += `<tr>
//                         <td>${d.posting_date}</td>
//                         <td><a onclick="frappe.set_route('Form','${d.voucher_type}','${d.voucher_no}')">${d.voucher_no}</a></td>
//                         <td>${d.voucher_type}</td>
//                         <td>${d.actual_qty}</td>
//                         <td>${d.qty_after_transaction || ""}</td>
//                     </tr>`;
//                 });

//                 html += `</table></div>`;

//                 frappe.msgprint({
//                     title: "Stock Details",
//                     message: html,
//                     wide: true
//                 });
//             }
//         });
//     },

//     // ---------------- PO POPUP ----------------
//     show_po: function(item_code) {

//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
//             args: { item_code: item_code },
//             callback: function(r) {

//                 let data = r.message?.pending_po || [];

//                 let html = frappe.query_reports["SANC New Report"].get_table_style();

//                 html += `<h3>Pending PO - ${item_code}</h3>
//                 <div style="max-height:400px;overflow:auto;">
//                 <table class="sanc-table">
//                     <tr><th>PO</th><th>Supplier</th><th>Qty</th><th>Received</th><th>Pending</th></tr>`;

//                 data.forEach(d => {
//                     html += `<tr>
//                         <td><a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">${d.parent}</a></td>
//                         <td>${d.supplier || ""}</td>
//                         <td>${d.qty}</td>
//                         <td>${d.received_qty || 0}</td>
//                         <td>${d.pending}</td>
//                     </tr>`;
//                 });

//                 html += `</table></div>`;

//                 frappe.msgprint({
//                     title: "Pending Purchase Orders",
//                     message: html,
//                     wide: true
//                 });
//             }
//         });
//     },

//     // ---------------- REFRESH KPI ----------------
//     refresh: function(report) {
//         frappe.call({
//             method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_kpis",
//             args: { filters: report.get_values() },
//             callback: function(r) {
//                 frappe.query_reports["SANC New Report"].set_kpis(r.message || []);
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

        // ❌ STOCK hyperlink removed

        // ✅ SALES ORDER hyperlink
        if (column.fieldname === "pending_so" && data.pending_so > 0) {
            value = `<a style="color:#8e44ad;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_so('${data.item_code}')">
                ${data.pending_so}
            </a>`;
        }

        // PO
        if (column.fieldname === "pending_po" && data.pending_po > 0) {
            value = `<a style="color:#e67e22;font-weight:bold"
                onclick="frappe.query_reports['SANC New Report'].show_po('${data.item_code}')">
                ${data.pending_po}
            </a>`;
        }

        return value;
    },

    // ---------------- SALES ORDER POPUP ----------------
    show_so: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_so_details",
            args: { item_code: item_code },
            callback: function(r) {

                let html = `<h3>Sales Orders - ${item_code}</h3><table class="table table-bordered">
                <tr><th>SO</th><th>Qty</th><th>Delivered</th><th>Pending</th></tr>`;

                (r.message || []).forEach(d => {
                    html += `<tr>
                        <td><a onclick="frappe.set_route('Form','Sales Order','${d.parent}')">${d.parent}</a></td>
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

    // ---------------- PO POPUP ----------------
    show_po: function(item_code) {

        frappe.call({
            method: "sanc_report.sanc_report.report.sanc_new_report.sanc_new_report.get_po_details",
            args: { item_code: item_code },
            callback: function(r) {

                let html = `<h3>Purchase Orders - ${item_code}</h3><table class="table table-bordered">
                <tr><th>PO</th><th>Supplier</th><th>Qty</th><th>Received</th><th>Pending</th></tr>`;

                (r.message.pending_po || []).forEach(d => {
                    html += `<tr>
                        <td><a onclick="frappe.set_route('Form','Purchase Order','${d.parent}')">${d.parent}</a></td>
                        <td>${d.supplier}</td>
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