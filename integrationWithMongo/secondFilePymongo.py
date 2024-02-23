import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pedrotomasini1:8VLT0GKPoDsZBAIB@cluster0.vmfziwd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
posts = db.posts