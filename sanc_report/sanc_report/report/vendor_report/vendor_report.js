// // Copyright (c) 2026, Sanc and contributors
// // For license information, please see license.txt

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

// 		// Download RBI Adapter Notepad Data
// 		//
// 		// Transaction Type is already populated by the Python report
// 		// from Payment Entry.custom_transaction_type:
// 		//
// 		// HDFC -> I
// 		// NEFT -> N
// 		// RTGS -> R
// 		// IMPS -> M
// 		//
// 		// The current value shown in the report grid is used
// 		// as the first field of the downloaded RBI line.

// 		report.page.add_inner_button(
// 			__("Download Notepad Data"),
// 			function () {

// 				let data = report.data;

// 				if (!data || !data.length) {
// 					frappe.msgprint(
// 						__("No data to download. Please run the report first.")
// 					);

// 					return;
// 				}

// 				let lines = data
// 					.map((row) => {

// 						let line = row["notepad_data"];

// 						if (
// 							line === undefined ||
// 							line === null ||
// 							line === ""
// 						) {
// 							return null;
// 						}

// 						// Get Transaction Type from the current report row.
// 						//
// 						// This value comes from:
// 						// Payment Entry.custom_transaction_type
// 						//
// 						// Backend mapping:
// 						// HDFC -> I
// 						// NEFT -> N
// 						// RTGS -> R
// 						// IMPS -> M

// 						let currentType =
// 							row["transaction_type"];

// 						if (
// 							currentType !== undefined &&
// 							currentType !== null &&
// 							currentType !== ""
// 						) {

// 							let parts =
// 								line.split(",");

// 							// Transaction Type is RBI field 1.
// 							parts[0] = currentType;

// 							line =
// 								parts.join(",");
// 						}

// 						return line;
// 					})
// 					.filter(
// 						(line) =>
// 							line !== undefined &&
// 							line !== null &&
// 							line !== ""
// 					);

// 				if (!lines.length) {

// 					frappe.msgprint(
// 						__("Notepad data column is empty.")
// 					);

// 					return;
// 				}

// 				let content =
// 					lines.join("\n");

// 				let blob =
// 					new Blob(
// 						[content],
// 						{
// 							type: "text/plain"
// 						}
// 					);

// 				let link =
// 					document.createElement("a");

// 				link.href =
// 					window.URL.createObjectURL(
// 						blob
// 					);

// 				link.download =
// 					"RBI_Adapter_Vendor_" +
// 					frappe.datetime.now_date() +
// 					".txt";

// 				document.body.appendChild(
// 					link
// 				);

// 				link.click();

// 				document.body.removeChild(
// 					link
// 				);
// 			}
// 		);
// 	}
// };


// Copyright (c) 2026, Sukku and contributors
// For license information, please see license.txt

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

	// ============================================================
	// ONLY TRANSACTION TYPE IS EDITABLE
	// ============================================================

	get_datatable_options: function (datatable_options) {

		datatable_options.getEditor = function (
			colIndex,
			rowIndex,
			value,
			parent,
			column,
			row,
			data
		) {

			// Do not make any other column editable.
			if (column.id !== "transaction_type") {
				return false;
			}

			// Normal text input because
			// Payment Entry.custom_transaction_type
			// is a Data field.

			let input =
				document.createElement("input");

			input.type = "text";

			input.className =
				"form-control";

			input.style.width =
				"100%";

			input.style.height =
				"100%";

			input.style.boxSizing =
				"border-box";

			input.style.padding =
				"4px 8px";

			parent.appendChild(input);

			return {

				initValue: function (value) {

					input.value =
						value || "";

					input.focus();

					input.select();
				},

				setValue: function (value) {

					input.value =
						value || "";
				},

				getValue: function () {

					return input.value;
				}
			};
		};

		return datatable_options;
	},

	onload: function (report) {

		// ============================================================
		// DOWNLOAD NOTEPAD DATA
		// ============================================================

		report.page.add_inner_button(
			__("Download Notepad Data"),
			function () {

				let data =
					frappe.query_report.data;

				if (!data || !data.length) {

					frappe.msgprint(
						__(
							"No data to download. Please run the report first."
						)
					);

					return;
				}

				let lines = data
					.map(function (row) {

						let notepad_line =
							row["notepad_data"];

						if (
							notepad_line === undefined ||
							notepad_line === null ||
							notepad_line === ""
						) {
							return null;
						}

						// Get current Transaction Type.
						let current_transaction_type =
							row["transaction_type"];

						let parts =
							notepad_line.split(",");

						// Replace only the first field.
						if (
							current_transaction_type !== undefined &&
							current_transaction_type !== null
						) {

							parts[0] =
								current_transaction_type;
						}

						return parts.join(",");
					})
					.filter(function (line) {

						return (
							line !== null &&
							line !== ""
						);
					});

				if (!lines.length) {

					frappe.msgprint(
						__(
							"Notepad data column is empty."
						)
					);

					return;
				}

				let content =
					lines.join("\n");

				let blob =
					new Blob(
						[content],
						{
							type: "text/plain"
						}
					);

				let link =
					document.createElement("a");

				link.href =
					window.URL.createObjectURL(
						blob
					);

				link.download =
					"RBI_Adapter_Vendor_" +
					frappe.datetime.now_date() +
					".txt";

				document.body.appendChild(
					link
				);

				link.click();

				document.body.removeChild(
					link
				);
			}
		);
	}
};