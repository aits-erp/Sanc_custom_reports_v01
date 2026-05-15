// frappe.query_reports["SO vs PO REPORT"] = {

//     formatter: function (value, row, column, data, default_formatter) {

//         value = default_formatter(value, row, column, data);

//         // ✅ CHECKBOX
//         if (column.fieldname === "in_transit") {

//             let checked = data.in_transit ? "checked" : "";

//             return `
//                 <input type="checkbox" ${checked}
//                     onclick="update_in_transit('${data.poi_name}', this.checked)">
//             `;
//         }

//         // ✅ EDITABLE AWB FIELD
//         if (column.fieldname === "awb_number") {

//             let val = data.awb_number || "";

//             return `
//                 <input type="text" value="${val}"
//                     style="width:150px"
//                     onchange="update_awb('${data.poi_name}', this.value)">
//             `;
//         }

//         return value;
//     }
// };


// // ✅ UPDATE CHECKBOX
// window.update_in_transit = function (poi_name, checked) {

//     frappe.call({
//         method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_in_transit",
//         args: {
//             poi_name: poi_name,
//             value: checked ? 1 : 0
//         },
//         callback: function () {
//             frappe.show_alert({ message: "In Transit Updated", indicator: "green" });
//         }
//     });
// };


// // ✅ UPDATE AWB NUMBER
// window.update_awb = function (poi_name, value) {

//     frappe.call({
//         method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_awb_number",
//         args: {
//             poi_name: poi_name,
//             awb_number: value
//         },
//         callback: function () {
//             frappe.show_alert({ message: "AWB Updated", indicator: "green" });
//         }
//     });
// };

frappe.query_reports["SO vs PO REPORT"] = {

    formatter: function (value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        // ✅ CERTIFICATE SELECT DROPDOWN (read-only display with color badge)
        if (column.fieldname === "custom_certificate") {

            let val = data.custom_certificate || "";

            // Color-coded badges for quick visual reference
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

        // ✅ CHECKBOX for In Transit
        if (column.fieldname === "in_transit") {

            let checked = data.in_transit ? "checked" : "";

            return `
                <input type="checkbox" ${checked}
                    onclick="update_in_transit('${data.poi_name}', this.checked)">
            `;
        }

        // ✅ EDITABLE AWB FIELD
        if (column.fieldname === "awb_number") {

            let val = data.awb_number || "";

            return `
                <input type="text" value="${val}"
                    style="width:150px; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px;"
                    onchange="update_awb('${data.poi_name}', this.value)">
            `;
        }

        // ✅ NEW: EDITABLE REMARK FIELD
        if (column.fieldname === "custom_remark") {

            let val = data.custom_remark || "";

            return `
                <input type="text" value="${val}"
                    style="width:180px; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px;"
                    placeholder="Add remark..."
                    onchange="update_remark('${data.poi_name}', this.value)">
            `;
        }

        return value;
    }
};


// ✅ UPDATE CHECKBOX
window.update_in_transit = function (poi_name, checked) {

    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_in_transit",
        args: {
            poi_name: poi_name,
            value: checked ? 1 : 0
        },
        callback: function () {
            frappe.show_alert({ message: "In Transit Updated", indicator: "green" });
        }
    });
};


// ✅ UPDATE AWB NUMBER
window.update_awb = function (poi_name, value) {

    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_awb_number",
        args: {
            poi_name: poi_name,
            awb_number: value
        },
        callback: function () {
            frappe.show_alert({ message: "AWB Updated", indicator: "green" });
        }
    });
};


// ✅ NEW: UPDATE REMARK
window.update_remark = function (poi_name, value) {

    frappe.call({
        method: "sanc_report.sanc_report.report.so_vs_po_report.so_vs_po_report.update_remark",
        args: {
            poi_name: poi_name,
            remark: value
        },
        callback: function () {
            frappe.show_alert({ message: "Remark Updated", indicator: "green" });
        }
    });
};