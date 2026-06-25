'''
Program: Port Scanner
Language: Python 3
---------------------------------------------------------
Computer: Desktop PC/Windows 10 Pro
Code Editor: Windows Notepad
Code Output: Windows command prompt
---------------------------------------------------------
Code borrowed from: 
YouTube Channel: Vinsloev Academy
Python Cybersecurity For Beginners - Build a Port Scanner 
https://www.youtube.com/watch?v=bH-3PuQC_n0
---------------------------------------------------------
Created: 11:58 28/08/2022
Updated: 11:58 28/08/2022
'''

from socket import *
def conScan(tgtHost,tgtPort):
   try:
      connskt = socket(AF_INET,SOCK_STREAM)
      connskt.connect((tgtHost,tgtPort))
      print('[+]%d/tcp open'% tgtPort)
      connskt.close()
   except:
      print('[-]%d/tcp closed'% tgtPort)

def portScan(tgtHost,tgtPorts):
   try:
      tgtIP = gethostbyname(tgtHost)
   except: 
      print('[-] Cannot resolve %d '% tgtHost)
      return
   try:
      tgtName = gethostbyaddr(tgtIP)
      print('\n[+] Scan result of: %s ' % tgtName[0])
   except:
      print('\n[+] Scan result of: %s ' % tgtIP)
   setdefaulttimeout(1)
   for tgtPort in tgtPorts:
      print('Scanning Port: %d'% tgtPort)
      conScan(tgtHost, int(tgtPort))       

if __name__ == '__main__':
   portScan('google.com',[80,22])
   #conScan('216.58.207.238',22)

'''
Output result...when run...

[+] Scan result of: 172.217.169.46
Scanning Port: 80
[+]80/tcp open
Scanning Port: 22
[-]22/tcp closed
'''
