import pymongo
# app = flask(__name__)
# mongo = pymongo(app)

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']

mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

# print(flask)
# mylist = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# melihat satu colom
find = mycol.find_one()
print(find)
# # melihat semua colom
# for x in mycol.find({}, {'address'}):
#     print(x)


print('batas antara ??')
for x in mycol.find():
    print(x)

# # sorting
# sname = mycol.find().sort('name', 1)
# for x in sname:
#     print(x)


