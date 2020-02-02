from pymongo import MongoClient
# Prettify the response
from pprint import pprint

client = MongoClient('localhost:27017')
db_admin=client.admin

serverStatusResult = db_admin.command("serverStatus")
pprint(serverStatusResult)

# Set the db object to point to the business database
db=client.business
employee = db.employees.find_one({})
print('Employee document')
pprint(employee)