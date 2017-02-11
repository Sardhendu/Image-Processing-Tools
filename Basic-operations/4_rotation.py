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
import cv2
import imutils

image=cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\sam.jpg")

cv2.imshow("original", image)
cv2.waitKey(0)

rotated= imutils.rotate(image, 45) # We pass only two arguments, because other two are default
cv2.imshow("The rotated image", rotated)
cv2.waitKey(0)

rotated_2=imutils.rotate(image, 90)
cv2.imshow("The rotated image with 90" , rotated_2)
cv2.waitKey(0)

