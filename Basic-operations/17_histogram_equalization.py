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

'''
1. Why do we need to perform histogram equalization?
Ans: For better contrast. The darker image get more darker and the lighter image gets more lighter

It is performed on GRAYSCALE image
It's very simple

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# load the image
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\green_beach.jpg")

# We resize
image=imutils.resize(image, height=500)         # Resizing
cv2.imshow("Original", image)
cv2.waitKey(0)

# convert into GRAYSCALE
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", image)
cv2.waitKey(0)

# perform equalization
eq= cv2.equalizeHist(image)

# Display image
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)

# Display both the images in one plot
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)

'''hstack is used to stack two or more arrays together
 Example a=[1,2,3], b=[3,4,5], np.hstack([a,b])= [1,2,3,3,4,5]
'''