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

''' Translation is shifting an image'''

import cv2
import numpy as np
import imutils


# Display the picture
image = cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\red.jpg")
cv2.imshow("original",image)
cv2.waitKey(0)

# Making call to imutil package
shifted= imutils.translate(image,25,50)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

shifted2= imutils.translate(image, -25, -100)
cv2.imshow("Shifted up and left", shifted2)
cv2.waitKey(0)



