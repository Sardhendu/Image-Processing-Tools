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

''' Masking is an very important topic in computer vision, It helps you get the parts
    of the image that you are interested in. For example If you are interested in the face
    then masking can help you extract the face out of the image
'''

# We will heavily use the Bitwise operators for masking

##  Displaying the original image
import numpy as np
import cv2
import imutils


image= cv2.imread("/Users/sam/All-Program/App-DataSet/Image-Processing/sam.jpg")
cv2.imshow("Original_image", image)
cv2.waitKey(0)



## Our Image is too large, hence we first shorten it using resizing
resized=imutils.resize(image, height=500)  # Passing the new height of the image , the width is automatically calculated in resize method of the imutil package
cv2.imshow("resized image", resized)
cv2.waitKey(0)
image=resized


## Now we determine the pixels that contains the head
cropped= image[7:230, 25:235]  # basically we display the pixel in that particulae area
# nuply array takes array input as (height * width)
cv2.imshow("cropped image", cropped)
cv2.waitKey(0)


## Now we perform Masking from center
# Now we perform masking on the original image, Here we would manually provide the pixels
# First we create a rectangle, because faces are suppose to be of rectangle size
# First lets just define a rectangle white in color and mask it in the center
mask=np.zeros(image.shape[:2], dtype="uint8")  # we create a mask with same array size as that of our image
(cx, cy)= (image.shape[1]/2, image.shape[0]/2) # we take the center point
cv2.rectangle(mask, (cx-105,cy-111), (cx+105,cy+111), 255,-1)  # (width(cx) * height(cy)
cv2.imshow("Mask_rectangle", mask)
cv2.waitKey(0)

masked=cv2.bitwise_and(image, image,mask=mask)
cv2.imshow("Masked_from_center", masked)
cv2.waitKey(0)


## Now we perform Masking of face
# Now we will shift the center and extract the face
mask=np.zeros(image.shape[:2], dtype="uint8")  # we create a mask with same array size as that of our image
(cx, cy)= (105, 111) # we take the center point
cv2.rectangle(mask, (cx-(105-25),cy-(111-7)), (cx+(235-105),cy+(230-111)), 255,-1) # (width(cx) * height(cy)
cv2.imshow("Mask_rectangle", mask)
cv2.waitKey(0)

masked=cv2.bitwise_and(image, image,mask=mask)
cv2.imshow("Masked_from_center", masked)
cv2.waitKey(0)




cv2.destroyAllWindows()

