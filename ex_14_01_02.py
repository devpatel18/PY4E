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
    lst1=tree.findall('.//count')
    lst2=[]
    for item in lst1:
        x=int(item.text)
        lst2.append(x)
    print("TOTAL COMMENTS :",len(lst))
    print("TOTAL COUNT :",sum(lst2))
    print("ENTER DONE IF YOU WANT EXIT")
