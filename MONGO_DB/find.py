from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

db=client["Class"]
collection=db['Student']
value=collection.find_one({'Name':'Rohit'})
print(value)
allval=collection.find({'Name':'Rohit'})
for val in allval:
  print("Name is :",val['Name'],"\nAge is :",val['age'])