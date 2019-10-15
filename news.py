import json, requests, random
ran=random.randint(1,15)
resp = requests.get('https://newsapi.org/v2/top-headlines?country=ru&apiKey=')
data = json.loads(resp.text)
print(data["articles"][ran]["title"])
print(data["articles"][ran-1]["title"])
print(data["articles"][ran+1]["title"])





