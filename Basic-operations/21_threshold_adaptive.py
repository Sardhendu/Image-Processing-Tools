#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     15/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
Intuition:
    In manual threshold we manually provide the threshold value, but in real world situation
    finding the threshold value manually is very difficult, tedious and time consuming, though the output
    can be convincing. Therefore to avoid such situations we leverage the adaptive threshold methos.

    The adaptive threshold concept works on the blurring concept of average and gaussian.
    In this we provide the pixel size and the algorithm calculates the average of the neighbours,
    this average is considered as the threshold point and any neighbour whose intensity is less than the threshold
    it's value is set to 0 and any neighbour whose intensity is greater than the threshold point is set to 255
'''

# Lets do some coding

import numpy as np
import cv2

# load the image
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\coins.png")
original_image=image
cv2.imshow("original", image)
cv2.waitKey(0)

# Convert the image into GRAYSCALE
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GREY image", image)
cv2.waitKey(0)

# perform blurring for 5*5 pixel size
blurred_image=cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred_image", blurred_image)
cv2.waitKey(0)

cv2.destroyAllWindows()


## Mean adaptive thresholding
# Perform mean adaptive thresholding (Average or mean type) for 11*11 pixels
thresh=cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,4)
cv2.imshow("Mean adaptive thresholding", thresh)
cv2.waitKey(0)

# Now we perform masking for Mean adaptive thresholding on GRAYSCALE image
masked_image=cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow("Masking on GRAYSCALE", masked_image)
cv2.waitKey(0)

# Now we perform masking for Mean adaptive thresholding on original image
masked_image=cv2.bitwise_and(original_image, original_image, mask=thresh)
cv2.imshow("Masking on Original image", masked_image)
cv2.waitKey(0)


## Gaussian adaptive thresholding
# Perform gaussian adaptive thresholding (Gaussian type) fro 11*11 pixels
thresh=cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian adaptive thresholding", thresh)
cv2.waitKey(0)

# Now we perform masking for Gaussian adaptive thresholding on GRAYSCALE image
masked_image=cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow("Masking on GRAYSCALE", masked_image)
cv2.waitKey(0)

# Now we perform masking for gaussian adaptive thresholding on original image
masked_image=cv2.bitwise_and(original_image, original_image, mask=thresh)
cv2.imshow("Masking on Original image", masked_image)
cv2.waitKey(0)



'''
You will be surprised to see that the output is not that convincing, nevertheless
the adaptive thresholding menthod comes in handy while edge detection.
'''