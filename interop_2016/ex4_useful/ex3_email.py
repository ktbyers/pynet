#!/usr/bin/env python
from email_helper import send_mail

sender = 'ktbyers@twb-tech.com'
recipient = 'ktbyersx@gmail.com'
subject = 'Test email for Interop Python course'
message = '''
This is a test email for Interop Python course
'''

print "Sending email mesage to {}".format(recipient)
send_mail(recipient, subject, message, sender)
