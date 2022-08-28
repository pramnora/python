# Make call to an external file: [myModules.py];
# in the case of name conflict/repetition...one can use the following syntax to distiguish between an internal/external file with the same function name: one()

from myModules import one as extOne

def one():
	print("Internal call/Function one")

one()    # calling an *internal* module function code
extOne() #calling an *external* module function code
