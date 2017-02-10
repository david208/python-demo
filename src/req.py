'''
Created on 2016年10月12日

@author: shim
'''

import requests

from bs4 import BeautifulSoup

response = requests.get("http://www.baidu.com")
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,"lxml")

print(soup.title)
print(soup.body)

for x in soup.findAll("a"):
    print(x['href'])

print(soup.children)



for child in  soup.children:
    print(child)

print(soup.findAll(href='http://home.baidu.com').pop().string)