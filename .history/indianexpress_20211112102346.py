import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

html_text = requests.get('https://indianexpress.com/')
soup = BeautifulSoup(html_text.text, 'lxml')
results = soup.find_all('div', class_= 'other-article')

big_data=[]
for result in results:
    data = {}
    title = result.h3.a.text
    link = result.h3.a['href']
    image = result.div.a.img['src']
    with open(title.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)

    print(f'''
        Title: {title}
        Article Link: {link}
        Image Link: {image}
       
    ''')

    print(' ')

data['title'] = title
data['article_link'] = link
data['image_link'] = image

big_data.append(data)
# big_data[0]

client = MongoClient('localhost', 27017)
db = client.scrap

for data in big_data:
    db.big_data.insert_one(data)