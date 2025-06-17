#!/usr/bin/python3

# The line above indicates where inside the Linux OS/Operating System
# the 'python3' program can be found...it is needed to run this script;
# by using the following instructions which are typed in after the dollar prompt:($)

# $ chmod +x pb2a.py                       # grant file executable permission
# $ ./pb2a.py                              # run file/execute code

# -------------------------------------------
#     PROGRAM: Phonebook database
#     VERSION: 0.01

#    LANGUAGE: Python3
#    DATABASE; SQLite3

#   COMPUTER: Home-based PC
#         OS: Linux Mint   

#      AUTHOR: Mr. Paul Ramnora
#       EMAIL: pramnora@yahoo.com
#   COPYRIGHT: (c)Mr. Paul Ramnora, 2025-
#              /All rights reserved.
   
#    CREATED: Sat 14th June 2025 10:28 PM GMT
#    UPDATED: Sun 15th June 2025 13:06 PM GMT
# -------------------------------------------

# ------------------------
# declare global variables
# ------------------------

dbName="pb1.db"
conn=""

screen_width_length=80
underlineChar="-"

# -----------------
# declare functions
# -----------------

def do_underline():
	print(screen_width_length * underlineChar)

# ---------------
# Main program...
# ---------------

# create_database():

print(f"1. Creating database: [{dbName}] - ",end="")

import sqlite3
conn = sqlite3.connect(dbName) # open database connection

print("database successfully created.")

# create_fields():

print("2. Adding database fields - ",end="")

conn.execute('''
		CREATE TABLE PHONEBOOK
		(
			ID 	INT 	PRIMARY KEY 	NOT NULL,
			NAME 	CHAR(50),
			AGE 	INT,
			COUNTRY CHAR(20),
			PREFIX	 CHAR(3),
			NUMBER CHAR(20)
		);
	''')

print("ALL fields successfully created.")

# insert_data_into_fields():

print("3. Inserting fields data - ",end="")

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, AGE, COUNTRY, PREFIX, NUMBER) \
VALUES (1,'Fred',25,'UK','+44','(0207) 111 1111')");  

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, AGE, COUNTRY, PREFIX, NUMBER) \
VALUES (2,'Grant',17,'US','+1','(111) 222-3333')");  

conn.execute("INSERT INTO PHONEBOOK (ID, NAME, AGE, COUNTRY, PREFIX, NUMBER) \
VALUES (3,'Li',54,'CN','+86','(111) 1234 5678')");  

conn.commit()

print("ALL insertions successful.")

# display_all_data_fields():

print("4. Displaying ALL database entries -\n")
cursor=conn.execute("SELECT ID, NAME, AGE, COUNTRY, PREFIX, NUMBER FROM PHONEBOOK")
for row in cursor:
	print("ID = ",row[0])
	print("NAME = ",row[1])
	print("AGE = ",row[2])
	print("COUNTRY = ",row[3])
	print("PREFIX = ",row[4])
	print("NUMBER = ",row[5])
	print()
print("...operation successful.") 

# close_database():
conn.close() # close database connection
