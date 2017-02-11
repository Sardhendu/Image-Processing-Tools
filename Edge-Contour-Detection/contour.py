#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     18/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2
import math
import edge_detection


# Let us first plot a canvas of  5*5
canvas=np.zeros((30,50), dtype="uint8")
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

white=(255,255,255)
(centerX, centerY)=(15,15)    # This is read as width * height
radius=10
circled_canvas=cv2.circle(canvas, (centerX, centerY), radius, white, -1)
cv2.imshow("Circled canvas", canvas)
cv2.waitKey(0)

cv2.imwrite("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\image.jpg", canvas)

cv2.destroyAllWindows()


# We load the image and perform research
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

edge_detection.main_call(image)