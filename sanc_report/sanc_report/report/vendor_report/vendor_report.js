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



// Copyright (c) 2026, Sanc and contributors
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

	onload: function (report) {

		// Download RBI Adapter Notepad Data
		//
		// Transaction Type is already populated by the Python report
		// from Payment Entry.custom_transaction_type:
		//
		// HDFC -> I
		// NEFT -> N
		// RTGS -> R
		// IMPS -> M
		//
		// The current value shown in the report grid is used
		// as the first field of the downloaded RBI line.

		report.page.add_inner_button(
			__("Download Notepad Data"),
			function () {

				let data = report.data;

				if (!data || !data.length) {
					frappe.msgprint(
						__("No data to download. Please run the report first.")
					);

					return;
				}

				let lines = data
					.map((row) => {

						let line = row["notepad_data"];

						if (
							line === undefined ||
							line === null ||
							line === ""
						) {
							return null;
						}

						// Get Transaction Type from the current report row.
						//
						// This value comes from:
						// Payment Entry.custom_transaction_type
						//
						// Backend mapping:
						// HDFC -> I
						// NEFT -> N
						// RTGS -> R
						// IMPS -> M

						let currentType =
							row["transaction_type"];

						if (
							currentType !== undefined &&
							currentType !== null &&
							currentType !== ""
						) {

							let parts =
								line.split(",");

							// Transaction Type is RBI field 1.
							parts[0] = currentType;

							line =
								parts.join(",");
						}

						return line;
					})
					.filter(
						(line) =>
							line !== undefined &&
							line !== null &&
							line !== ""
					);

				if (!lines.length) {

					frappe.msgprint(
						__("Notepad data column is empty.")
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

