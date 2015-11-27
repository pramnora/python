How to use python string arrays with functions...

items=["eggs","tomatoes","bannanas","apples"]
print(items)
#eggs,tomatoes,bannanas,apples

items[1]
#tomatoes

items[1]="bread"
print(items)
#eggs,bread,bannanas,apples

del items[3]
print(items)
#eggs,bread,bannanas

len(items)
#3

items.append("oranges")
print(items)
#eggs,bread,bannanas,oranges


