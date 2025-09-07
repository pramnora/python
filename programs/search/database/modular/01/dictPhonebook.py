# NOTE: Search is 'case sensitive'...;
#       so, Cashplus, cashplus, CASHPLUS
#       only the first search will be found;
#       the other 2 search results in data item not found.
import data
print("Database: Phonebook")
print("-------------------")
while True:
    name=input("Enter a name(or, empty string to Quit): ")
    if name != "":
       if name in data.phonebook:
          print(data.phonebook[name])
       else:
          print("-Sorry, data entry NOT found! Please, try again...")
    else:
       print("-Finished!")
       break
