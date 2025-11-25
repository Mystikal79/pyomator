import requests
r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=6aaeac25a032410cbf1b8172b94c28c5')
content = r.jason()
print(content)