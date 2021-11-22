# CREATED: 221121 23:11 PM GMT
# UPDATED: 221121 23:11 PM GMT

# NOTE: This code was, originally, borrowed from...
# https://www.skillshare.com/classes/Learn-Python/488262944/projects
# ...then, was further adapted and developed by me.

#-----------------------------------------------------------
import webbrowser

#--- Example 1: Using a string literal as the URL to open...

webbrowser.open("https://www.instagram.com")

#-----------------------------------------------------------

#--- Example 2: Using a string variable as the URL to open...

URL = "https://www.facebook.com"
webbrowser.open(URL)

#-----------------------------------------------------------

#--- Example 3: Using an array...to store multiple different URL string values...

araListOfMultipleURLs = ["redbubble","deviantart","imagekind"]

#--- the for loop is used to cycle through each separate array item value... 

for eachURL in araListOfMultipleURLs:
	webbrowser.open("https://www." + eachURL + ".com")

#-----------------------------------------------------------

