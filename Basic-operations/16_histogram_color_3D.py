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


## 1. At first we resize out image because our image is too large to view it completely
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\green_beach.jpg")
image=imutils.resize(image, height=500)         # Resizing
cv2.imshow("original", image)

## 2. Now we split the image into BGR and define colors
chan_image=cv2.split(image)
colors=("b","g","r")

## 3. Now we plot the 2D figure
plt.figure()
hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print "3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0])
plt.plot(hist)
plt.show()
cv2.waitKey()