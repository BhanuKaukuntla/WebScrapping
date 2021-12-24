from pymongo.mongo_client import MongoClient
import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.firstpost.com/')
soup = BeautifulSoup(html_text.text, 'lxml')
results = soup.find_all('div', class_= 'big-thumb')
# data = soup.find('div', {'class' : 'left-part'}).text
# category = data.find('a', class_= 'category_name')
big_data=[]
for result in results:
    data = {}
    title = result.find('h3', class_= 'main-title').text.strip()
    content = result.find('p', class_ = 'copy').text.strip()
    link = result.h3.a['href']
    category = result.div.a.text.strip()
    image = result.a.img['src']
    with open(title.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            # print('Writing: ', title)

    print(f'''
        Title: {title}
        Content: {content}
        Article Link: {link}
        Category: {category}
        Image Link: {image}
    ''')

    print(' ')

data['title'] = title
data['content'] = content
data['article_link'] = link
data['category'] = category
data['image_link'] = image

big_data.append(data)

# client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.scrape

for data in big_data:
    db.big_data.insert_one(data)








