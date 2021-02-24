#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet NMAPEZ")
print("""
welcome to nmapEZ
1) fast scan
2) fast scan plus
3) intense scan
4) instense scan all tcp ports
5) ping
6) service info
7) system info

""")

islemno = raw_input("chose a number:")
if (islemno=="1"):
            ipadress = raw_input("insert ip to scan:")
            os.system("nmap -T4 -F " + ipadress)
elif(islemno=="2"):
             ipadress = raw_input("insert ip to scan:")
             os.system("nmap -sV -T4 -O -F --version-light " + ipadress)
elif(islemno=="3"):
             ipadress = raw_input("insert ip to scan:") 
             os.system("nmap -T4 -A -v " + ipadress)
elif(islemno=="4"):
             ipadress = raw_input("insert ip to scan:")
             os.system("nmap -p 1-65535 -T4 -A -v " + ipadress)
elif(islemno=="5"):
             ipadress = raw_input("insert ip to scan:")
             os.system("nmap -sn " + ipadress)
elif(islemno=="6"):
             ipadress = raw_input("insert ip to scan:")
             os.system("nmap -sS -sV " + ipadress)
elif(islemno=="7"):
             ipadress = raw_input("insert ip to scan:")
             os.system("nmap -0 " + ipadress)
else:
      print("invalid number bro :(")
