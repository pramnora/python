#!/usr/bin/python3

# ----------------------------------------------------------------------

# PROGRAM: Creates a very simple phonebook database;  
#          the database file is called: [pb1.db];  

# it adds 3 database fields: id,name,number  

# next, creates 2 separate records...
# ...with each record containing each of the 3 above fields
# ...having been filled in with data;  

# finally prints out all records/together with all fields. 

# ----------------------------------------------------------------------

# Create SQLite3 database...

import sqlite3
conn = sqlite3.connect('pb1.db') # open database

# Create a table.../also, add a number of fields...

conn.execute('''CREATE TABLE PHONEBOOK(
ID INT PRIMARY KEY NOT NULL,
NAME CHAR(50),
NUMBER CHAR(20));''')

# Insert data into each of the fields...

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (1,'Jack','0207 111 1111')");

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (2,'Jill','0208 222 2222')");  

conn.commit()

# Print database...including, all records/all fields...

cursor=conn.execute("SELECT ID, NAME, NUMBER FROM PHONEBOOK")
print("ID,NAME,NUMBER")
for row in cursor:
        print(f"{row[0]},{row[1]},{row[2]}")

conn.close() # close database

# ----------------------------------------------------------------------

# output...

# ID,NAME,NUMBER
# 1,Jack,0207 111 1111
# 2,Jill,0208 222 2222

