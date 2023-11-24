import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/login'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

with open('login.html', 'w', encoding='utf-8') as fl:
    fl.write(str(soup))