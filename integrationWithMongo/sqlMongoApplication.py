import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pedrotomasini1:8VLT0GKPoDsZBAIB@cluster0.vmfziwd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
collection = db.test_collection
print(db.list_collection)

# Definiçaão de infos para compor o doc.
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now()
}

# Preparando para submeter as infos.
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

#print(db.posts.find_one())
pprint.pprint(db.posts.find_one())

# Bulk inserts
new_posts = [{
    "author": "John",
    "text": "Another post!",
    "tags": ["bulk", "insert"],
    "date": datetime.datetime.now()},
    {
    "author": "Eliot",
    "title": "MongoDB is fun",
    "text": "and pretty easy too!",
    "date": datetime.datetime(2009, 11, 12, 11, 44)}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
print("\nrecuperação final")
pprint.pprint(db.posts.find_one({"author": "Eliot"}))

print("\nDocumentos presentes na coleção posts")
for posts in posts.find():
    pprint.pprint(posts)