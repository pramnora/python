'''
 -----------------------------------------------------------
   PROGRAM: Look up chart...
  LANGUAGE: Python 3.10.6
  COMPUTER: Home based Desktop PC/Windows 10 Pro
 -----------------------------------------------------------
    AUTHOR: Mr. Paul Ramnora
     EMAIL: pramnora@yahoo.com
 COPYRIGHT: (c)2020-, Mr. Paul Ramnora./All rights reserved.
 -----------------------------------------------------------
   CREATED: Tue 160822 14:38 PM GMT
   UPDATED: Tue 160822 14:38 PM GMT
 ----------------------------------------------------------------------------------
 NOTES: This program is a 'blueprint' for a 'look up' type of chart/file...;
        my original idea was to create a phonebook 'look up' program,
        such where you type in the persons name/then, their phone number gets returned;
        but, the program can very easily be adapted to doing
        many other types of 'look up' operations, too.         
 ----------------------------------------------------------------------------------
'''

# Variable declarations...

# NOTE: Phonebook data is stored using all lower case...;
#       so that search can be 'case insensitive'.

phonebook = {
     'abe':'1111 111 1111',
     'brian':'2222 222 2222',
     'charlie':'3333 333 3333',
     'daisy':'4444 444 4444',
     'earl':'5555 555 5555',
     'fred':'6666 666 6666',
     'gillian':'7777 777 777'
    }

# Main program...

print("PROGRAM: Phonebook\n")

while (True):                       # while repeat equals, True...continue looping...
                                    # prompt user to enter their search term/
                                    # also, tell them how to make the program stop/
                                    # next, convert that search term into being all 'lower case'  
   doSearch = input("Enter what name phone number to find/(or, type in nothing to quit): ").lower()
   if (doSearch != ""):             # if search term doesn't equal nothing/
       if (doSearch in phonebook):  # check if the search term exists as key inside of the phonebook
          print(phonebook[doSearch])# if search term match found/print out the phone number part
       else:                        # if search term does not exist as a key inside of the phonebook
          print("-Sorry, that search term NOT found!") # display search term NOT found message
   else:                            # else, if search term does equal nothing
      print("...done!")             # print out message to say the program is, now, done
      break                         # break out of while loop; and,...


