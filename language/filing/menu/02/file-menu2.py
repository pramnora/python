# ----------------------------------
#  CREATED: 150626 15:54 PM GMT
#  UPDATED: 150626 15:54 PM GMT
# ----------------------------------
#  PROGRAM: File handling
# LANGUAGE: Python 3.12.3
#       OS: Linux Mint 22.3
# COMPUTER: (home based) Nuc MiniPC/
#           8GB RAM/120 SSD  
#   EDITOR: Nano
# ----------------------------------
#   AUTHOR: Mr. Paul Ramnora
# LOCATION: London, UK
#    EMAIL: pramnora@yahoo.com
# ----------------------------------

# COMMENTS: 

# This is a very simple File handling program...;
# which aims to manipulate just a single data file called: 'data.txt'.

# It is a menu driven program...

# - display a main menu showing options for end user to select from
# - allow users to select from the menu options by typing in either a number(1,2,3)/letter(Q/q)
# - carry out the user selected option: view/write/append/quit

# ------------------------
# Variable declarations...
# ------------------------

fileName="data.txt"
underlineChar="-"
choice=""

# ------------------------
# Function declarations...
# ------------------------

def printMenuOptionsText():
    print()
    print(f"Filename: [{fileName}]")
    printUnderline()
    print("Main Menu:-")
    print()
    print("1. Show file")
    print("2. Write to file/(over-write)")
    print("3. Append to file/(add)")
    print()
    print("Type: 'Q' to Quit")
    printUnderline()

def printUnderline():
   print(underlineChar*80)

def fileOpenReadShow():
    file=open(fileName,"r")
    content=file.read()
    print(content)
    file.close()

def printContinueMessage():
    print()
    x=input("Press [SPACEBAR] to continue...")
    print()

def fileWrite():
    file=open(fileName,"w")
    content=""
    while(content != "EOF"):
        content=input("(Enter 'EOF' to stop.) File content: ")
        if content != "EOF":
           content+="\n"
           file.write(content)
    file.close()

def fileAppend():
    file=open(fileName,"a")
    content=""
    while(content != "EOF"):
        content=input("(Enter 'EOF' to stop.) File content: ")
        if content != "EOF":
           content+="\n"
           file.write(content)
    file.close()

# ---------------
# Main program...
# ---------------

while(choice != "Q" and choice != "q"):

   printMenuOptionsText()

   choice=input("Enter menu option choice number: '1','2','3'/or, 'Q': ")
   print(choice)
   printUnderline()

   if choice=="1":
      fileOpenReadShow()
      printContinueMessage()
   elif choice=="2":
      fileWrite()
   elif choice=="3":
      fileAppend()
   elif choice in ("Qq"):
      print("-Finished!")

