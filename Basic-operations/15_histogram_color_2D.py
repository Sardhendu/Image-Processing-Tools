#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     14/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2
import matplotlib as plt
import imutils
from matplotlib import pyplot as plt

# Here we shall plot a 2D histogram i.e how many count of pixel has two colors
# For example how many count of pixels have red 10 and blue 15 or how many pixels have red 30 and blue 40

## 1. At first we resize out image because our image is too large to view it completely
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\green_beach.jpg")
image=imutils.resize(image, height=500)         # Resizing
cv2.imshow("original", image)


## 2. Now we split the image into BGR and define colors
chan_image=cv2.split(image)
colors=("b","g","r")


## 3. Now we plot the 2D figure
fig=plt.figure()
ax=fig.add_subplot(131)
hist=cv2.calcHist([chan_image[1], chan_image[0]], [0,1], None, [32,32], [0,256, 0,256])
  # [chan_image[1], chan_image[0]] is taking two image , chan_image[1]->Green and chan_image[0]->blue
  # [0,1] . since we are using two channels we define them
  # None, because we do no masking
  # [32,32] we took bin size of [32,32] because if we take [256,256] it will be a 2D plot of 65536 seperate pixels count, which is redundant and wasteful of resource
  # [0,256, 0,256] is the range of green and blue channels
p= ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax=fig.add_subplot(132)
hist=cv2.calcHist([chan_image[1], chan_image[2]], [0,1], None, [32,32], [0,256, 0,256])
p= ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax=fig.add_subplot(133)
hist=cv2.calcHist([chan_image[0], chan_image[2]], [0,1], None, [32,32], [0,256, 0,256])
p= ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)


plt.show()




'''
Questions
1. why ax=fig.add_subplot(131)
ans: subplot is a plot inside a plot, fig.add_subplot(131) is actually equal to fig.add_subplot(1,3,1)
     It says that we would like to accomodate 3 subplots in one plot of which (131) is the first.
     similarly,
     If it was fig.add_subplot(132) then it would say that this subplot is the second subplot out of the 3 subplot we plan to accomodate in one plot
     similarly,
     If we have fig.add_subplot(111) then we say that we would like to have 1 plot, 1 subplot and this plot is the 1

2. why p= ax.imshow(hist, interpolation="nearest")
ans: There are different types of interpolation like None, none, nearest, gaussian, bilenear, hamming and many others
     The interpolation affects how the output is viewed
     Just try different interpolations and see how your 2D histogram varies

3. why plt.colorbar(p), what can you infer from it
Ans: Color bar is the long rectangular bar that shows shades of red when the pixel count is high and shades of blue when the pixel count is low
     For example when we plot the above graphs we see
     In the ist subplotn pixel count for green(32) and blue(30) is the highest (>9000). This shows the green pixels of the vegetation and trees and the blue of the sky and ocean
     similarly,
     In the 2nd subplot pixel count for green(26) and red(30) is the highest (>9000). This shows the green pixels of the vegetation and trees and the red of the dark edge of beach, the beach sand and others
     Similarly, the same approach can be taken for the 3rd subplot
'''
