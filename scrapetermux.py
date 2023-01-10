import os
os.system('pip install pyfiglet')
os.system('pip install urllib3')
from urllib.request import urlopen


import pyfiglet
os.system('clear')

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(R+br)
print(G+'''
[Scraping Content From Website ]
Coded By CodeAx1
_________________________________________________''')
try:
    userurl = input('Enter Your valid url :')
    url = urlopen(userurl)
    
    while True:
        try:
            print(B,'Type A for Scrap All content')
            print(B,'Type Q to exit this code')

            user = input("Enter Your Number:")
            if user.upper() == 'A':
                print(Y,(url.read()))

                print('We Are Quitting Our Script')
                print('Thank You For using CodeAx1 Script')
                break
        except:
            print('Somthing Wromg or wott?')
except:
    print('SomeThing Wromg')
