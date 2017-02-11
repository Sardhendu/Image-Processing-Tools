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

import math
import cv2


# First we calculate the RGB, we call it luminosity. 
# Here We calculate the GRAY scale colors of the colored image
def cal_luminosity(bgr, rcoff=0.2126, gcoff=0.7152, bcoff=0.0722):     # BGR because we have used openCV to load the image
    luminosity=(bcoff*bgr[0])+(gcoff*bgr[1])+(rcoff*bgr[2])
    return luminosity


# Not needed in our case because we take care of the pixel coordinate in generate_pixel function ,, anyway this checks if the pixel in process is in range of the pixel size
def check_pixel_range (image, r, c):    #c is the column and r is the row
    total_size_xaxis=image.shape[1]
    total_size_yaxis=image.shape[0]
    return c>0 and c<total_size_xaxis-1 and r>0 and r<total_size_yaxis-1



# Calculate the dy (the change in y axis) we need the vertical neighbours to calculate dy
def cal_dy (image, r,c, default_delta=1.0):

    if not check_pixel_range(image,r,c):
         return default_delta
    #print "dydydydydydydydydydydydyd"
    #vertical_neighbor_intensity_change=cal_luminosity(image[c,r-1])- cal_luminosity(image[c,r+1])
    vertical_neighbor_intensity_change=cal_luminosity(image[r-1,c])- cal_luminosity(image[r+1,c]) # we have taken (r-1,c) and (r+1,c) because in openCV an image point is read as (r,c) not (c,r)
    dy=vertical_neighbor_intensity_change

    if dy==0:
        return default_delta
    else:
        return float(dy)



# Calculate the dx (the change in x axis) we need the horizontal neighbors to calculate dx
def cal_dx (image, r, c, default_delta=1.0):

    if not check_pixel_range(image,r,c):
         return default_delta
    #print "dxdxdxdxdxdxdxdxdxdxdxdxd"
    #horizontal_neighbor_intensity_change=cal_luminosity(image[c-1,r])- cal_luminosity(image[c+1,r])
    horizontal_neighbor_intensity_change = cal_luminosity(image[r,c-1])- cal_luminosity(image[r,c+1]) # we have taken (r-1,c) and (r+1,c) because in openCV an image point is read as (r,c) not (c,r)
    dx=horizontal_neighbor_intensity_change

    if dx==0:
        return default_delta
    else:
        return float(dx)


# Calculate the magnitude of the gradient
def cal_gradient_magnitude(dx, dy):
    magnitude=math.sqrt(math.pow(dx,2) + math.pow(dy,2))
    return magnitude

# Calculate the orientation of the gradient
def cal_gradient_orientation(dx,dy, default_theta=1.0):
    if dx==dy:
        return default_theta
    theta=math.atan2(dy,dx) * (180/math.pi)
    if theta<0:
        return math.floor(theta)
    elif theta>0:
        return math.ceil(theta)
    else:
        return theta


# to generate pixels
def generate_pixels(image):
    array=[]
    row,column=(image.shape[0],image.shape[1])
    r,c=0,0
    for r in range (0,row-1):
        for c in range(0,column-1):
            if r==0 or c==0 or r==row-1 or c==column-1:
                a=0
            else:
                array.append((r,c))

    return array




def main_call(image, theta_threshold=360, magnitude_threshold=20):
    coordinates_array=generate_pixels(image)
    print (coordinates_array)

    # # We create a output_canvas to plot the final image
    for i in range (0,len(coordinates_array)):
        r,c=coordinates_array[i]
        #print c,r
        dy=cal_dy(image, r,c)
        dx=cal_dx(image,r,c)
        magnitude=cal_gradient_magnitude(dx,dy)
        theta=cal_gradient_orientation(dx,dy)
        #print r, " ",c," ",dy,"   ",dx,"   ",magnitude,"   ", theta,"   ", "   ",image[r,c],"   ", "   ", cal_luminosity(image[r,c])

        # Converting the magnotude and orientation into integer
        magnitude=int(magnitude)
        theta=int(theta)

        if abs(theta)<=theta_threshold and abs(magnitude)>=magnitude_threshold:
            edged_detected_image[r,c]=255
        else:
            edged_detected_image[r,c]=0






######################################################################################################################################
#image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\sam.jpg")
#edged_detected_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\sam.jpg")



# image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\Data mining and analysis\\image_processing\\Research_1\\photo_research\\segregate\\DSC_0027.jpg")
# edged_detected_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\Data mining and analysis\\image_processing\\Research_1\\photo_research\\segregate\\DSC_0027.jpg")

#no_edges_blurr_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face_sized.jpg")

image=cv2.imread("/Users/sam/All-Program/App-DataSet/Kaggle-Challenges/CIFAR-10/trainDataAirplane/25178.png")
edged_detected_image=cv2.imread("/Users/sam/All-Program/App-DataSet/Kaggle-Challenges/CIFAR-10/trainDataAirplane/25178.png")

##########################################    Run the below command     ################################

main_call(image)
cv2.imshow("Original_image", image)
cv2.imshow("edge_detected", edged_detected_image)
cv2.waitKey(0)