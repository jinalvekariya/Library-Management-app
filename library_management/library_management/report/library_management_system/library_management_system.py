# Copyright (c) 2023, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import re
from frappe.utils import formatdate
from collections import defaultdict
from frappe.model.document import Document
from frappe import _
from frappe.utils import *
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns()
    data = get_library_member(filters)
    message = None
    return columns, data, message
 

def get_columns():
    columns = [
        {
            'fieldname': 'full_name',
            'label': 'Full Name',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'email_address',
            'label': 'Email Address',
            'fieldtype': 'Data',
            'options': 'Email'
        },
        {
            'fieldname': 'phone',
            'label': 'Phone',
            'fieldtype': 'Phone',
            'options': 'Phone'
        },
        {
            'fieldname': 'date_of_birth',
            'label': 'Date of Birth',
            'fieldtype': 'Date'
        },
        {
            'fieldname': 'age',
            'label': 'Age',
            'fieldtype': 'Float'
        } 
    ]
    return columns	

def get_library_member(filters=None):
    data = []
    filter = []
    if filters.get('full_name'):
        full_name=filters.get('full_name')
        filter.append({'full_name':full_name})
        
    if filters.get('email_address'):
        email_address=filters.get('email_address')
        filter.append({'email_address':email_address})
        
    library_member_data = frappe.db.get_list("Library Member", filters=filter, fields=["full_name", "email_address", "phone", "date_of_birth", "age"])
    for d in library_member_data:
        row = {
            'full_name': d.full_name,
            'email_address': d.email_address,
            'phone': d.phone,
            'date_of_birth': d.date_of_birth,
            'age': d.age
            }
        data.append(row)
    return data

def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value
    return conditions