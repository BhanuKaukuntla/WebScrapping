import requests

html_text = requests.get('https://timesofindia.indiatimes.com/business')
print(html_text)