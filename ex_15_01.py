import json
import ssl
import urllib.request,urllib.parse,urllib.error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    url=input("ENTER URL:")
    if len(url)<1:
        break
    try:
        url_handle=urllib.request.urlopen(url,context=ctx).read().decode()
    except:
        print("ERROR")

    print("Retrived:",len(url_handle),"contents")

    try:
        js=json.loads(url_handle)
    except:
        print("Parsing failed")

    comments=js["comments"]

    sum=0
    for comment in comments:
        ct=int(comment["count"])
        sum=sum+ct

    print("Total count:",sum)
