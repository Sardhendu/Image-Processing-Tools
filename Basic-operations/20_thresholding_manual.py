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
Thresholding is also called as binarization of an image.
Thresholding is a technique in which we convert a GRAYSCALE image into a binary image.
binary in image terms is not the value 0 and 1, but quite similar to it.
With the use of thresholding we convert a image into black and white pixels
i.e either 0 or 255.

1. How do we achieve it?
Ans: We first choose a threshold value and all the pixel value that is lower than the
threshold point is converted to 0 and all the pixel value greater than the threshold value is converted to 255.
For example In a GRAYSCALE we have pixels ranging from [0-255]. suppose we take a threshold value of 150
            so all the pixels value in the GRAYSCALE image that are >150 will be changed to 255
            and all the pixels value in the GRAYSCALE image that are =<150 will be changed to 0.
            Hence our GRAYSCALE image will be turned to black and white image or binary image
'''


##  Our aim in this section is to find the coins in an image

import numpy as np
import cv2


# Lets do some thresholding

image=cv2.imread("/Users/sam/All-Program/App-DataSet/Image-Processing/coins.png")
original_image= image
cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Now we convert the image into GRAYSCALE
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)
cv2.waitKey(0)

# Now we do blurring for 5*5 pixels
blurred_image= cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred image", blurred_image)
cv2.waitKey(0)

# Lets apply thresholding at point 155
(T, thresh)= cv2.threshold(blurred_image, 155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

# Lets apply thresholding inverse at point 155
(T, threshInv)= cv2.threshold(blurred_image, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold BInary Inverse", threshInv)
cv2.waitKey(0)

# Now we perform masking on the GRAYSCALE image and then find our coins
masked=cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Coins", masked)
cv2.waitKey(0)

# Now we perform masking on the original image and then find our coins
masked=cv2.bitwise_and(original_image, original_image, mask=threshInv)
cv2.imshow("Coins", masked)
cv2.waitKey(0)



'''
Question:
1. Why is blurring important.
Ans Blurring is important because it helps us get rid of few high frequency edges.
    You would understand it better if you did the threshold without the blurring and then
    compare it to the threshold with blurring. Without blurring you would find the
    white shines on many coins which would cause problem while performing thresholding on them.

2. Why do we need THRESH_BINARY when we accomplish all the job with THRES_BINARI_INV
Ans: it just done to have an understanding. We will use it later

3. Why is masking done?
Ans: After thresholding we get the binary image of the coins, the coins are shaped white in color
     and the other parts are black. now to identify the coins in the original image we mask the
     binary threshold image onto the original image.
     In short masking helps us to reveal the coins in the image and hide everything else

4. What are the input arguments to the threshold function
Ans: The first argument is the image you want to threshold
     The second argument is the threshold level
     The third argument is the maximum value applied during thresholding
     The fourth argument is the type of thresholding or method of thresholding
'''