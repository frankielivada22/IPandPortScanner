import threading
import random
import socket
import time
import sys
import os
from colorama import Fore, Back, Style

print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░███░█░▄▄█░██▀▄▀█▀▄▄▀█░▄▀▄░█░▄▄
██░█░█░█░▄▄█░██░█▀█░██░█░█▄█░█░▄▄
██▄▀▄▀▄█▄▄▄█▄▄██▄███▄▄██▄███▄█▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
	""")
print("")
print("Scanning IP's.")

print("Testing...")
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((ip,8080))
if result == 0:
	print(ip, Fore.GREEN+"8080 Port is open")
	print(Style.RESET_ALL)
else:
	print(ip, Fore.RED+"8080 Port is not open")
	print(Style.RESET_ALL)
result = sock.connect_ex((ip,80))
if result == 0:
	print(ip, Fore.GREEN+"80 Port is open")
	print(Style.RESET_ALL)
else:
	print(ip, Fore.RED+"80 Port is not open")
	print(Style.RESET_ALL)
result = sock.connect_ex((ip,443))
if result == 0:
	print(ip, Fore.GREEN+"443 Port is open")
	print(Style.RESET_ALL)
else:
	print(ip, Fore.RED+"443 Port is not open")
	print(Style.RESET_ALL)

print("Please wait while I start")
time.sleep(5)



def f():
	while True:
		ip = ".".join(map(str, (random.randint(0, 255) 
							for _ in range(4))))
		print(ip)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((ip,8080))
		if result == 0:
			print(ip, Fore.GREEN+"8080 Port is open")
			print(Style.RESET_ALL)
			f = open("8080.txt", "a")
			f.write(ip+":"+"8080")
		else:
			print(ip, Fore.RED+"8080 Port is not open")
			print(Style.RESET_ALL)

		result = sock.connect_ex((ip,80))
		if result == 0:
			print(ip, Fore.GREEN+"80 Port is open")
			print(Style.RESET_ALL)
			f = open("80.txt", "a")
			f.write(ip+":"+"80")
		else:
			print(ip, Fore.RED+"80 Port is not open")
			print(Style.RESET_ALL)

		result = sock.connect_ex((ip,443))
		if result == 0:
			print(ip, Fore.GREEN+"443 Port is open")
			print(Style.RESET_ALL)
			f = open("443.txt", "a")
			f.write(ip+":"+"443")
		else:
			print(ip, Fore.RED+"443 Port is not open")
			print(Style.RESET_ALL)

		print("")
		print("")




if __name__ == '__main__':
	for i in range(1000):
		t = threading.Thread(target=f)
		time.sleep(0.2)
		t.start()