'''
This code borrowed from YouTube...
https://www.youtube.com/shorts/QdMzVy2GiKc

Created: 03:04 19/07/2023
Updated: 03:05 19/07/2023
'''

names = [
    "Charles",
    "David",
    "Paul"   
]

# dict comprehension...

length = {name:len(name) for name in names}

print(length)

# output...
# {'Charles': 7, 'David': 5, 'Paul', 4}
