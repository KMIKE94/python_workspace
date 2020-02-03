from pymongo import MongoClient
# Prettify the response
from pprint import pprint

username = 'user'
password = 'password'
client = MongoClient('mongodb://%s:%s@localhost:27017' % (username, password))

# Set the db object to point to the business database
db=client.get_database("mymongodb")
col = db.get_collection('employees')
employee = col.find_one({})
print('Employee document')
pprint(employee)