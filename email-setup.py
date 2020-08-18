import smtplib
import json


with open('email-creds.json') as creds:
    email_creds = json.load(creds)

server = email_creds['server']
port = email_creds['port']
username = email_creds['username']
password = email_creds['password']
from_addrs = email_creds['email']

to_addrs = ["aayushkapoor.bhms@gmail.com"]
email_msg = "DUMMY"
email_subject = "TEST"


def msg_formatter(to_addrs, msg, subject):
    """format email message to send

    Args:
        to_addrs ([str]): [list of email addresses]
        msg (str): [string of email-text message]
        subject (str): [email subject line]

    Returns:
    Properly formatted message
    """

    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\ %s""" % (
        from_addrs, ", ".join(to_addrs), subject, msg)

    return message


def connection(server_name, port, username, password):
    server = smtplib.SMTP(server_name, port)
    server.connect(server_name, port)
    server.ehlo()
    server.starttls()  # I NEED TO MAKE THIS OPTIONAL SOMEHOW
    server.ehlo()
    server.login(username, password)
    print("Connection is successful")
    return server


server = connection(server, port, username, password)
for i in range(100):
    msg = msg_formatter(to_addrs, email_msg, email_subject)
    server.sendmail(from_addrs, to_addrs, msg)
server.quit()
print("Email message sent successfully")
