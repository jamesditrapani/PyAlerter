#!/usr/bin/python3

from mailer import Mailer
from mailer import Message

class alerter():
		
	def format_alert(email_to, email_from, email_subject, alert_severity, alert_summary, alert_host, alert_module, alert_timestamp, alert_data):
		with open('alert_template.html', 'r') as alert_template:
			html_template = alert_template.read().format(alert_severity, alert_summary, alert_host, alert_module, alert_timestamp, alert_data)
			#html_template = alert_template.read()
			alerter.send_alert(email_to, email_from, email_subject, html_template)

	def send_alert(email_to, email_from, email_subject, html_template):
		message = Message(From=email_from, To=email_to)
		message.Subject = email_subject
		message.Html = html_template
		sender = Mailer('localhost')
		sender.send(message)
