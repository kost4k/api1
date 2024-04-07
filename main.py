import requests

url = "http://www.boredapi.com/api/activity/?lang=ru"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    activity = data['activity']
    print("Случайная активность: ", activity)
else:
    print("Не удалось получить активность. Код статуса:", response.status_code)
