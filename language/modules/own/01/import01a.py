# Make calls to an external file: [myModules.py];
# so, that one can use modules written inside of that external file inside of this same file.

# NOTE: Using this syntax means...
#       one has to prefix the external module file name: myModules...;
#       before one can call the named function: myModules.two()/myModules.three()

import myModules

def one():
	print("Internal call/Function one")

one()             # calling an *internal* module function code
myModules.one()   # calling an *external* module function code
myModules.two()   # calling an *external* module function code
myModules.three() # calling an *external* module function code
