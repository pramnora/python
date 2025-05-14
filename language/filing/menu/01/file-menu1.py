# ----------------------------
#  PROGRAM: Filing...
# ----------------------------
# COMPUTER: Home based PC
#       OS: Linux Mint
#   EDITOR: Nano
# ----------------------------
#  CREATED: 140525 10:42 PM GMT
#  UPDATED: 140525 10:42 PM GMT
# ----------------------------

# -(NOTE: This is a menu driven program.)-

# ---------------------------------------------------
# BUGS FOUND LIST...
# 1. When the program is first run...; 
#    -(unless the file already exists inside of the current folder directory)-;
#    then, one needs to give it a file name to work with.
#    Creating the file name itself...does NOT create any file;
#    instead, all it does is to give the program 
#    a file name to be able to refer to/and, use, later on.
# 2. Also, after giving the program a file name;
#    one has to remember to write to that file, first...;
#    otherwise, the program will complain can't find file
#    to read/append to...?!    
# ---------------------------------------------------

# initialise variables...

# set file mode...

read="r" 
write="w" 
append="a"

# working variables...

file_name=""
each_line=""
new_line_char="\n"
yes_no=""

def get_file_name():
    global file_name
    print("Get file name...\n")
    while True:
        file_name=input("Enter filename: ")
        yes_no=input("Y/N?")   
        if yes_no.lower()=='y':
           break
        else:
           print()

def do_file_read():
    file_mode=read
    print(f"Reading from file: {file_name}...\n")
    with open(file_name,file_mode) as file_handle:
        any_text=file_handle.read()
        print(f"Here is the contents of file: {file_name}")
        print(any_text+new_line_char)
        input("Press any key to continue...")

def do_file_write():
    file_mode=write
    print(f"Writing to file: {file_name}...\n")
    with open(file_name,file_mode) as file_handle:
        print("Enter text to 'write' to file(type: '*' to quit): ") 
        while True:
            each_line=input()
            if each_line != '*':
                file_handle.write(each_line+new_line_char)
            else:
                break

def do_file_append():
    file_mode=append
    print(f"Appending to file: {file_name}...\n")
    with open(file_name,file_mode) as file_handle:
        print("Enter text to 'append' to file(type: '*' to quit): ") 
        while True:
            each_line=input()
            if each_line != '*':
                file_handle.write(each_line+new_line_char)
            else:
                break

def do_show_menu():
   print("Main menu")
   print("---------")
   print("1> Get file name")
   print("2> Read file")
   print("3> Write file")
   print("4> Append file")   
   print("--------------")
   print("Type: 'Q' to Quit!")
   
def perform_user_menu_selection():
    print("\nPlease, choose a number from main menu either: 1,2,3,4/or, type: 'Q' to quit")
    user_menu_selection=input("?")
    global done
    done=False
    if user_menu_selection=="1":
        get_file_name()
    if user_menu_selection=="2": 
        do_file_read()
    if user_menu_selection=="3":
        do_file_write()
    if user_menu_selection=="4":
        do_file_append()
    if user_menu_selection.lower()=="q":
            done=True
 
def main():
    while True:
        do_show_menu()
        perform_user_menu_selection()
        if done:
           break

if __name__ == '__main__':
   main()
