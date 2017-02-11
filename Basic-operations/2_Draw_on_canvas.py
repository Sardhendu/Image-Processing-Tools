#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     06/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2

# We define a canvas, i.e instead of oading a picture from the desktop we would create one
# Hence we definr the cancas sixe on which we want to frame our picture

canvas=np.zeros((300,300,3), dtype='uint8')
# yeild a canvas sixe of 300*300 the 3 is given for RGB and uint8 is the data type

green=(0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
# we fill the canvas with green color from coordinate(0,0) to (300,300): The result will basically be a green diagonal (decreasing slope) line
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red=(0,0,255)
cv2.line(canvas, (300,0), (0,300), red)
# we fill the canvas with red color from coordinate(300,0) to (0,300): The result will basically be a red diagonal (increasing slope) line
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)



## On the same canvas we plot different shapes like circle, rectangle and square
# Plot a rectangle
blue=(255,0,0)
cv2.rectangle(canvas,(130,130), (180,180), blue, 5) # 5 is given for thickness, the thickness is measured in pixels
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# plot a circle outlined
white=(255,255,255)
(centerX,centerY)=(60,70)  # Define the center of the circle
radius=30
cv2.circle(canvas, (centerX, centerY), radius, white, 3)  # 3 is the thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# plot a circle filled
white=(100,100,20)
(centerX,centerY)=(250,200)  # Define the center of the circle
radius=30
cv2.circle(canvas, (centerX, centerY), radius, white, 3)  # 3 is the thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


## All the above are just the outline so how do we now fill the inner area of the rectangle
## We now seek help from numpy
## We would draw it in a new canvas

canvas=np.zeros((300,300,3), dtype="uint8")
(centerX, centerY)=(canvas.shape[1] /2, canvas.shape[0]/2)
# centerX and centerY are the center of the canvas (150,150)- canvas.shape[1] and canvas.chape[0] are bothe the size of xanvas i.e [300*300], therefore we divide them by 2
white=(255,255,255)

for i in xrange(0,150,20):
    cv2.circle(canvas, (centerX, centerY), i, white)
# The above for loop says that we loop over a number of radius starting from 0 and ending at 150 by incrementing 20 value at each step
# The first circle will be the inner most circle (a simple dot) with radius 0 ,
# the second would be the circle circummounting the dot with radius 20 and similarly the circle will keep on increasing until 150 is reached
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


## Draw a canvas with 25 random circles
for i in xrange(0, 25):  #  the code will loop 25 times, i.e creation of 25 random circles
   radius = np.random.randint(5, high = 200)
   # will generate a random radius between the range of 5 - 200
   color = np.random.randint(0, high = 256, size = (3,)).tolist()
   # will generate random colors, we know that the color needs three parameter RGB, therefore the size=(3,) is mentioned.
   # the np.random.randint will create 3 random integers between 0-256 and pass it to the color variable as list of those three integers by using the tolist() function
   pt = np.random.randint(0, high = 300, size = (2,))
   # Will randomly find the coordinate or the center of the circle between 0-300

   cv2.circle(canvas, tuple(pt), radius, color,-1)  #-1 is the thickness
   # Note:
   # If the thickness is -1 then the whole circle is filled with color, else if the thickness is any positive integer then the circle is only outlined with the respective thickness
   cv2.imshow("Canvas", canvas)
   cv2.waitKey(0)