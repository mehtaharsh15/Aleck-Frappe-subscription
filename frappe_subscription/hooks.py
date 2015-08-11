app_name = "frappe_subscription"
app_title = "Frappe Subscription"
app_publisher = "Indictrans"
app_description = "Frappe Subscription"
app_icon = "icon-shopping-cart "
app_color = "red"
app_email = "contact@indictranstech.com"
app_url = "google.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_subscription/css/frappe_subscription.css"
# app_include_js = "/assets/frappe_subscription/js/frappe_subscription.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_subscription/css/frappe_subscription.css"
# web_include_js = "/assets/frappe_subscription/js/frappe_subscription.js"

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

# Installation
# ------------

# before_install = "frappe_subscription.install.before_install"
# after_install = "frappe_subscription.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_subscription.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Packing Slip": {
		"on_cancel": "frappe_subscription.ec_packing_slip.on_packing_slip_cancel",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_subscription.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_subscription.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_subscription.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_subscription.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_subscription.tasks.monthly"
# 	]
# }

fixtures = ["Custom Field"]

# Testing
# -------

# before_tests = "frappe_subscription.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "frappe_subscription.event.get_events"
# }
