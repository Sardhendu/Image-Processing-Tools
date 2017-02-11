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


# We would be taking a different picture to understand the pixel color [RGB] properly

import numpy as np
import cv2


image= cv2.imread("C:\Users\sardhendu_mishra\Desktop\StudyHard\Machine_learning\photus\wave.jpg")
cv2.imshow("Original_image", image)
cv2.waitKey(0)


## Split
# We can split an image into Blue, Green and Red
# The color that is very less in the given will result into a darket image
(B,G,R)= cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)


## Explanation
# The first image Red would be darker than Green and Blue because in the wave has no RED color in it
# The second image Green would be lighter than Red because a wave has shades of green.
# The third image Blue would be most lighter in color because a wave is blue


## merge
# When we combine these three images together we get our resultant image of wave
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()




######  Alternative method  to get the channels R,G,B ########

M= np.zeros(image.shape[:2], dtype="uint8")
red_channel=cv2.merge([M,M,R])
green_channel=cv2.merge([M,G,M])
blue_channel=cv2.merge([B,M,M])
cv2.imshow("Red", red_channel)
cv2.imshow("Green", green_channel)
cv2.imshow("Blue", blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()