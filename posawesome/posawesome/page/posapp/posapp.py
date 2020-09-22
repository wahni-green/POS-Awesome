# -*- coding: utf-8 -*-
# Copyright (c) 2020, Youssef Restom and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import getdate, now_datetime, nowdate, flt, cint, get_datetime_str, add_days
from frappe import _
from erpnext.accounts.party import get_party_account
from posawesome import console


@frappe.whitelist()
def get_items():
	return frappe.db.sql("""
        select name ,item_code, item_name, image, item_group, stock_uom
        from `tabItem`
        order by name
        LIMIT 0, 10000 """
        , as_dict=1)


@frappe.whitelist()
def get_items_groups():
	return frappe.db.sql("""
        select name 
        from `tabItem Group`
        where is_group = 0
        order by name
        LIMIT 0, 200 """
        , as_dict=1)


@frappe.whitelist()
def get_customer_names():
        customers = frappe.db.sql("""
        select name 
        from `tabCustomer`
        order by name
        LIMIT 0, 10000 """
        , as_dict=1)
        customers_list = []
        for customer in customers:
                customers_list.append(customer["name"])
        return customers_list


# @frappe.whitelist()
# def add_project(pro):
# 	pro = json.loads(pro)
# 	doc = frappe.get_doc(dict(
# 		doctype = "MyProjects",
#         title = pro["title"],
#         content = pro["content"],
#         due = pro["due"],
# 	)).insert()
# 	console("data in" , doc)
# 	return "Project Add"


# @frappe.whitelist()
# def get_all_projects():
# 	console("Trigger get_all_projects")
# 	return frappe.db.sql("""
#         select *
#         from `tabMyProjects`
#         order by name"""
#         , as_dict=1)

