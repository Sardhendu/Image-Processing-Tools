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
import matplotlib as plt
import imutils
from matplotlib import pyplot as plt



## Let us now plot histogram with multiple channels (RGB)
# At first we resize out image because our image is too large to view it completely
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\red.jpg")
image=imutils.resize(image, height=500)         # Resizing
cv2.imshow("original", image)


# It gets a bit tricky in here because to plot histogram for multiple channels we would have to plot them one by one.
# Therefore, we have to do a loop for each channel

# 1. We split the image into (BGR)
chan_image=cv2.split(image)   # this will give us an array of three image (Blue, Green and Red)
colors=("b","g","r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")


for (chan_image, color) in zip(chan_image, colors):
    chan=chan_image
    hist=cv2.calcHist([chan_image], [0],None, [256], [0,256]) # [chan_image] is nothing but the image in blue, green and red color
    # since we are using loop. Therefore, at a particular loop we only deal with one channel
    # Hence we use channel as [0] and range as [0,256]
    plt.plot(hist, color=color)
    plt.xlim([0,256])

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()




'''
Note:
1. chan_image will give an array with three tuppels, or see for yourself the output below
  [
     array(
            [
               [ 90,  94,  95, ..., 159, 154, 149],
               [ 87,  88,  85, ..., 150, 157, 156],
               [ 81,  85,  89, ..., 136, 139, 155],
               ...,
               [121, 123, 122, ..., 125, 137, 134],
               [115, 119, 124, ..., 134, 141, 140],
               [108, 113, 123, ..., 151, 160, 162]
            ],
            dtype=uint8
          ),
     array(
            [
               [123, 128, 128, ..., 170, 165, 161],
               [120, 122, 118, ..., 159, 167, 167],
               [114, 119, 123, ..., 144, 148, 166],
               ...,
               [141, 144, 145, ..., 141, 151, 147],
               [135, 140, 145, ..., 149, 154, 151],
               [127, 133, 143, ..., 167, 173, 173]
            ],
            dtype=uint8
           ),
     array(
            [
               [171, 174, 174, ..., 183, 179, 175],
               [168, 168, 164, ..., 171, 181, 181],
               [161, 165, 170, ..., 156, 161, 178],
               ...,
               [175, 176, 176, ..., 161, 170, 166],
               [170, 173, 177, ..., 170, 172, 170],
               [162, 166, 174, ..., 188, 192, 193]\
            ],
            dtype=uint8
           )
  ]

2. Colors is just a tuple ('b','g','r')

3. When we zip channel and colors we get something like
  [
    (array
      (
        [ [ 90,  94,  95, ..., 159, 154, 149],
          [ 87,  88,  85, ..., 150, 157, 156],
          [ 81,  85,  89, ..., 136, 139, 155],
          ...,
          [121, 123, 122, ..., 125, 137, 134],
          [115, 119, 124, ..., 134, 141, 140],
          [108, 113, 123, ..., 151, 160, 162]  ], dtype=uint8
      ),
    'b'
    ),

    (array
      (
        [ [123, 128, 128, ..., 170, 165, 161],
          [120, 122, 118, ..., 159, 167, 167],
          [114, 119, 123, ..., 144, 148, 166],
          ...,
          [141, 144, 145, ..., 141, 151, 147],
          [135, 140, 145, ..., 149, 154, 151],
          [127, 133, 143, ..., 167, 173, 173]   ], dtype=uint8
      ),
     'g'
    ),

    (array
      (
        [ [171, 174, 174, ..., 183, 179, 175],
          [168, 168, 164, ..., 171, 181, 181],
          [161, 165, 170, ..., 156, 161, 178],
          ...,
          [175, 176, 176, ..., 161, 170, 166],
          [170, 173, 177, ..., 170, 172, 170],
          [162, 166, 174, ..., 188, 192, 193]   ], dtype=uint8
     ),
     'r'
    )
  ]


4. Why go through such trouble doing all that zip and other stuff?
Ans: Because we would compute ahistogram for each chan_image (blue, green and red)
     our for loop is
     "for (chan_image, color) in zip(chan_image, colors)"
     With the zip we ensure that the right color comes for the right chan_image

     i.e
     for channel--
     (array
      (
        [ [ 90,  94,  95, ..., 159, 154, 149],
          [ 87,  88,  85, ..., 150, 157, 156],
          [ 81,  85,  89, ..., 136, 139, 155],
          ...,
          [121, 123, 122, ..., 125, 137, 134],
          [115, 119, 124, ..., 134, 141, 140],
          [108, 113, 123, ..., 151, 160, 162]  ], dtype=uint8
      )
      our color value should be
      "b"


5. Do the below and you will understand the importance of the zip function
x = [[1, 2, 3],[3,2,1], [2,1,3]]
y = (4, 5, 6)
zipped = zip(x, y)

'''