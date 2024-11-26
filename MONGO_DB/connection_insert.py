from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")

db=client["Class"]
collection=db['Student']
data={'Name':'Rohit','age':21}
collection.insert_one(data)
insertValues=[
  {'name':'Romil','age':23},
  {'name':'Rushabh','age':21},
  {'name':'Baigan','age':20},
  {'name':'Atharva','age':10}
]
collection.insert_many(insertValues)