#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     17/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
A contour is a curve of a point. A curve can be full circle or a small curve with no gaps in it.
By the use of contours we can determine the shape of an object wheather it is a circle or tringle or rectangle.
In order to plot the contour or count the number of curves we will have to obtain the binarization
of the image (black and white version) either by thresholding or by edge dectection.

'''

import cv2
import numpy as np


# Load the image
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face.jpg")
cv2.imshow("original image",image)
cv2.waitKey()

# We convert the colored image into GRAYSCALE image
grayscale_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY scale color", grayscale_image)
cv2.waitKey()

# We perform blurring with Gaussian
blurred_image=cv2.GaussianBlur(grayscale_image, (11,11), 0)
        # We take (11,11) because this will blurr the image properly getting rid of most of the noise.
        # Which will help canny edge dectector to identify the edge properly
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey()

# Now to perform canny Edge detection
edged_image=cv2.Canny(blurred_image, 20,150)
cv2.imshow("canny Edge detected", edged_image)
cv2.waitKey()



# Now finally we find the count of copins using contours of the edged image
(cnts, _)=cv2.findContours(edged_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # The above code returns a tuple 1. the count of contours and 2. the hierarchy of the contours which will come in handy at a later point of time
        # The first argument is the binary image with detected edges. We take a copy because the contours functions destroys our original image.
        # The second argument is the type of contours we want to use. Other function are like cv2.RETR_LIST, cv2.RETR_COMP and others
        # The third argument is just a technique to compress the contours point. We dont eant all the points of the contour, that would be memory wastage.
             # In order to get all the point on the contour we can use cv2,CHAIN_APPROX_NONE
print "There are %d coins in the image" % (len(cnts))

# Now we draw the contours on the edged image
coins=image.copy()
cv2.drawContours(coins, cnts, -1,(0,255,0),2)
        # (0,255,0) indicates to plot the contours in green color
        # -1 indicates that we have to draw all the contours, we can also suply the index to draw any one or few contours instead of all
        # 2 is the thickness of the contours, if you provide a -1 it will cover the entire coin structure.
cv2.imshow("Coins", coins)
cv2.waitKey()

# Plotting few contours not all with different color
coins_few=image.copy()
cv2.drawContours(coins_few, cnts, 0,(0,255,0),2)
cv2.drawContours(coins_few, cnts, 1,(255,0,0),6)
cv2.drawContours(coins_few, cnts, 4,(0,0,255),-1)
cv2.imshow("Coins", coins_few)
cv2.waitKey()


cv2.destroyAllWindows()







''' CROPING INDIVIDUAL ELEMENT FROM THE IMAGE
CNTS:   The output of the cnts consists of 9 elements inside a list, since the count of coin is 9
        . However, it also consist the coordinated of each pixel point that form the counter.
        With the help these coordinated we can extract any particular piece of image from the original image
        Example if you are only interested in to coin 4 with the help of the coordinates we can easily find it.


        How is the array cnts?
        >>> cnts
        [array([[[126, 183]],

                [[125, 184]],

                [[122, 184]],

                [[121, 185]],

                [[119, 185]],
                    .
                    .
                    .
                    .
'''
# To find a particular coin from the image we enumerate over the cnts array fetching each coin one by one
# And then we fetch the coordinates of each coins, and after fetching the coordinates we mask on the image to find the particular item.

for (i,c) in enumerate(cnts):
    # I is the coin number and c is the list of the coordinates (boundaries coordinates) of that coin
    # Lets only crop the 1st coin
    if i==0:   # for the first coin
        (x,y,w,h)=cv2.boundingRect(c)
            # The use of boundingRect on out current contour finds a box
            # x and y are the position that the box (rectangle) starts
            # w and h are the width and height that the rectangle encloses

        coin=image[y:y +h, x:x +w]
        cv2.imshow("Coin", coin)
        cv2.waitKey(0)

        # The above code extracts the coin image


'''The above code extract the 1st coin out of the image. but the coin comes witha rectangular border.
   We know that our coins are circular in shape, so it is better if we find the exact circe instead of the rectangular box
'''
for (i,c) in enumerate(cnts):
    if i==0:
        # Now we form a mask
        mask =np.zeros(image.shape[:2], dtype="uint8")
        # Finding the circular coordinates
        ((centerX, centerY), radius)= cv2.minEnclosingCircle(c)
        # Now we find the circle of first coin in the mask image (complete black image)
        cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255,-1)
        mask=mask[y:y +h, x:x +w]
        # We mask the masked image upon the original image to find the coin
        cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask =mask))
        cv2.waitKey(0)






