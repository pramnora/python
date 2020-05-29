#----------------------------------------------------------
#*** PROGRAM: Phonebook - Version II
#   LANGUAGE: Python 3.8.2/(python.org)
#    COMPUTER: Home based PC/OS: Windows 10 Professional
#----------------------------------------------------------
#   AUTHOR: Mr. Paul Ramnora
#    EMAIL: pramnora@yahoo.com
#  COPYRIGHT: 2020-, Mr. Paul Ramnora./All rights reserved. 
#----------------------------------------------------------
#    CREATED: 270520 23:30 PM GMT
#    UPDATED: 280520 10:25 AM GMT
#----------------------------------------------------------

#*** LIST OF WHAT'S WORKING:
#   - both full and partial searches (eg. a,ab,abe)
#   - using either: lower/upper/mixed cased searching (eg. abc/ABC/aBc/Abc)

#*** LIST OF POSSIBLE FUTURE UPDATES:
#   - searches through 'name' field, only; NOT both 'name/number' fields.
#   but, what if...you've completely forgotten the name;
#   and, can only remember the number/or, part of the number.

#*** LIST OF BUG/S FOUND:
#   - The output shows 'phone numbers'; but, with no accompanying name?!
#   This is especially a problem when there are multiple entries having been found;
#   how to clearly distinguish between one entry and the next...?!

#*** SPECIAL NOTE/S:
#   - Each key has to be entirely 'unique', and, thefore, individual;
#   which means if a particular data entry contains 'multiple' phone numbers;
#   then, you would enter that key as: entry-name-1,entry-name-2;
#   because entering it as the same: entry-name,entry-name...;
#   then, only 'one' entry would show up/but,NOT the other one;
#   in other words, the previous entry has been over-written...; and, therefore, is 'ignored'!

#---------------------------------------------------------------------------------------------

#----------------------------
#*** variable declarations...
#----------------------------

phonebook = {
    "Samaritans(1)":"08457 90 90 90",
    "Samaritans(2)":"116 123",
    "Cashplus":"0330 024 0924",   
    "Nat West":"0800 200 400",
    "Emergency":"999",
    "NHS":"111",
}

#-------------------
#*** main program...
#-------------------

print("Phonebook")
while True:
    found_flag = False
    search_term = input("(type nothing to end)/search: ")
    if search_term == "":
        print("-Finish!")
        break
    else:
        for each_name in phonebook: 
            if search_term.upper() in each_name.upper():
                print(phonebook[each_name])
                found_flag = True
        if found_flag == False:
            print("-Sorry, search term NOT found!")

