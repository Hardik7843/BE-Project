"""
This python script is for connecting the MySQL database to
Python
"""

import mysql.connector

# host = "127.0.0.1"
port = "3306"
user_name = "root"
pwd = "root"
dbname = "park"
mydb = mysql.connector.connect(
  user = user_name,
  password=pwd
)

print(f"Database connected: {mydb.is_connected()}")



# Cursor is needed to make changes and fetch the data
cursorObject = mydb.cursor(
    buffered = True
)
  

# This is how queries works in SQL connector  
# query = "Select * from sys.slots;"
# cursorObject.execute(query)

a9 = 0
flag9 = 1
print( f"a9 equals flag9: {a9 == flag9}" )
if(a9 != flag9):
    if(a9 == 0):
        j = int(9)
        query = "UPDATE sys.slots SET avl= 'y' where slot_id = 9 "
        cursorObject.execute(query)
        print("a9 = 0")
        # display = "select * from sys.slots where slot_id = 9"
        # cursorObject.execute(display)
    else:
        j1 = int(9)
        # query1 = f"UPDATE sys.slots SET avl= 'y' where slot_id = {j1};"
        query1 = "UPDATE sys.slots SET avl = 'n' where slot_id = 9 "
        cursorObject.execute(query1)
        print("a9 = 1")
        # display = "select * from sys.slots where slot_id = 9"
        # cursorObject.execute(display)
    flag9 = a9

# query = " UPDATE sys.slots SET avl = 'y' where slot_id = 9; "
# cursorObject.execute(query)

# Just printing the result
# myresult = cursorObject.fetchall()
# # print(myresult)
# for x in myresult:
#     print(x)


# Closing the database connection
mydb.close()
print(f"Database connected: {mydb.is_connected()}")