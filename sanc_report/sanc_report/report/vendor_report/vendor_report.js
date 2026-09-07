// frappe.query_reports["Vendor Report"] = {
// 	"filters": [
// 		{
// 			"fieldname": "from_date",
// 			"label": __("From Date"),
// 			"fieldtype": "Date",
// 			"default": frappe.datetime.month_start(),
// 			"reqd": 1
// 		},
// 		{
// 			"fieldname": "to_date",
// 			"label": __("To Date"),
// 			"fieldtype": "Date",
// 			"default": frappe.datetime.month_end(),
// 			"reqd": 1
// 		}
// 	],

// 	onload: function (report) {
// 		// Button to export the last column ("Open Notepad and Copy Below Data")
// 		// as a plain .txt file, one row per line - ready to paste into Notepad
// 		// or upload to the RBI adapter.
// 		//
// 		// Transaction Type is an editable Select column (I/N/R/M) in the grid,
// 		// defaulting to the value auto-mapped from Payment Entry but can be
// 		// manually overridden per row. The notepad_data string is pre-built
// 		// server-side using the auto-mapped value, so before exporting we
// 		// swap in whatever Transaction Type is currently showing in the grid
// 		// for that row (in case it was manually changed) as the first field
// 		// of the RBI line.
// 		report.page.add_inner_button(__("Download Notepad Data"), function () {
// 			let data = report.data;

// 			if (!data || !data.length) {
// 				frappe.msgprint(__("No data to download. Please run the report first."));
// 				return;
// 			}

// 			let lines = data
// 				.map((row) => {
// 					let line = row["notepad_data"];

// 					if (line === undefined || line === null || line === "") {
// 						return null;
// 					}

// 					// Use the current (possibly manually edited) Transaction
// 					// Type value from the grid as the first field of the line.
// 					let currentType = row["transaction_type"];
// 					if (currentType !== undefined && currentType !== null && currentType !== "") {
// 						let parts = line.split(",");
// 						parts[0] = currentType;
// 						line = parts.join(",");
// 					}

// 					return line;
// 				})
// 				.filter((line) => line !== undefined && line !== null && line !== "");

// 			if (!lines.length) {
// 				frappe.msgprint(__("Notepad data column is empty."));
// 				return;
// 			}

// 			let content = lines.join("\n");
// 			let blob = new Blob([content], { type: "text/plain" });
// 			let link = document.createElement("a");

// 			link.href = window.URL.createObjectURL(blob);
// 			link.download = "RBI_Adapter_Vendor_" + frappe.datetime.now_date() + ".txt";
// 			document.body.appendChild(link);
// 			link.click();
// 			document.body.removeChild(link);
// 		});
// 	}
// };



frappe.query_reports["Vendor Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.month_start(),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.month_end(),
			"reqd": 1
		}
	],

	onload: function (report) {
		// Button to export the last column ("Open Notepad and Copy Below Data")
		// as a plain .txt file, one row per line - ready to paste into Notepad
		// or upload to the RBI adapter.
		//
		// Transaction Type is a free-text editable field (same pattern as
		// AWB Number / Remark in SO vs PO Report), and every typed value is
		// saved straight to Payment Entry.custom_transaction_type via
		// update_transaction_type() - so row["transaction_type"] here is
		// already the current, persisted value. We still swap it into the
		// first field of notepad_data as a safety net, in case a value was
		// just typed and not yet re-fetched from a fresh report run.
		report.page.add_inner_button(__("Download Notepad Data"), function () {
			let data = frappe.query_report.data;

			if (!data || !data.length) {
				frappe.msgprint(__("No data to download. Please run the report first."));
				return;
			}

			let lines = data
				.map((row) => {
					let line = row["notepad_data"];

					if (line === undefined || line === null || line === "") {
						return null;
					}

					// Use the current (possibly manually edited) Transaction
					// Type value from the grid as the first field of the line.
					let currentType = row["transaction_type"];
					if (currentType !== undefined && currentType !== null && currentType !== "") {
						let parts = line.split(",");
						parts[0] = currentType;
						line = parts.join(",");
					}

					return line;
				})
				.filter((line) => line !== undefined && line !== null && line !== "");

			if (!lines.length) {
				frappe.msgprint(__("Notepad data column is empty."));
				return;
			}

			let content = lines.join("\n");
			let blob = new Blob([content], { type: "text/plain" });
			let link = document.createElement("a");

			link.href = window.URL.createObjectURL(blob);
			link.download = "RBI_Adapter_Vendor_" + frappe.datetime.now_date() + ".txt";
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
		});
	},

	// ─────────────────────────────────────────────
	// FORMATTER
	// ─────────────────────────────────────────────
	formatter: function (value, row, column, data, default_formatter) {

		value = default_formatter(value, row, column, data);

		// ✅ EDITABLE TRANSACTION TYPE FIELD (free text, same pattern as
		// AWB Number / Remark in SO vs PO Report - no dropdown, user types
		// the value directly. Still expected to be I / N / R / M, and is
		// validated + saved server-side onto Payment Entry.custom_transaction_type
		// in update_transaction_type() below.)
		if (column.fieldname === "transaction_type") {

			let val = (data.transaction_type || "").replace(/"/g, "&quot;");
			let payment_entry = data.payment_entry || "";

			if (!payment_entry) {
				return `<span>${val}</span>`;
			}

			return `
                <input type="text" value="${val}"
                    maxlength="1"
                    style="width:100%; box-sizing:border-box; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px; text-transform:uppercase;"
                    placeholder="I/N/R/M"
                    onchange="vendor_report_update_transaction_type('${payment_entry}', this.value)">
            `;
		}

		return value;
	},
};


// ─────────────────────────────────────────────
// WHITELISTED UPDATE HELPER
// ─────────────────────────────────────────────

window.vendor_report_update_transaction_type = function (payment_entry, value) {
	frappe.call({
		method: "sanc_report.sanc_report.report.vendor_report.vendor_report.update_transaction_type",
		args: {
			payment_entry: payment_entry,
			transaction_type: value
		},
		callback: function (r) {
			if (r.message) {
				let saved_value = r.message.transaction_type;

				// Keep the in-memory report data (used by the notepad
				// download button and by re-rendering) in sync with what
				// was just saved, so an immediate download without a
				// refresh still shows the correct value.
				let data = frappe.query_report.data || [];
				let row = data.find((d) => d.payment_entry === payment_entry);

				if (row) {
					row.transaction_type = saved_value;

					if (row.notepad_data) {
						let parts = row.notepad_data.split(",");
						parts[0] = saved_value;
						row.notepad_data = parts.join(",");
					}
				}

				frappe.show_alert({ message: __("Transaction Type Updated"), indicator: "green" });
			}
		},
		error: function () {
			frappe.msgprint(__("Failed to save Transaction Type. Please try again."));
			// Reload the report so the field snaps back to the last saved
			// value rather than showing an invalid typed value.
			frappe.query_report.refresh();
		}
	});
};