#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     23/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import cv2

import sys
sys.path.insert(0, '/Users/sam/All-Program/App-DataSet/Image-Processing')

import imutils

class FaceDetector:

    def __init__(self):
        self.faceCascade=cv2.CascadeClassifier("C:\\Python27\\Lib\\site-packages\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")

    def detect_the_rect_area (self,image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)):
        rects=self.faceCascade.detectMultiScale(image,
                                               scaleFactor=scaleFactor,
                                               minNeighbors=minNeighbors,
                                               minSize=minSize)
                                              # flag= cv2.cv.CV_HAAR_SCALE_IMAGE)

        return rects



#faceCascade = cv.Load("C:\\Python27\\Lib\\site-packages\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
image=cv2.imread("/Users/sam/All-Program/App-DataSet/Image-Processing/face.jpg")

# Resize the image
image_resized=imutils.resize(image, height=200)

# Convert the image into GRAYSCALE
image_GRAY=cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

# Now we create an instance for the class
fd_instance= FaceDetector()

face_rects=fd_instance.detect_the_rect_area(image_GRAY,
                                            scaleFactor=1.1,
                                            minNeighbors=5,     # 5*5 pixels area for the face
                                            minSize=(30,30))
print "I found %d face" % (len(face_rects))


# Lets plot the computed rectangle on the resized but color image,
# For loop is given to take care if there are multiple faces.
for (x, y, w, h) in face_rects:
   cv2.rectangle(image_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("Faces", image_resized)
cv2.waitKey(0)