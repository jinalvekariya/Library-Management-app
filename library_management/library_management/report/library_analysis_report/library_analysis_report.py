# # Copyright (c) 2023, Frappe and contributors
# # For license information, please see license.txt

# # import frappe


def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data


	chart = {
		"type": "bar",
		"data": {
			"labels": ["Monday", "Tuesday", "wednesday", "Thursday", "Friday"],
			"databases": [
				{"name": "Some Data", "values": [25, 40, 30, 35, 8]},
				{"name": "Author Set", "values": [25, 50, -10, 15, 18]},
			],
		}
	}

	columns = [
		{'fieldtype': 'Data', 'label': 'Book Name', 'fieldname': 'book_name', 'width': 100},
		{'fieldtype': 'Data', 'label': 'Author', 'fieldname': 'author', 'width': 100},
	]

	result = [
		{'book_name': 'Book 1', 'author': 'Author 1'},
		{'book_name': 'Book 2', 'author': 'Author 2'},
		{'book_name': 'Book 3', 'author': 'Author 3'},
	]

	return columns, result, None, chart