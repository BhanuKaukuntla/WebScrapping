import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://timesofindia.indiatimes.com/business')
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
title = soup.find_all('div', class = 'main-content')