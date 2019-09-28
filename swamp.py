import subprocess
import json
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
print()
print(Fore.YELLOW + """ .d8888b. 888       888       d8888888b     d8888888888b. 
d88P  Y88b888   o   888      d888888888b   d8888888   Y88b
Y88b.     888  d8b  888     d88P88888888b.d88888888    888
 "Y888b.  888 d888b 888    d88P 888888Y88888P888888   d88P
    "Y88b.888d88888b888   d88P  888888 Y888P 8888888888P" 
      "88888888P Y88888  d88P   888888  Y8P  888888       
Y88b  d88P8888P   Y8888 d8888888888888   "   888888       
 "Y8888P" 888P     Y888d88P     888888       888888       """)

print()
print(Fore.GREEN + "An OSINT tool for Google Analytics ID Reverse lookup")
print(Fore.RED + "By Jake Creps | With help from Francesco Poldi")
print()
id = input(Fore.YELLOW + "[!] " + Fore.GREEN + "Insert Google Analytics ID: " + Fore.WHITE) #UA-6888464-2
api_call = 'curl -s -X GET https://urlscan.io/api/v1/search/?q=' + id + ' -o "output.json" > /dev/null'
print(Fore.YELLOW + "[+] " + Fore.RED + "Searching for associated URLs...")

#Call API
subprocess.call(api_call, shell=True)

#Open JSON File

tempDict = {}
jsonFile = open('output.json', 'r')
values = json.load(jsonFile)
for i in range (0, len (values['results'])):
    url = values['results'][i]['page']['url']
    try:
        _ = tempDict[url]
    except KeyError:
        tempDict.update({url: True})
        print(Fore.YELLOW + "[!] " + Fore.GREEN + "URL: " + Fore.WHITE + url)
jsonFile.close()
