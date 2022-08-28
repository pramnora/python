import myModules

def one():
	print("Function one")

one()         # calling an *internal* module function code
myModules.two()   # calling an *external* module function code
myModules.three() # calling an *external* module function code
