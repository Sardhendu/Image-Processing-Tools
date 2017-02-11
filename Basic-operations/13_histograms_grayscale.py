#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     13/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2
import matplotlib as plt
import imutils
from matplotlib import pyplot as plt

''' A histogram is plotted using matplotlib and the histogram cal function takes inputs, the image, channel, mask, bin number and range
   # cv2.calcHist(images,channels,mask,histSize,ranges)
'''

## Let us first plot a GRAYSCALE histogram
# At first we resize out image because our image is too large to view it completely
image=cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\sam.jpg")
image=imutils.resize(image, height=500)         # Resizing
# Now we convert the image into grayscale
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # Grayscale image
cv2.imshow("original", image)
hist=cv2.calcHist([image], [0], None, [256], [0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# The histogram depicted shows how many times a particular bin has occured.
# In layman terms for a GRAY color the picture is mostly a transition of black and white
# so the histogram shows the number of pixels in each bin, here bin is indicated by 0,1,2,3.....255
# with 255 being the lightest color (white) and 0 being the darkest color (black)



# You must be wonderig why did we write the image as [image] in the calcHist function
# Its just because to make the graph smoother. Just remove square brackets and compare the graphs, you'll find the difference
