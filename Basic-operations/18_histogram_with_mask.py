#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     14/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import cv2
from matplotlib import pyplot as plt
import histogram_with_mask
import imutils


## Create histogram without masking
# Load the image
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\green_beach.jpg")

# Resize the image
image=imutils.resize(image, height=500)
cv2.imshow("Original",image)
cv2.waitKey(0)

# Call the plot_histogram functiom of package histogram_with_mask
plot_histogram(image, "Histogram of original image")
plt.show()

cv2.destroyAllWindows()



## Create Histogram with masking
# For masking first we have to create a canvas of the same shape of that our image
mask=np.zeros(image.shape[:2], dtype="uint8")

# Now we need to create a rectangular or circular area to mask the image by providing the pixel area
cv2.rectangle(mask,(15,15), (130,100), 255,-1)  # 15 -130 pixels horizontally and 15-100 pixels vertically
cv2.imshow("Masked shape", mask)
cv2.waitKey(0)

# Now we vizualize the masked image
masked=cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the mask", masked)
cv2.waitKey(0)

# Now we call the plot_histogram functiom of package histogram_with_mask providing the masking area
plot_histogram(image, "Histogram for masked area", mask=mask)
plt.show()



''' Question
1. What do you infer from the masked histogram?
Ans: The masked part of the image is the blue sky, and if you see the histogram we
     notice that most of the red pixels falls in the range of (0-150) indicating very little contribution of red color in the masked image
     Whereas, the most of the blue pixels falls in the range (180-230) indicating larger contribution of blue color in the masked image
     which corroborates the fact that the sky is blue is color , hahaha

2. What is the importance of masking?
Ans: With masking we are able to achieve the histogram and study the impact of different channels in the masked are i.e the area of our interest.
     Studying the histogram of the complete image is paltry when we are interested in only a particular region.

'''