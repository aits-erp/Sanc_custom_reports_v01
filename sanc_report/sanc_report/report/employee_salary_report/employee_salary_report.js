
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

// 		report.page.add_inner_button(
// 			__("Download Notepad Data"),
// 			function () {

// 				// Pull CURRENT grid data so that if the user
// 				// manually changes Transaction Type, that
// 				// changed value is used in the download.

// 				let data = frappe.query_report.data;

// 				if (!data || !data.length) {

// 					frappe.msgprint(
// 						__(
// 							"No data to download. Please run the report first."
// 						)
// 					);

// 					return;
// 				}

// 				let lines = data
// 					.map((row) => {

// 						let notepad_line =
// 							row["notepad_data"];

// 						if (
// 							notepad_line === undefined ||
// 							notepad_line === null ||
// 							notepad_line === ""
// 						) {
// 							return null;
// 						}

// 						// Transaction Type comes from:
// 						//
// 						// Salary Slip.custom_transaction_type
// 						//
// 						// Backend mapping:
// 						//
// 						// IMPS   -> I
// 						// NEFT   -> N
// 						// RTGS   -> R
// 						// UPI    -> M
// 						// MOBILE -> M

// 						let parts =
// 							notepad_line.split(",");

// 						let current_transaction_type =
// 							row["transaction_type"];

// 						// Replace the first RBI field with
// 						// the current Transaction Type value.

// 						if (
// 							current_transaction_type !== undefined &&
// 							current_transaction_type !== null
// 						) {
// 							parts[0] =
// 								current_transaction_type;
// 						}

// 						return parts.join(",");
// 					})
// 					.filter(
// 						(line) =>
// 							line !== null &&
// 							line !== ""
// 					);

// 				if (!lines.length) {

// 					frappe.msgprint(
// 						__(
// 							"Notepad data column is empty."
// 						)
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
// 					"RBI_Adapter_" +
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

	// ------------------------------------------------------------
	// ONLY Transaction Type column is editable.
	//
	// It is a normal text input because Salary Slip
	// custom_transaction_type is a Data field.
	// ------------------------------------------------------------

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

			// Only Transaction Type should be editable.
			if (column.id !== "transaction_type") {
				return false;
			}

			// Create normal text input.
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

				// When user opens the cell.
				initValue: function (value) {

					input.value =
						value || "";

					input.focus();

					input.select();
				},

				// When DataTable sets a value.
				setValue: function (value) {

					input.value =
						value || "";
				},

				// Value entered by user.
				getValue: function () {

					return input.value;
				}
			};
		};

		return datatable_options;
	},

	onload: function (report) {

		// ------------------------------------------------------------
		// DOWNLOAD NOTEPAD DATA
		// ------------------------------------------------------------

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

						// ------------------------------------------------
						// Get CURRENT Transaction Type value.
						//
						// If client edited the report cell,
						// the edited value is used here.
						// ------------------------------------------------

						let current_transaction_type =
							row["transaction_type"];

						let parts =
							notepad_line.split(",");

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
					"RBI_Adapter_" +
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