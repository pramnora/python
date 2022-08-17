# -----------------------------------------------------------
#   PROGRAM: Look up chart...
#  LANGUAGE: Python 3.10.6
#  COMPUTER: Home base desktop PC/Windows 10 Pro
# -----------------------------------------------------------
#    AUTHOR: Mr. Paul Ramnora
#     EMAIL: pramnora@yahoo.com
# COPYRIGHT: (c)2020-, Mr. Paul Ramnora./All rights reserved.
# -----------------------------------------------------------
#   CREATED: Tue 160822 14:38 PM GMT
#   UPDATED: Wed 170822 02:33 AM GMT
# -----------------------------------------------------------

# Variable declarations...

# NOTE: NATO phonetic codes: a-z...look up chart drill.
#       Data is stored using all lower case...;
#       so, that the search can be 'case insensitive'.

NATOPhoneticCodes = {
     'a':'alpha',
     'b':'bravo',
     'c':'charlie',
     'd':'delta',
     'e':'echo',
     'f':'foxtrot',
     'g':'golf',
     'h':'hotel',
     'i':'india',
     'j':'julliet',
     'k':'kilo',
     'l':'lima',
     'm':'mike',
     'n':'november',
     'o':'oscar',
     'p':'papa',
     'q':'quebec',
     'r':'romeo',
     's':'sierra',
     't':'tango',
     'u':'uniform',
     'v':'victor',
     'w':'whisky',
     'x':'x-ray',
     'y':'yankee',
     'z':'zulu'
}

# Main program...

print("PROGRAM: NATOPhoneticCodes: a-z\n")

while(True):                        # while True...continue looping...
                                    # prompt user to enter their search term/
                                    # also, tell them how to make the program stop/
                                    # next, convert that search term into being all 'lower case'  
   doSearch = input("Enter a letter: (a-z)/(or, type in nothing to quit): ").lower()
   if (doSearch != ""):             # if search term doesn't equal nothing/
       if (doSearch in NATOPhoneticCodes):  # check if the search term exists as key inside of the database
          print(NATOPhoneticCodes[doSearch])# if search term match found/print out the NATO Phonetic code part
       else:                        # if search term does not exist as a key inside of the phonebook
          print("-Sorry, that search term NOT found!") # display search term NOT found message
   else:                            # else, if search term does equal nothing
      print("...done!")             # print out message to say the program is, now, done
      break                         # break out of while loop/stop program
      
