from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client['ecommerce']
connection=db['orders']

# docs=[
#   {
#   'name':'rohit',
#   'age':20,
#   'salary':200
#   },{
#     'name':'ramesh',
#   'age':20,
#   'salary':500
#   },{
#     'name':'ram',
#   'age':20,
#   'salary':600
#   }
# ]
# connection.insert_many(docs)
doc=connection.find()
for d in doc:
  if(d['salary']>200):
    print(d)