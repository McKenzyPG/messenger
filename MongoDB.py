import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["userDB"]

collist = mydb.collection_names()
if "userDB" in collist:
  print("The collection exists.")

# create dictionary
user_record = {}
 
# set flag variable
flag = True
 
# loop for data input
while (flag):
   # ask for input
   user_name,user_pass = input("Enter username name and password: ").split(',')
   # place values in dictionary
   user_record = {'name':user_name,'pass':user_pass}
   # insert the record
   mycol.insert(user_record)
   # should we continue?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False
 
# find all documents
results = mycol.find()
 
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
 
# display documents from collection
for record in results:
# print out the document
print(record['name'] + ',',record['pass'])
 
print()
 
# close the connection to MongoDB
connection.close()