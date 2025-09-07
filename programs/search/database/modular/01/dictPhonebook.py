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
