# fill list n with numbers 1 up to 10...
n=[n for n in range(1,11)]

# fill list n_squared with each of the n list numbers having been squared...
n_squared=list(map(lambda x:x**x,n))

# print list n...
print(n)

# print list n_squared...
print(n_squared)