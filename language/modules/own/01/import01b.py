# Make calls to an external file: [myModules.py];
# so, that one can use modules written inside of that external file inside of this same file.

# NOTE: Using this syntax means...
#       one can shorten the long name: myModules...to become, instead, quite simply: mm
#       one needs to prefix the external module file name(in this case shortened): mm...;
#       before one can call the named external function to use it: mm.two()/mm.three()

import myModules as mm

def one():
	print("Internal call/Function one")

one()      # calling an *internal* module function code
mm.one()   # calling an *external* module function code
mm.two()   # calling an *external* module function code
mm.three() # calling an *external* module function code
