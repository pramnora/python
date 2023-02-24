import os      # import the os library module

print(os)      # result: <module 'os' (frozen)>
print(os.name) # result: nt 
print(os.path) # result: <module 'ntpath' (frozen)>

# variable stores the current working directory...
current_working_dir = os.getcwd()

# this line lists where is the current directory/(full path)...
print(os.getcwd())

# lists all folders/files inside of the current folder directory...
for eachEntry in os.listdir(current_working_dir):
    print(eachEntry)
