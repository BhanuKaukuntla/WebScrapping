import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

html_text = requests.get('https://indianexpress.com/')
# print(html_text)
soup = BeautifulSoup(html_text.text, 'lxml')
results = soup.find_all('div', class_= 'other-article')

big_data=[]
for result in results:
    data = {}
#     title = result.find('h3', class_= 'main-title').text.strip()
#     contentData = result.find('p', class_ = 'copy')
#     content = contentData.text.strip()
    title = result.h3.a.text
    link = result.h3.a['href']
    image = result.div.a.img['src']
#     category = result.div.a.text.strip()
#     image = result.a.img['src']
#     # downloads the images to local storage
#     with open(title.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
#             im = requests.get(link)
#             img = f.write(im.content)
# #             print('Writing: ', img)
    

    print(f'''
        Title: {title}
        Article Link: {link}
        Image Link: {image}
       
    ''')

    print(' ')

data['title'] = title
# data['content'] = content
data['article_link'] = link
# data['category'] = category
data['image_link'] = image

big_data.append(data)
big_data[0]

client = MongoClient('localhost', 27017)
db = client.scrap

for data in big_data:
    db.big_data.insert_one(data)