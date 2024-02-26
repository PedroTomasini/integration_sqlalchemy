import pprint

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pedrotomasini1:8VLT0GKPoDsZBAIB@cluster0.vmfziwd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "John"}))
print(posts.count_documents({"tags": "python"}))

pprint.pprint(posts.find_one({"author": "John"}))

print("\nRecuperando documentos na coleção posts de maneira ordenada por data.")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([("author", pymongo.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 1, 'name': 'John'},
    {'user_id': 2, 'name': 'Jane'},]

result = db.profile.insert_many(user_profile_user)
print("\nColeções armazenadas no MongoDB:")
collections = db.list_collection_names()
for collection in collections:
    print(collection)