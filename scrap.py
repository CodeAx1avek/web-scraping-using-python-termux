import os
from re import A
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install urllib3')
os.system('pip install bs4')
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


import pyfiglet


R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(R+br)
print(G+'''
[Scrap Your Content From Website ]
Coded By CodeAx1
_________________________________________________''')
try:
    userurl = input('Enter Your valid full url like http://www.:')
    url = urlopen(userurl)
    bs = BeautifulSoup(url.read(), 'html.parser')
        
    
    while True:
        try:
            print(B,'Type A for Scrap Title')
            print(B,'Type B for scrap Heading')
            print(B,'Type C for Scrap paragraph')
            print(B,'Type D for scrap All content')
            print(B,'Type E to quit this script')

            user = input("Enter Your Number:")
            if user.upper() == 'A':
                print(G,'You selected A For Scarping Title')
                print(Y,(bs.title))
            if user.upper() == 'B':
                print(G,'You selected B For Scarping Heading')
                print(Y,(bs.h1))
            if user.upper() == 'C':
                print(G,'You selected C For Scarping Paragraph')
                print(Y,(bs.p))
            if user.upper() == 'D':
                def dd(url):
                    return urllib.request.urlopen(url).read()
                scrapall = dd(userurl)
                print(G,'You selected D For Scarping All Content')
                print(Y,(scrapall))
            if user.upper() == "E":
                print(G,'You selected E For Exitting this script...By CodeAx1')
                print(Y,'We Are Quitting Our Script')
                print(Y,'Thank You For using CodeAx1 Script')
                break
        except:
            print('Somthing Wromg or wott?')
except:
    print('SomeThing Wromg')
