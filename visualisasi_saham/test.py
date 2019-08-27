import requests
import json

url = 'https://kurs.web.id/api/v1/bca'
data = requests.get(url)
matauang = data.json()
print(matauang)
