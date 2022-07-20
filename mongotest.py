import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@clustertad.bsan2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name": "praful",
    "email": "praful@gmail.com",
    "surname" : "hedaoo"
}

db1 = client ['mongotest']
coll = db1['test']
coll.insert_one(d)