import requests

url = 'https://search.kompas.com/search/?q=coronavirus&submit=Submit'
res = requests.get(url).text

print(res)
