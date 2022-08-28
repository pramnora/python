# Make calls to an external file: [myModules.py];
# so, that one can use a single 'specific' named module which is written inside of that external file...inside of this same file.

# NOTE: Using this syntax means...
#       one can shorten the long name: myModules...to become, instead, quite simply: mm
#       one needs to prefix the external module file name(in this case shortened): mm...;
#       before one can call the named external function to use it: mm.two()/mm.three()

from myModules import two

def one():
	print("Function one")

one()      # calling an *internal* module function code
mm.two()   # calling an *external* module function code
mm.three() # calling an *external* module function code/this call will bug out...as function three hasn't been declared...?!
