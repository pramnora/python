#How to use dictionaries in Python...

#NOTE: Dictionaries create an 'unordered' list...; 
#therefore, printing out the full dictionary may print out a different order each time

#creating dictionaries; and, assigning key/value pairs to each dictionary item...
persons={"Tom":1,"Dick":2,"Harry":3}

#printing out all dictionary keys...
print(persons.keys())
#Tom, Dick, Harry

#printing out all dictionary values...
print(persons.values())
#1,2,3

#printing out the dictionary length...
len(persons)
#3

#printing out a selected key/value pair item inside of the dictionary...
print(persons["Tom"])
#1

#re-assigning a key/value pair...
persons["Dick"] = 4

#printing out all dictionary keys/values...
print(persons)
#Tom:1, Dick:4, Harry:3

#how to delete a dictionary key/value pair item... 
del persons["Dick"]

#printing out all dictionary keys/values...
print(persons)
#Tom:1,Harry:3

#creating a new dictionary with key/value pairs...
persons2={"Jack":2,"Jill",4)

#joining together two dictionaries...
persons.update(persons2)

#printing out all dictionary keys/values...
print(persons)
#Tom:1,Harry:3,Jack:2,Jill:4

#clearing all values inside of the dictionary by wiping them out...
persons.clear()

#printing out all dictionary keys/values...
print(persons)
#{} ...returns an empty dictionary

#deleting the dictionary entirely altogether...
del persons

#printing out all dictionary keys/values...
print(persons)
#returns an error message: 'persons not defined'


