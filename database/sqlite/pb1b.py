#!/usr/bin/python3

# PROGRAM: Phonebook (id,name,number)
# LANGUAGE: PYTHON3
# DATABASE: SQLite3

import sqlite3                  
conn = sqlite3.connect('pb1.db') 

conn.execute('''CREATE TABLE PHONEBOOK(
ID INT PRIMARY KEY NOT NULL,
NAME CHAR(50),
NUMBER CHAR(20));''')

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (1,'Jack','0207 111 1111')");
conn.execute("INSERT INTO PHONEBOOK (ID, NAME, NUMBER) \
VALUES (2,'Jill','0208 222 2222')");  
conn.commit()

cursor=conn.execute("SELECT ID, NAME, NUMBER FROM PHONEBOOK") 
print("ID,NAME,NUMBER") 
for row in cursor:      
        print(f"{row[0]},{row[1]},{row[2]}")

conn.close() # close database
