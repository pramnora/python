'''
Code borrowed from:
https://www.youtube.com/shorts/ACuXn0EQfS0

Created: 17:24 08/07/2023
Updated: 17:24 08/07/2023
'''

links = [
  "www.askjeeves.com",
  "www.google.com",
  "www.yahoo.com",
  "www.wikipedia.org"
]

# -----------------------------------------------------------------------

# This doesn't work because it searches to find all w's/all .'s...and, removes them from the left...

print("\n1> lstrip('www.')\n")
for link in links:
	print(link.removeprefix("www."))

# -----------------------------------------------------------------------

# This is a similar code to the above...only, written more abbreviated...

print("\n2> lstrip('w.')\n")

for link in links:
	print(link.lstrip("w."))

# -----------------------------------------------------------------------

# This is the correct code...

print("\n3> removeprefix('www.')\n")

for link in links:
	print(link.removeprefix("www."))

# -----------------------------------------------------------------------

# This is an additional method...

print("\n4> link[4:]\n")

for link in links:
	print(link[4:])

# -----------------------------------------------------------------------

# This is an additional method...

print("\n5> link.replace('www.',"")\n")

for link in links:
	print(link.replace('www.',''))

# -----------------------------------------------------------------------

# This is an additional method...
# NOTE: Didn't work...?!

# print("\nX> link.replaceAll('www.',"")\n")

# for link in links:
#	print(link.replaceAll('www.',''))

# -----------------------------------------------------------------------

# This is an additional method...

print("\n6> {print([link.removeprefix('www.') for link in links])}\n")

{print([link.removeprefix("www.") for link in links])}

# -----------------------------------------------------------------------

# This is an additional method...

print("\n7> links=[link[4:] for link in links]\n")

links = [link[4:] for link in links]
print(links)

# -----------------------------------------------------------------------
