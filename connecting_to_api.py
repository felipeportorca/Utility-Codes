import requests
url= 'digit the url'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
  print(key+ ':', value)
