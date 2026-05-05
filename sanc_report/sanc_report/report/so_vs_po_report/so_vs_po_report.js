frappe.query_reports["SO vs PO REPORT"] = {

    formatter: function (value, row, column, data, default_formatter) {

        value = default_formatter(value, row, column, data);

        // ✅ CHECKBOX
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
                    style="width:150px"
                    onchange="update_awb('${data.poi_name}', this.value)">
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