# PyAlerter

## About
Basic Python module to send alerts using local SMTP relay by passing data into pre defined variables. Currently, this script expects your SMTP relay to be running on localhost:25.

## Usage
Import module to Python script using:
```python
from python_alerter import alerter
```

Execute using:
```python
alerter.format_alert(email_to, email_from, email_subject, alert_severity, alert_summary, alert_host, alert_module, alert_timestamp, alert_data)
```

PyAlerter currently expects you to pass the below variables to `format_alert()`:
```python
email_to = # Email you wish to send to
email_from = # Email you wish to send from
email_subject = # Subject of the alert email
alert_severity = # Severtiy of the alert, e.g. Critical, Warning, Non-Critical etc.
alert_summary = # Brief summary of the alert
alert_host = # Host of the alert in question
alert_module = # Track which class/script the alert has sourced from. This is handy if there are multiple scripts reporting into PyAlerter
alert_timestamp = # Pass a timestamp for the alert
alert_data = # Any other data you wish to pass
```


## Example

![Example](https://i.imgur.com/RifVONK.png)

```python
from PyAlerter import alerter

email_to = 'alerts@domain.com'
email_from = 'root@domain.com'
email_subject = 'CRITICAL: BGP PEER DOWN'
alert_severity = 'CRITICAL'
alert_summary = 'BGP Session with 192.168.1.2 - DOWN'
alert_host = 'server1.domain.com'
alert_module = 'BGP-MON'
alert_timestamp = '13:34:33 24/06/2019'
alert_data = "Insert more information here"

alerter.format_alert(email_to, email_from, email_subject, alert_severity, alert_summary, alert_host, alert_module, alert_timestamp, alert_data)
```
