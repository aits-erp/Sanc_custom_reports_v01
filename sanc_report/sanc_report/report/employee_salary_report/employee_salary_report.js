
// // Copyright (c) 2026, Sukku and contributors
// // For license information, please see license.txt

// frappe.query_reports["Employee Salary Report"] = {
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
// 		report.page.add_inner_button(__("Download Notepad Data"), function () {
// 			// Pull the CURRENT grid data (not a stale snapshot), so that any
// 			// manual Transaction Type edit made in the editable dropdown is
// 			// picked up.
// 			let data = frappe.query_report.data;

// 			if (!data || !data.length) {
// 				frappe.msgprint(__("No data to download. Please run the report first."));
// 				return;
// 			}

// 			let lines = data
// 				.map((row) => {
// 					let notepad_line = row["notepad_data"];

// 					if (notepad_line === undefined || notepad_line === null || notepad_line === "") {
// 						return null;
// 					}

// 					// notepad_data is built once on the server with whatever
// 					// Transaction Type was there at report-run time. If the
// 					// user has since picked a different value (I/N/R/M) in
// 					// the editable Transaction Type column, that live value
// 					// lives in row["transaction_type"] - so we splice it into
// 					// the first comma-separated field of the notepad line
// 					// here, right before download.
// 					let parts = notepad_line.split(",");
// 					let current_transaction_type = row["transaction_type"];

// 					if (current_transaction_type !== undefined && current_transaction_type !== null) {
// 						parts[0] = current_transaction_type;
// 					}

// 					return parts.join(",");
// 				})
// 				.filter((line) => line !== null && line !== "");

// 			if (!lines.length) {
// 				frappe.msgprint(__("Notepad data column is empty."));
// 				return;
// 			}

// 			let content = lines.join("\n");
// 			let blob = new Blob([content], { type: "text/plain" });
// 			let link = document.createElement("a");

// 			link.href = window.URL.createObjectURL(blob);
// 			link.download = "RBI_Adapter_" + frappe.datetime.now_date() + ".txt";
// 			document.body.appendChild(link);
// 			link.click();
// 			document.body.removeChild(link);
// 		});
// 	}
// };




// // Copyright (c) 2026, Sukku and contributors
// // For license information, please see license.txt

// frappe.query_reports["Employee Salary Report"] = {
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
// 		report.page.add_inner_button(__("Download Notepad Data"), function () {
// 			let data = frappe.query_report.data;

// 			if (!data || !data.length) {
// 				frappe.msgprint(__("No data to download. Please run the report first."));
// 				return;
// 			}

// 			let lines = data
// 				.map((row) => row["notepad_data"])
// 				.filter((line) => line !== undefined && line !== null && line !== "");

// 			if (!lines.length) {
// 				frappe.msgprint(__("Notepad data column is empty."));
// 				return;
// 			}

// 			let content = lines.join("\n");
// 			let blob = new Blob([content], { type: "text/plain" });
// 			let link = document.createElement("a");

// 			link.href = window.URL.createObjectURL(blob);
// 			link.download = "RBI_Adapter_" + frappe.datetime.now_date() + ".txt";
// 			document.body.appendChild(link);
// 			link.click();
// 			document.body.removeChild(link);
// 		});
// 	},

// 	// ─────────────────────────────────────────────
// 	// FORMATTER
// 	// ─────────────────────────────────────────────
// 	formatter: function (value, row, column, data, default_formatter) {

// 		value = default_formatter(value, row, column, data);

// 		// ✅ EDITABLE TRANSACTION TYPE DROPDOWN
// 		if (column.fieldname === "transaction_type") {

// 			let val = data.transaction_type || "";
// 			let salary_slip = data.salary_slip || "";

// 			if (!salary_slip) {
// 				return `<span>${val}</span>`;
// 			}

// 			let options = ["", "I", "N", "R", "M"];
// 			let option_html = options
// 				.map((opt) => {
// 					let selected = opt === val ? "selected" : "";
// 					let label = opt || "-";
// 					return `<option value="${opt}" ${selected}>${label}</option>`;
// 				})
// 				.join("");

// 			return `
//                 <select
// 					style="width:100px; border:1px solid #d1d8dd; border-radius:4px; padding:2px 4px;"
//                     onchange="employee_salary_update_transaction_type('${salary_slip}', this.value)">
//                     ${option_html}
//                 </select>
//             `;
// 		}

// 		return value;
// 	},
// };


// // ─────────────────────────────────────────────
// // WHITELISTED UPDATE HELPER
// // ─────────────────────────────────────────────

// window.employee_salary_update_transaction_type = function (salary_slip, value) {
// 	frappe.call({
// 		method: "sanc_report.sanc_report.report.employee_salary_report.employee_salary_report.update_transaction_type",
// 		args: {
// 			salary_slip: salary_slip,
// 			transaction_type: value
// 		},
// 		callback: function (r) {
// 			if (r.message) {
// 				let saved_value = r.message.transaction_type;

// 				// Keep the in-memory report data (used by the notepad
// 				// download button and by re-rendering) in sync with what
// 				// was just saved, so an immediate download without a
// 				// refresh still shows the correct value.
// 				let data = frappe.query_report.data || [];
// 				let row = data.find((d) => d.salary_slip === salary_slip);

// 				if (row) {
// 					row.transaction_type = saved_value;

// 					if (row.notepad_data) {
// 						let parts = row.notepad_data.split(",");
// 						parts[0] = saved_value;
// 						row.notepad_data = parts.join(",");
// 					}
// 				}

// 				frappe.show_alert({ message: __("Transaction Type Updated"), indicator: "green" });
// 			}
// 		},
// 		error: function () {
// 			frappe.msgprint(__("Failed to save Transaction Type. Please try again."));
// 		}
// 	});
// };

// Copyright (c) 2026, Sukku and contributors
// For license information, please see license.txt

frappe.query_reports["Employee Salary Report"] = {
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
		// saved straight to Salary Slip.custom_transaction_type via
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
			link.download = "RBI_Adapter_" + frappe.datetime.now_date() + ".txt";
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
		// validated + saved server-side onto Salary Slip.custom_transaction_type
		// in update_transaction_type() below.)
		if (column.fieldname === "transaction_type") {

			let val = (data.transaction_type || "").replace(/"/g, "&quot;");
			let salary_slip = data.salary_slip || "";

			if (!salary_slip) {
				return `<span>${val}</span>`;
			}

			return `
                <input type="text" value="${val}"
                    maxlength="1"
                    style="width:100%; box-sizing:border-box; border:1px solid #d1d8dd; border-radius:4px; padding:2px 6px; text-transform:uppercase;"
                    placeholder="I/N/R/M"
                    onchange="employee_salary_update_transaction_type('${salary_slip}', this.value)">
            `;
		}

		return value;
	},
};


// ─────────────────────────────────────────────
// WHITELISTED UPDATE HELPER
// ─────────────────────────────────────────────

window.employee_salary_update_transaction_type = function (salary_slip, value) {
	frappe.call({
		method: "sanc_report.sanc_report.report.employee_salary_report.employee_salary_report.update_transaction_type",
		args: {
			salary_slip: salary_slip,
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
				let row = data.find((d) => d.salary_slip === salary_slip);

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