from __future__ import unicode_literals
import frappe


def get_context(context):
    context.articles = frappe.db.get_all('Article', '*')