# import from opencv library...

import cv2 as cv

# -(NOTE: Here I went and created a sub-directory folder called: Photos;  
#       into which I 'copied and pasted' a single graphic [.jpg] file image.)-  

# set variables...

pathName = "photos/"
fileName = "01"
extensionName = ".jpg"
imageURL = pathName + fileName + extensionName # "photos/01.jpg"

# read image...

img = cv.imread(imageURL)

# set window title...

windowTitleText = "Photo"

# show image...

cv.imshow(windowTitleText,img)

# await user key press...

cv.waitKey(0)
