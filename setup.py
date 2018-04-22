#Setup Script for Orphic Virus Generator.
import time
import imp
import os
import pip


def __main__():

        print(""" 

             ██████╗ ██████╗ ██████╗ ██╗  ██╗██╗ ██████╗
            ██╔═══██╗██╔══██╗██╔══██╗██║  ██║██║██╔════╝
            ██║   ██║██████╔╝██████╔╝███████║██║██║     
            ██║   ██║██╔══██╗██╔═══╝ ██╔══██║██║██║     
            ╚██████╔╝██║  ██║██║     ██║  ██║██║╚██████╗
             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝

                ||  Anti Chrome Modules Installer ||      
    """)
        print("==========================================================")
        print("[+] Checking & Installing Required Modules...")
        print("==========================================================")
        time.sleep(2)
        print("==========================================================")
        print("[+] Checking if ipgetter exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('ipgetter')
            exists = True
        except ImportError:
            exists = False
        print("[+] ipgetter Exists : ", exists)
        if(exists == False):
            print("[-] ipgetter not installed, Installing..")
            pip.main(['install', 'ipgetter'])
        else:
            print("[+] ipgetter is Installed.")

        print("==========================================================")
        print("[+] Checking if sqlite3 exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('sqlite3')
            exists = True
        except ImportError:
            exists = False
        print("[+] sqlite3 Exists : ", exists)
        if(exists == False):
            print("[-] sqlite3 not installed, Installing..")
            pip.main(['install', 'sqlite3'])
        else:
            print("[+] sqlite3 is Installed.")

    
        print("==========================================================")
        print("[+] Checking if win32crypt[pywin32] exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('win32crypt[pywin32]')
            exists = True
        except ImportError:
            exists = False
        print("[+] win32crypt[pywin32] Exists : ", exists)
        if(exists == False):
            print("[-] win32crypt[pywin32] not installed, Installing..")
            pip.main(['install', 'pywin32'])
        else:
            print("[+] win32crypt[pywin32] is Installed.")


        print("==========================================================")
        print("[+] Checking if smtplib exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('smtplib')
            exists = True
        except ImportError:
            exists = False
        print("[+] smtplib Exists : ", exists)
        if(exists == False):
            print("[-] smtplib not installed, Installing..")
            pip.main(['install', 'smtplib'])
        else:
            print("[+] smtplib is Installed.")

        print("==========================================================")
        print("[+] Checking if socket exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('socket')
            exists = True
        except ImportError:
            exists = False
        print("[+] socket Exists : ", exists)
        if(exists == False):
            print("[-] socket not installed, Installing..")
            pip.main(['install', 'socket'])
        else:
            print("[+] socket is Installed.")

        print("==========================================================")
        print("[+] Checking if psutil exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('psutil')
            exists = True
        except ImportError:
            exists = False
        print("[+] psutil Exists : ", exists)
        if(exists == False):
            print("[-] psutil not installed, Installing..")
            pip.main(['install', 'psutil'])
        else:
            print("[+] psutil is Installed.")

        
        print("==========================================================")
        print("[+] Checking if platform exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('platform')
            exists = True
        except ImportError:
            exists = False
        print("[+] platform Exists : ", exists)
        if(exists == False):
            print("[-] platform not installed, Installing..")
            pip.main(['install', 'platform'])
        else:
            print("[+] platform is Installed.")

        print("==========================================================")
        print("[+] Checking if datetime exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('datetime')
            exists = True
        except ImportError:
            exists = False
        print("[+] datetime Exists : ", exists)
        if(exists == False):
            print("[-] datetime not installed, Installing..")
            pip.main(['install', 'psutil'])
        else:
            print("[+] datetime is Installed.")

        print("==========================================================")
        print("[+] Checking if os exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('os')
            exists = True
        except ImportError:
            exists = False
        print("[+] os Exists : ", exists)
        if(exists == False):
            print("[-] os not installed, Installing..")
            pip.main(['install', 'os'])
        else:
            print("[+] os is Installed.")

        print("==========================================================")
        print("[+] Checking if time exists...")
        print("==========================================================")
        time.sleep(2)
        try:
            imp.find_module('time')
            exists = True
        except ImportError:
            exists = False
        print("[+] time Exists : ", exists)
        if(exists == False):
            print("[-] time not installed, Installing..")
            pip.main(['install', 'time'])
        else:
            print("[+] time is Installed.")

        input("[*] Done, Now Orphic Anti Chrome can be Compiled easily. Hit Enter..")
        exit
        

if __name__ == '__main__':
    __main__()