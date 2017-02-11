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

rectangle= np.zeros((300,300), dtype= "uint8") # We built a rectangle of the size
cv2.rectangle(rectangle, (50, 50), (250, 250), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle= np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150), 125, 255,  -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)


# After the above piece of code we get two image. A rectabgle and a circle
# We would use bitwise operators to combine those images

# Bitwise AND - the common area covered by both the image
bitwiseAnd= cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# Bitwise OR - the total area covered by both the image
bitwiseOr= cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# Bitwise XOR - The uncommon area by both the image
bitwiseXor= cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Bitwise NOT - The area where both the image are coinciding
bitwiseNot= cv2.bitwise_not(circle)      # Not will just flip the pixel, if 0 then 255 if 255 then 0
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)


'''  Now lets see how the whole bitwise stuff works
Since we are dealing with only black and white color combination, the pixel will have
a value of greater than 1 when encountered with white color, therefore a given pixel is
turned ON if the value of the pixel is greater than 0 and is turned off when the value of
pixel is 0
In short
for every white color we have input as 1 to the bitwise operators
for every black color we have input as 0 to the bitwise operators
then all is the game of 1 and 0's binary operation. The pixels of both the images are compared
'''
