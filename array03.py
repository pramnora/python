How to use python string arrays with functions...

#assign values to the array...
items=["eggs","tomatoes","bannanas","apples"]

#print out array values...
print(items)
#eggs,tomatoes,bannanas,apples

#select a specific array item with the array index number...
items[1]
#tomatoes

#re-assign a different value to an array item...
items[1]="bread"

#print out array values...
print(items)
#eggs,bread,bannanas,apples

#delete an array item... 
del items[3]

#print out array values...
print(items)
#eggs,bread,bannanas

#print out array items length...
len(items)
#3

#add an item to tha array...
items.append("oranges")

#print out array values...
print(items)
#eggs,bread,bannanas,oranges


