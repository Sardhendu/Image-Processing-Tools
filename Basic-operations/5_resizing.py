#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     11/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import imutils
import cv2

image=cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\sam.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

# In order to resize we need to find the ratio of the current image and then resize them accordingly
# For exmaple if the ratio is 100 * 50 then resizeing the width (100) to 50 would resize length (50) to 25

resized=imutils.resize(image, height=500)  # Passing the new height of the image , the width is automatically calculated in resize method of the imutil package
cv2.imshow("resized image", resized)
cv2.waitKey(0)

resized_2=imutils.resize(image, width=200)  # Passing the new width of the image , the height is automatically calculated in resize method of the imutil package
cv2.imshow("resized image", resized_2)
cv2.waitKey(0)

resized_3 = imutils.resize(image, width=400, height=1000)
cv2.imshow("resized image", resized_3)
cv2.waitKey(0)
