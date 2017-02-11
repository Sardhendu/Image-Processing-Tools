#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     16/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


''' Topics Covered
1. Laplacian Edge Detection
2. Sobel Edge Detection
3. Canny Edge Detection

Thought:
    Edge detection like thresholding is also a sort of binarization of an image,
    Converting the image into white and black (0 or 255).
'''

import numpy as np
import cv2

# load the image
image= cv2.imread("/Users/sam/All-Program/App-DataSet/Image-Processing/tiger.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

# convert the image into GRAYSCALE
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY color Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


## Laplacian Edge Detection'''
# Now we detect the gradient and perform the laplacian edge detection
lap=cv2.Laplacian(image, cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("Laplacian edge detection", lap)
cv2.waitKey(0)
cv2.destroyAllWindows()




## Sobel Edge Detection
# Now we shall use Sobel operator top determine the horizontal and vertical edges
sobelX= cv2.Sobel(image, cv2.CV_64F,1,0)
'''the first argument is the image whose edge we want to find
   the second argument is the datatype
   the third and fourth (1,0) indicated that the vertical edges are to be determied'''
sobelY= cv2.Sobel(image, cv2.CV_64F,0,1)
'''the first argument is the image whose edge we want to find
   the second argument is the datatype
   the third and fourth (1,0) indicated that the horizontal edges are to be determied'''

sobelX = np.uint8(np.absolute(sobelX))#np.absolute(sobelX)
sobelY = np.uint8(np.absolute(sobelY))#np.absolute(sobelY)
'''Why do we take absolute and convert the floating image into 8-bit unsigned integer'''

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined edge detection", sobelCombined)
cv2.waitKey(0)
cv2.destroyAllWindows()




## Canny Edge Detection
# Canny edge detection, unlike the Laplacian and Sobel is a long step by step process.

# We blurr the image (A special case for canny edge detection)
blurred_image=cv2.GaussianBlur(image, (5,5), 0)
    # The first argument is the GRAYSCALE BLURRED image
    # The Second argument is the threshold1
    # The third argument is the threshold2
    # Any value less than 30 is considered non-edge
    # Any value grater than 150 is considered an edge
    # and the values between 30 and 150 are considered edge and non-edge based on their varying intensities.
cv2.imshow("Blurred", image)

# Now we detect the canny edges
canny=cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()


'''
Points to know:
    1. While computing the gradient and edges we compute them in single channel,
       However, we can also compute in BGR channel, but we do it for the sake of simplicity
    2. In "lap=cv2.Laplacian(image, cv2.CV_64F)" we compute the gradient magnitude image.

Question:
    1. What is a gradient magnitude.
    Ans. Gradient magnitude is best described in the first copy of Image Processing. Please refer that.

    2. Why do we use 64-bit float now since overall we have been using 8-bit unsigned integers?
    Ans. For edge detection in a GRAYSCALE image we have to find the transition of white color
         and black. For example in our coins diagram the coins are in black color, to find the edges
         of the coins we have to find the transition of white to black.

         These transition can be from black-to-white or white-to-black. black-to-white is considered
         as a positive slope whereas white-to-black is considered as a negative slope and 8-bit
         unsigned integers doesnot represent -ve numbers, therefore we use 64bit float.
         If we dont use 64bit float we will miss out the edges that requires transition from white-to-black.

    3. Why do we combine the SobelX and SobelY using bitwise_or?
    Ans: Because our GRAYSCALE color is represented in black and white color where white represents the edges
         . The white is represented as 1 and black is represented as 0. Horizontal edges are missed out SobelX
         and hence the edges are black in color, similarly, Vertical edges are missed by sobelY leaving them black in color.
         But the edges missed by sobelX are caught by sobelY and viceversa. So at any cost either of them would have the edge
         as white in color. Hence we use OR because OR states 0+1=1(white) 1+0=1(white) and (1+1)=1(white).
         Which states if any of the edge is white then make it white. And hence it is easy to detect the edges.

    4. What is the importance canny Edge detection and why do we blurr the image while canny edge detection
    Ans: Since while finding the edges we are only interested in finding the edges not the inner edges, For example In the coin image
         we are only interested in finding the outer edge, but due to the pixels inside the coins also vary in their
         intensity our laplacian and Sobel identifies the inner edges too. To avoid this inner edge detection we use canny.

         We perform blurr prior to edge detection because blurr helps us remove noisy edges, In our coin example the noisy edges
         are actually the inner edges of the coin
'''
