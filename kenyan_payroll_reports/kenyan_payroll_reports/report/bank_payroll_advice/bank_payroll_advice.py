# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe, erpnext
from frappe import _

def execute(filters=None):
	
	company_currency = erpnext.get_company_currency(filters.get("company"))
	columns = get_columns()
	data = get_data(filters,company_currency)

	return columns, data

def get_columns():
	columns = [			
		{
		'label': _('Employee ID'),
		'fieldname': 'employee',
		'options': 'Employee',
		'width': 180
		},
		{
		'label': _('Employee Names'),
		'fieldname': 'employee_name',
		'fieldtype': 'Read Only',
		'width': 260
		},
		{
		'label': _('National ID'),
		'fieldname': 'national_id',
		'fieldtype': 'Data',
		'width': 120
		},
		{
		'label': _('Bank Name'),
		'fieldname': 'bank_name',
		'fieldtype': 'Data',
		'width': 190
		},			
		{
		'label': _('Bank Account No'),
		'fieldname': 'bank_account_no',
		'fieldtype': 'Data',
		'width': 150
		},
		{
		'label': _('Workstation'),
		'fieldname': 'branch',
		'fieldtype': 'Data',
		'width': 150
		},
		{
		'label': _('Net Pay'),
		'fieldname': 'net_pay',
		'fieldtype': 'Currency',
		'width': 150
		}
	]
		
	return columns

def get_data(filters,company_currency,conditions=""):
	conditions = get_conditions(filters,company_currency)

	data = frappe.db.sql("""
	SELECT 	ss.employee, ss.employee_name,
	        ss.start_date, ss.end_date, 
			ss.bank_name, ss.bank_account_no,
			ss.branch, ss.net_pay, e.national_id
	FROM `tabSalary Slip` ss, `tabEmployee` e
	WHERE %s
	    and e.name = ss.employee
	""" % conditions, filters, as_dict=1)

	return data

def get_conditions(filters,company_currency):
	conditions = ""
	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

	if filters.get("docstatus"):
		conditions += "ss.docstatus = {0}".format(doc_status[filters.get("docstatus")])

	if filters.get("from_date"): conditions += " and ss.start_date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and ss.end_date <= %(to_date)s"
	if filters.get("company"): conditions += " and ss.company = %(company)s"
	if filters.get("bank_name"): conditions += " and ss.bank_name = %(bank_name)s"
	if filters.get("currency") and filters.get("currency") != company_currency:
		conditions += " and ss.currency = %(currency)s"
	
	return conditions
