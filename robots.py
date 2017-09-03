# coding : utf-8
# author : Weedatae
# title : Auto Found Robots.txt
import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.GREEN + "\nAuto Found robots.txt...." + Style.RESET_ALL)
print(Fore.CYAN + "Chargement..." + Style.RESET_ALL + "\n")
time.sleep(2)
website = input("Enter a website (http/https) : ")
print(Fore.MAGENTA + "ROBOTS.TXT : \n" + Style.RESET_ALL)
req = requests.get(website + "/robots.txt")
if "User-agent:" in req.text:
 print(req.text)
else: 
	print(Fore.RED + "Error.. (file not found)" + Style.RESET_ALL)