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
#   UPDATED: Wed 170822 02:19 AM GMT
# -----------------------------------------------------------

# Variable declarations...

# NOTE: French numbers 1 to 20...look up chart drill.
#       Data is stored using all lower case...;
#       so, that the search can be 'case insensitive'.

frenchNos1To20 = {
     'one':'un',
     'two':'deux',
     'three':'trois',
     'four':'quatre',
     'five':'cinq',
     'six':'six',
     'seven':'sept',
     'eight':'huit',
     'nine':'neuf',
     'ten':'dix',
     'eleven':'onze',     
     'twelve':'douze',     
     'thirteen':'threze',     
     'fourteen':'quartorze',     
     'fifteen':'quinze',     
     'sixteen':'seize',     
     'seventeen':'dix-sept',     
     'eighteen':'dix-huit',     
     'nineteen':'dix-neuf',     
     'twenty':'vingt'     
}

# Main program...

print("PROGRAM: French numbers 1 to 20\n")

while(True):                        # while True...continue looping...
                                    # prompt user to enter their search term/
                                    # also, tell them how to make the program stop/
                                    # next, convert that search term into being all 'lower case'  
   doSearch = input("Enter a number as an english word: (one/two/-etc.)/(or, type in nothing to quit): ").lower()
   if (doSearch != ""):             # if search term doesn't equal nothing/
       if (doSearch in frenchNos1To20):  # check if the search term exists as key inside of the phonebook
          print(frenchNos1To20[doSearch])# if search term match found/print out the phone number part
       else:                        # if search term does not exist as a key inside of the phonebook
          print("-Sorry, that search term NOT found!") # display search term NOT found message
   else:                            # else, if search term does equal nothing
      print("...done!")             # print out message to say the program is, now, done
      break                         # break out of while loop/stop program.


