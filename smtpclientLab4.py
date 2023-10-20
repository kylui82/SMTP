import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText

email_sender = 'testingnetworking1@gmail.com'
email_password = ''
email_receiver = 'testingnetworking1@gmail.com'
email_cc = 'kylui82@gmail.com,catabc82@gmail.com'
subject = 'Text message'
body = """  This is a test email implementing smtp protocol """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em["Cc"] = email_cc
em.set_content(body)

filename = "example.txt"
em.attach(MIMEText(open(filename).read()))

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 587, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, email_cc, em.as_string())
  smtp.quit()

