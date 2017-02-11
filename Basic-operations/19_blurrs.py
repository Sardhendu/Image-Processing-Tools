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
There are four blurring techniques we will discuss
1. Averaging
2. Gaussian
3. Median
4. Bilatral

Question:
1. Why is blurring important?
Ans: An image looks more sharp and clear if we are able to perceive all its object and shapes correctly.
     For example consider a face, the eye eye pupil has a different color, the eyelid has a different color,
     the eyebrow has a different color comnbination all together there are a lot of differences in the eye itself.
     In a face how would you identify a eye if there are so many differences. Therefore, blurring help in reducing the edge contents
     and makes the transition from one color to other color very smooth. For instance
     by blurring a face one can easily make out that eye (that consist of eye pupil, eyelid, and others).

2. What the blurr does?
Ans: It basically mixes each of the pixels with its surrounding pixels intensities, the mixture of pixels in a
     neighbourhood becomes our blurred pixel.

'''

import numpy as np
import cv2
import imutils

# Load the image and resize
image=cv2.imread("/Users/sam/All-Program/App-DataSet/Kaggle-Challenges/CIFAR-10/trainDataTruck/187.png")
image= imutils.resize(image, height=200)


## Averaging:
blurred= np.hstack([image,
                    cv2.blur(image, (3,3)),
                    cv2.blur(image, (5,5)),
                    cv2.blur(image, (7,7)),
                    cv2.blur(image, (9,9)),
                    cv2.blur(image, (11,11))])
# cv2.destroyWindow("Averaged")
# cv2.waitKey(-1)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

'''
Question:
1. why do we use only odd number and what are those actually?
Ans: It is odd number because with odd number it is always easy to find one center,
     For example consider a 3*3 matrix, for this matrix position [2,2] can be stated as one center
     But for a 2*2 or 4*4 matrix there is no common center. Well we can always use even number, there is no restriction
     using them. However, it is preferable to use odd numbers.

2. What exactly are these (3,3), (5,5)
Ans: What we do is create a window of 3*3 i.e 3*3 pixels in the top left corner of the original image
     This window slides to the right and bottom blurring the image
     What happens is that the center pixel is replaced with the average weight of the neighbour pixels
     For Exmaple : for a (3,3) kernel the center [2,2] is relaced by the average pixel value of
                   [1,1][1,2][1,3], [2,1][2,3], [3,1][3,2][3,3]

     For instance check out the blurred image of (11,11) , you see that the whole eye section has become black in color
     the eye portion in (11,11) can be easily identified when compared to our original image

     These (3,3), (5,5) are called "Convolution Kernels" or just "kernels"
'''



# Gaussian blurror weighted mean
blurred= np.hstack([image,
                    cv2.GaussianBlur(image, (3,3),0),
                    cv2.GaussianBlur(image, (5,5),0),
                    cv2.GaussianBlur(image, (7,7),0),
                    cv2.GaussianBlur(image, (9,9),0),
                    cv2.GaussianBlur(image, (11,11),0)])
cv2.imshow("gaussian", blurred)
cv2.waitKey(0)



'''
Questions
1. What is difference between average and gaussian blurr?
Ans:  Average Blurr-> the average blurr is just the simple mean, you find the center and blur the image accordingly.
      Gaussinan Blurr-> The gaussian blurr is weighted averaged mean
                        that is for a blurr kernel (11,11) the pixels near the center like (2*2),(2*4) (3*3) would contribute
                        more to the color intensities than the pixels at the outer parts like (9*9),(9*10) (10*10).

                        There fore our edge even smoothes better

2. What is the third argument (0) in the cv2.GaussianBlur(image, (3,3),0)?
Ans: This is just the standard deviation (sigma), by setting the value of zero we are instructing
     the overCV to automatically compute them based on our kernel size.
'''




# Median Blurr
blurred= np.hstack([image,
                    cv2.medianBlur(image, 3),
                    cv2.medianBlur(image, 5),
                    cv2.medianBlur(image, 7),
                    cv2.medianBlur(image, 9),
                    cv2.medianBlur(image, 11)])
cv2.imshow("median", blurred)
cv2.waitKey(0)

'''
Question
1. What is the importance of median blurr over average and gaussian blurr
Ans: The gaussian and average blurr calculates the weighted average and average of the neighbourhood pixels respectively.
     There may be a case in which the calculated value may not be present in the neighbourhood.
     For example In lay man terms you have a stack of 1,2,3,4,7 there average is 3.4 which is not present in the stack. \
     And our gaussian and average blurr algo says just replace the center with the average i.e(3.4) which is not present in the neighbour stack
     which inturn is not a good result.

     In median blurr indtead of taking the average we just take the median vaklue of the neighbour and replace the center pixel with the median value.
     for Example 1,2,3,4,7 the median is 3 which will one of the neighbouring stack.
     And it can be concluded that the median pixel will always exist in the neighbourhood.
     which will indefinately give better results.

2. When should median blurr be used?
Ans: When you want to remove the detail and noise of a image.
     For example see the median blur image for kernel size 7 or 11. you cna find that the details like
     edge of ear, or the depth of eye ort the eyelid persay, the two holes of nose are all lost.

'''





# Bilateral Blurr
blurred= np.hstack([image,
                    cv2.bilateralFilter(image, 3,11,11),
                    cv2.bilateralFilter(image, 5,21,21),
                    cv2.bilateralFilter(image, 7,31,31),
                    cv2.bilateralFilter(image, 9,41,41),
                    cv2.bilateralFilter(image, 11,51,51)])
cv2.imshow("bilateral", blurred)
cv2.waitKey(0)
