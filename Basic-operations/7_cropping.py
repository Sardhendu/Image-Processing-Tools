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

# Cropping is very simple, we wont use define the cropping method in imutil package, but we would directly crop the particulat pixel box

# Cropping is the same as displaying few pixels

image=cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\sam.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

cropped= image[50:640, 100:630]  # basically we display the pixel in that particulae area
# nuply array takes array input as (height * width)
cv2.imshow("cropped image", cropped)
cv2.waitKey(0)

