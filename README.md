# Web_Scraping_with_python

Website Scarping like Title tag,heading tag and paragraph tag..
this script is made with python using python libraries like urllib and bs4.
small and simple project here..





## Installation

- Run This Code in Vscode,pycharm and other virtual env of python


- open your favourate virtual env which support python
- copy and save code with .py extension

## Deployment

To deploy this project run

```bash
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
```
## Deployment
To deploy this On Window Or Termux
copy and paste
```bash
  apt update && apt upgrade
```
```bash
 git clone https://github.com/CodeAvek/Web_Scraping_with_python.git
```
```bash
  ls
```
Now For Window Paste
```bash
python scarp.py
```
For Termux Paste
```bash
scarptermux.py
```
## 🔗 Youtube Link
[![Youtube](https://i.ytimg.com/an_webp/uvLpcxtDBTs/mqdefault_6s.webp?du=3000&sqp=COCqmJUG&rs=AOn4CLDIMLwUwogks5YAjQfDy2m8PnaMQw)](https://www.youtube.com/watch?v=uvLpcxtDBTs)
