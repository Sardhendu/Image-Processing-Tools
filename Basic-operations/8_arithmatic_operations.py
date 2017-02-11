#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     12/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import numpy as np
import cv2


image= cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\sam.jpg")
cv2.imshow("original", image)
cv2.waitKey(0);


'''
For arithmatic operations like addition and sibstraction, both numpy and openCV behave differently
As because the addition od pixels for RGB should lie under the range (0-255), numy and openCV have their own approach to handle such situations
if the user does an addition that results in more than 255

1. OpenCV would round the addition value value to 255 when the result of addition is more that 255 and similarly round the value to 0 when the substraction result value less than 0
2. Numpy however, doesn't round the value but provides a wrap value.
   The numpy counts the value till 255 and outputs the result value
   For example 200+100 = 44 (300-255) and 2000+100=52  (2100- (2100*256)) 256 because the range is 0-255
   For exmpale 50-100  = 206 (256-50) and 1000-100=132 ( 900 (1000-100) -  768 (256*3 )) )
'''

# 1. For openCV the 8-bit unsigned integer should have a value within range 0-255
print "max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))
print "min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100])))

# 2. For numpy also the 8-bit unsigned integer should have a value within 0-255
print "wrap around: " + str(np.uint8([200]) + np.uint8([100]))
print "wrap around: " + str(np.uint8([50]) - np.uint8([100]))





''' Now Let us Perform arithmatic operations on the image. '''

# In order to add a certain number to the image's pixels, first we have to create a array of that number of the same size as our image
M= np.ones(image.shape, dtype="uint8") * 100 # it is creating an array of 1 similar to that of the image's array size and multiply 100 to each 1's. Basically we create an array of 100's
added=cv2.add(image, M)
cv2.imshow("Added_image", added)  # ADDITION WOULD BRING EACH PIXEL VALUE CLOSER TO 255 AND HENCE OUR IMAGE WOULD APPEAR BRIGHTER
cv2.waitKey(0)

# Similarly we subtract
M=np.ones (image.shape, dtype="uint8") *50
subtracted= cv2.subtract(image, M)
cv2.imshow("Subtracted_image", subtracted) # SUBTRACTION WOULD BRING EACH PIXEL VALUE CLOSER TO 0 AND HENCE OUR IMAGE WOULD APPEAR DARKER
cv2.waitKey(0)