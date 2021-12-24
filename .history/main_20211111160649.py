import pymongo

if __name__ == "__main__":
    print("Connected to mongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['scrap']
    collection = db['hai']
    dictionary = {'name': 'Bhanu', 'marks': '99'}
    collection.insert_one(dictionary)