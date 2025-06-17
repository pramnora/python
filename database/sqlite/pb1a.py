!/usr/bin/python3

# Program creates a very simple phonebook database...;
# adds 3 database fields: id,name,number
# next adds 2 separate records...each record containing the 3 fields
# finally prints out all records/together with all fields

import sqlite3
conn = sqlite3.connect('pb1.db') 

conn.execute('''CREATE TABLE PHONEBOOK(
ID INT PRIMARY KEY NOT NULL,
NAME CHAR(50),
NUMBER CHAR(20));''')

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (1,'Jack','0208 111 1111')");  
conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (2,'Jill','0207 222 2222')");  
conn.commit()

cursor=conn.execute("SELECT ID, NAME, NUMBER FROM PHONEBOOK")
print("ID,NAME,NUMBER")
for row in cursor:
        print(f"{row[0]},{row[1]},{row[2]}")

conn.close()


