import ssl
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("ENTER URL:")
repeat=int(input("ENTER THE NUMBER OF TIMES YOU WANT TO REPEAT THE PROCESS:"))
position=int(input("AT WHAT POSITION:"))
for i in range(repeat):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup("a")
    url=tags[position-1].get("href",None)
    print(url)
