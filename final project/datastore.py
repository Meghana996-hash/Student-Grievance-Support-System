import pymongo
# Connecting to Mongo
conn = pymongo.MongoClient()
# Get the database
db = conn['login']
# Get Collection
users = db['users']
grs = db['grs']
from bson.objectid import ObjectId

import datetime


# Create
def add_user(name, username, password):
	record = {'username' : username, 
			'name' : name, 
			'password' : password,
			'login_count' : 0 }
	return users.insert_one(record)

# Retrieve
def get_user(username, password):
	record = {'username' : username, 
			'password': password}
	
	rec = users.find_one(record)
	return rec

def get_users():
	records = []
	for rec in users.find():
		records.append(rec)

	return records


#upload

def add_griv(name, username, comment):
    record = {'name' : name,
	      'username' : username,
             'comment' : comment,
              'time' : datetime.datetime.now() ,
             'upvote' : 0}
    return grs.insert_one(record)

    


def get_griv(id):
    record = {'_id' : ObjectId(id)}
    
    return grs.find_one(record)

def get_grs():
    records=[]
    for rec in grs.find():
        records.append(rec)
    print(records)
    return records


def update_upvote(griv):
	upvote_count = griv['upvote']
	grs.update(griv, {'$set' : {'upvote' : upvote_count + 1}})




