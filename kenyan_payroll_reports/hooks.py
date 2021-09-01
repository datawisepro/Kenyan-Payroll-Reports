from . import __version__ as app_version

app_name = "kenyan_payroll_reports"
app_title = "Kenyan Payroll Reports"
app_publisher = "Navari"
app_description = "Kenyan Payroll Report App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "solutions@navari.co.ke"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kenyan_payroll_reports/css/kenyan_payroll_reports.css"
# app_include_js = "/assets/kenyan_payroll_reports/js/kenyan_payroll_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/kenyan_payroll_reports/css/kenyan_payroll_reports.css"
# web_include_js = "/assets/kenyan_payroll_reports/js/kenyan_payroll_reports.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "kenyan_payroll_reports/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "kenyan_payroll_reports.utils.jinja_methods",
# 	"filters": "kenyan_payroll_reports.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "kenyan_payroll_reports.install.before_install"
# after_install = "kenyan_payroll_reports.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kenyan_payroll_reports.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kenyan_payroll_reports.tasks.all"
# 	],
# 	"daily": [
# 		"kenyan_payroll_reports.tasks.daily"
# 	],
# 	"hourly": [
# 		"kenyan_payroll_reports.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kenyan_payroll_reports.tasks.weekly"
# 	],
# 	"monthly": [
# 		"kenyan_payroll_reports.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "kenyan_payroll_reports.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kenyan_payroll_reports.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "kenyan_payroll_reports.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"kenyan_payroll_reports.auth.validate"
# ]

