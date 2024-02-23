import pprint

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