// Copyright (c) 2023, Frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Analysis Report"] = {
	formatter: function(value, row, column, data, default_formatter) {
		if(column.fieldname === 'age') {
			if(value > 6){
				return `<span class="text-success">${value}</span>`
			}
			return `<span class="text-danger">${value}<span>`
		}
		return value
	}
};
