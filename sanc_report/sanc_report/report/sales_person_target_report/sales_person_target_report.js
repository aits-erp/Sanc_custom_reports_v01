// frappe.query_reports["Sales Person Target Report"] = {

// 	filters: [
// 		{
// 			fieldname: "customer",
// 			label:     __("Customer"),
// 			fieldtype: "Link",
// 			options:   "Customer",
// 			get_query: function () {
// 				return { filters: { disabled: 0 } };
// 			},
// 			on_change: function () {
// 				let customer = frappe.query_report.get_filter_value("customer");
// 				if (customer) {
// 					frappe.db.get_value("Customer", customer, "customer_name", (r) => {
// 						if (r && r.customer_name) {
// 							frappe.query_report.set_filter_value("customer_name", r.customer_name);
// 						}
// 					});
// 				} else {
// 					frappe.query_report.set_filter_value("customer_name", "");
// 				}
// 			},
// 		},
// 		{
// 			fieldname: "customer_name",
// 			label:     __("Customer Name"),
// 			fieldtype: "Data",
// 		},
// 	],

// 	formatter: function (value, row, column, data, default_formatter) {
// 		value = default_formatter(value, row, column, data);
// 		if (!data) return value;

// 		if (data.is_total_row) {
// 			return `<strong style="color:var(--text-color);">${value}</strong>`;
// 		}

// 		if (column.fieldname === "achievement_percent") {
// 			let pct   = flt(data.achievement_percent);
// 			let color = pct >= 100 ? "#28a745"
// 			           : pct >= 75  ? "#fd7e14"
// 			           :              "#dc3545";
// 			return `<span style="color:${color};font-weight:600;">${value}</span>`;
// 		}

// 		if (column.fieldname === "total_balance" && flt(data.total_balance) < 0) {
// 			return `<span style="color:#dc3545;">${value}</span>`;
// 		}

// 		return value;
// 	},
// };





// frappe.query_reports["Sales Person Target Report"] = {

// 	filters: [
// 		{
// 			fieldname: "fiscal_year",
// 			label:     __("Fiscal Year"),
// 			fieldtype: "Link",
// 			options:   "Fiscal Year",
// 			reqd:      1,
// 			default:   frappe.defaults.get_user_default("fiscal_year"),
// 		},
// 		{
// 			fieldname: "customer",
// 			label:     __("Customer"),
// 			fieldtype: "Link",
// 			options:   "Customer",
// 			get_query: function () {
// 				return { filters: { disabled: 0 } };
// 			},
// 		},
// 		{
// 			fieldname: "sales_person",
// 			label:     __("Sales Person"),
// 			fieldtype: "Link",
// 			options:   "Sales Person",
// 		},
// 	],

// 	formatter: function (value, row, column, data, default_formatter) {
// 		value = default_formatter(value, row, column, data);
// 		if (!data) return value;

// 		if (data.is_total_row) {
// 			return `<strong style="color:var(--text-color);">${value}</strong>`;
// 		}

// 		return value;
// 	},
// };



frappe.query_reports["Sales Person Target Report"] = {

	filters: [
		{
			fieldname: "fiscal_year",
			label:     __("Fiscal Year"),
			fieldtype: "Link",
			options:   "Fiscal Year",
			reqd:      1,
			default:   frappe.defaults.get_user_default("fiscal_year"),
		},
		{
			fieldname: "customer",
			label:     __("Customer"),
			fieldtype: "Link",
			options:   "Customer",
			get_query: function () {
				return { filters: { disabled: 0 } };
			},
		},
		{
			fieldname: "sales_person",
			label:     __("Sales Person"),
			fieldtype: "Link",
			options:   "Sales Person",
		},
	],

	formatter: function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (!data) return value;

		if (data.is_total_row) {
			return `<strong style="color:var(--text-color);">${value}</strong>`;
		}

		return value;
	},

	onload: function (report) {
		frappe.db
			.get_list("Fiscal Year", {
				filters:  { disabled: 0 },
				fields:   ["name"],
				order_by: "year_start_date desc",
				limit:    1,
			})
			.then((list) => {
				if (list && list.length) {
					let fy = report.get_filter("fiscal_year");
					if (fy && !fy.get_value()) {
						fy.set_value(list[0].name);
					}
				}
			});
	},
};