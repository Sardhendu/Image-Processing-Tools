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

# Fipping is too easy, therefore it is not worth writing the fucntion for flipping in imutil

# Flipping horizontally around y-axis
flipped=cv2.flip(image,1)
cv2.imshow("flipped_image", flipped)
cv2.waitKey(0)

# Flipping vertically around x-axis
flipped_2=cv2.flip(image,0)
cv2.imshow("flipped_image", flipped_2)
cv2.waitKey(0)

# Flipping vertically-horizontally
flipped_3=cv2.flip(image,-1)
cv2.imshow("flipped_image", flipped_3)
cv2.waitKey(0)