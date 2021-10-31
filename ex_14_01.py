import ssl
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    url=input("ENTER THE URL:")
    if url=="DONE":
        break
    xml=urllib.request.urlopen(url,context=ctx).read()
    tree=ET.fromstring(xml)
    lst=tree.findall("comments/comment")
    lst1=[]
    print("TOTAL COMMENTS :",len(lst))
    for item in lst:
        x=int(item.find('count').text)
        lst1.append(x)
    print("TOTAL COUNT :",sum(lst1))
    print("ENTER DONE IF YOU WANT EXIT")
