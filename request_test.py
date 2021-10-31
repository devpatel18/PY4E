import requests
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
print(r)
json = r.json()
print(json.keys())
print(r.encoding)
