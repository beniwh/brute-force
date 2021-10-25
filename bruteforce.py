#!/usr/bin/python
'''
==========================================================
               Brute-force script for Linux
You can pass the wordlist by argument or in the run time.
==========================================================

'''
print("Loading Bhonori......")

import os
import sys
import crypt
import colorama
from colorama import Fore, Back
os.system("cls" if os.name == "nt" else "clear")

#print banner
def print_banner():
    print(Fore.BLUE)
    print ('''
    888      888                                         d8b 
    888      888                                         Y8P 
    888      888                                             
    88888b.  88888b.   .d88b.  88888b.   .d88b.  888d888 888 
    888  88b 888  88b d88  88b 888  88b d88  88b 888P    888 
    888  888 888  888 888  888 888  888 888  888 888     888 
    888 d88P 888  888 Y88..88P 888  888 Y88..88P 888     888 
    p88888P  888  888   Y88P   888  888   Y88P   888     888 ''')
    print(Fore.RESET)

#setup options
print_banner()

#get hash
print(Fore.YELLOW  + "Full Hash: " + Fore.RESET, end="")
full_hash = input()

#extract Salt
tmp = full_hash.split("$")
salt = "$" + tmp[1] + "$" + tmp[2] + "$"
print(Fore.YELLOW  + "Hash Salt: " + Fore.RESET + salt)

#get wordlist:
if len(sys.argv) == 2:
    wordlist = sys.argv[1]
    print(Fore.YELLOW  + "Wordlist: " + Fore.RESET + wordlist)
else:
    print(Fore.YELLOW  + "Wordlist: " + Fore.RESET, end="")
    wordlist = input()

#open wordlist
try:
    with open(wordlist, "r", encoding='iso8859_15') as fl:
        words = fl.read().split("\n")
    print(Fore.YELLOW  + "Wordlist Size: " + Fore.RESET + str(len(words)))
except Exception as error:
    print("")
    print(Fore.WHITE + Back.YELLOW )
    print("Failed to load wordlist.")
    print(error)
    print(Fore.RESET + Back.RESET)
    sys.exit()

#cracking loop
input(Fore.YELLOW  + "Ready. Press ENTER to go." + Fore.RESET)
print("")
for word in words:
    tmp = crypt.crypt(word, salt)
    if tmp == full_hash:
        print(Fore.RED + "[+] {0} - {1}".format(word, tmp))
        print("[OK] Your key was found." + Fore.RESET)
        sys.exit()
    else:
        print(Fore.YELLOW  + "[-]" + Fore.RESET + " {0}".format(word) + Fore.YELLOW  + " - " + Fore.RESET + "{0}".format(tmp))
print("\n" + Fore.YELLOW  + "[FAIL] No password was found." + Fore.RESET)
