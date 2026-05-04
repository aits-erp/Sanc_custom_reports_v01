// frappe.query_reports["SO vs PO REPORT"] = {

//     formatter: function (value, row, column, data, default_formatter) {

//         value = default_formatter(value, row, column, data);

//         // ✅ CLICKABLE CHECKBOX (NOW LINKED TO PURCHASE ORDER)
//         if (column.fieldname === "in_transit") {

//             let checked = data.in_transit ? "checked" : "";

//             return `
//                 <input type="checkbox" ${checked}
//                     onclick="update_in_transit('${data.poi_name}', this.checked)">
//             `;
//         }

//         return value;
//     }
// };


// // ✅ GLOBAL FUNCTION (UPDATED)
// window.update_in_transit = function (po_name, checked) {

//     frappe.call({
//         method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_in_transit",
//         args: {
//             po_name: po_name,   // ✅ must match Python
//             value: checked ? 1 : 0
//         },
//         callback: function () {
//             frappe.show_alert({
//                 message: "In Transit Updated",
//                 indicator: "green"
//             });
//         }
//     });
// };


frappe.query_reports["SO vs PO REPORT"] = {

    formatter: function (value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        // ✅ CLICKABLE CHECKBOX (ROW LEVEL - PO ITEM)
        if (column.fieldname === "in_transit") {

            let checked = data.in_transit ? "checked" : "";

            return `
                <input type="checkbox" ${checked}
                    onclick="update_in_transit('${data.poi_name}', this.checked)">
            `;
        }

        return value;
    }
};


// ✅ GLOBAL FUNCTION (FIXED)
window.update_in_transit = function (poi_name, checked) {

    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_in_transit",
        args: {
            poi_name: poi_name,   // ✅ MATCHES PYTHON
            value: checked ? 1 : 0
        },
        callback: function () {
            frappe.show_alert({
                message: "In Transit Updated",
                indicator: "green"
            });

            // ✅ optional but recommended
            frappe.query_report.refresh();
        }
    });
};