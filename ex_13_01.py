
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("ENTER URL:")
try:
    html=urllib.request.urlopen(url,context=ctx).read()
except:
    print("url not found.")
    quit()
soup=BeautifulSoup(html,'html.parser')
tags= soup('span')

list=[]
for tag in tags:
    x=int(tag.contents[0])
    list.append(x)
print("THE SUM IS :",sum(list))
