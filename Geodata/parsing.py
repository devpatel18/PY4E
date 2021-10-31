import urllib.request,urllib.parse,urllib.error
import ssl
import json
import time
import http
import sys
import sqlite3

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
#if you have google api enter here
if api_key is False :
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

con = sqlite3.connect('geodata.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations(
address TEXT,
geodata TEXT
)
''')

count = 0
fh = open("where.data")
for line in fh:
    if count > 200 :
        print("Retrieved 200 locations : Please restart to retrieve more.")
        break

    address = line.strip()
    print('')
    cur.execute('SELECT geodata FROM Locations WHERE address = ?',(memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print("Found in database :",address)
        continue

    except:
        pass

    parms = {}
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    url_handle = urllib.request.urlopen(url,context=ctx).read().decode()
#added this if statement as a part of the assignment
    if address == "Borivali":
        print("Retrieved : Borivali",len(url_handle), 'characters')
    print("Retrieved :",len(url_handle), 'characters', url_handle[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(url_handle)

    except:
        print(url_handle)
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(url_handle)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(url_handle.encode()) ) )

    con.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(2)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
