'''
    Usage:

    recipient = 'someone@domain.com'
    subject = 'Test message'
    message = 'This is a test message'
    sender = 'someone@gmail.com'

    # send the message
    send_mail(recipient, subject, message, sender)

'''

def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection
    smtp_conn.quit()

    return True

