#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     24/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import cv2

import sys
sys.path.insert(0, '/Users/sam/All-Program/App/Image-Processing/')
import imutils
from functools import reduce



#==============================================================================
#   Gaussian BLURR 
#==============================================================================
# Getting the neighbors
def generate_neighbors_and_weight(kernel,r,c):
    arr_neighbor=[]
    arr_value_weight=[]
    for get_size in range (0, kernel):
        sub_no=get_size-((kernel-1)/2)

        for get_size_2 in range (0, kernel):
            sub_no_2=get_size_2-((kernel-1)/2)
            row=r+sub_no
            column=c+sub_no_2
            arr_neighbor.append((row,column))
            arr_value_weight.append((abs(r-row), abs(c-column)))

    return arr_neighbor, arr_value_weight


# Performing gaussian on the neighbors
def gaussian_value(neighbors_weights, sd_sigma):
    # Calculating gausian weight
    arr_gaussian_weight=[]
    for gaussian_wt in range (0, len(neighbors_weights)):
        left_term=0
        right_term=0
        x,y=neighbors_weights[gaussian_wt]
        left_term=1/(2*3.14 * math.pow(sd_sigma,2))
        right_term=math.exp(-1 * ( (math.pow(x,2)+math.pow(y,2)) / (2 * math.pow(sd_sigma,2))))
        arr_gaussian_weight.append(left_term * right_term)

    return arr_gaussian_weight

# to generate pixels:
#Why do we generate pixels, because the code we write will search for neighbors in all the direction i.e x, y, -x, -y but for pixel 0,0 we dont have any y or -x direction
# so according to the kernel provided we get rid of some pixels.


def main_functionality(image,kernel, sd_sigma,r,c):

    neighbors_coordinates, neighbors_weights=generate_neighbors_and_weight(kernel,r,c)
    gaussian_weight=gaussian_value( neighbors_weights, sd_sigma)

    ''' we know that the sum of the gaussian weight should be equal to 1 but if we add the total gaussian weight we dont get equall to 1
        so we simply multiply a value to each of the gaussian list to make their total sum= 1
    '''
    balancing_value=(1/sum(gaussian_weight))
    gaussian_fnl_weights=[j *balancing_value for j in gaussian_weight]

    ''' Now we multiply the computed gaussian_fnl_weighted with the pixel value and find the resultant average
        and then finally subtitute the pixel with the average value. But to find the pixel value we will have to call the luminosity function
    '''
    # We find the total pixel value of the neighboring coordinates
    pixel_value=[]
    for count in range(0, len(neighbors_coordinates)):
        pixel_value.append(image[neighbors_coordinates[count]])
        #print neighbors_coordinates[count]
    # The below code will multiply the weighted gaussian with the pixel value of each neighbor
    neighbors_weighted_pixel=[a*b for (a,b) in zip(gaussian_fnl_weights, pixel_value)]
    ##for ww in range(0,len(neighbors_weighted_pixel)):
      ##  print  neighbors_weighted_pixel[ww]
    # Now wew compute the sum of the new weighted neighbors and return it to the main_call, because the sum is our new pixel
    return reduce(lambda x, y: x + y, neighbors_weighted_pixel)



def main_call_blurr(image, kernel_val, sd, r,c):
    #for x_axis in range(0,image.shape[0]):
    #     for y_axis in range(0,image.shape[1]):
    new_pixel_value=new_pixel_value=main_functionality(image, kernel_val, sd, r,c)
    output_image[r,c]=new_pixel_value






#==============================================================================
#  Edge Detection 
#==============================================================================

# First we calculate the RGB, we call it luminosity. Basically we calculate the GRAY scale colors of the colored image
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
    horizontal_neighbor_intensity_change=cal_luminosity(image[r,c-1])- cal_luminosity(image[r,c+1]) # we have taken (r-1,c) and (r+1,c) because in openCV an image point is read as (r,c) not (c,r)
    dx=horizontal_neighbor_intensity_change

    if dx==0:
        return default_delta
    else:
        return float(dx)


# Calculate the magnitude of the gradient
def cal_gradient_magnitude(dx, dy):
    magnitude=math.sqrt(math.pow(dx,2) + math.pow(dy,2))
    return magnitude

# Caluculate the orientation of the gradient
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


def main_call_edge(image,kernel ,coordinates, sd,theta_threshold=360, magnitude_threshold=20):

    # We create a output_canvas to plot the final image
    for i in range (0,len(coordinates)):
        r,c=coordinates[i]

        # Check id the coordinate is present in both array_coordinate_blurr=[] and coordinates=[]. If yes only then procees for the blurring
        if (r,c) in array_coordinate_blurr:
            #print r,c
            dy=cal_dy(image, r,c)
            dx=cal_dx(image,r,c)
            magnitude=cal_gradient_magnitude(dx,dy)
            theta=cal_gradient_orientation(dx,dy)
            #print r, " ",c," ",dy,"   ",dx,"   ",magnitude,"   ", theta,"   ", "   ",image[r,c],"   ", "   ", cal_luminosity(image[r,c])

            # Converting the magnotude and orientation into integer
            magnitude=int(magnitude)
            theta=int(theta)

            if abs(theta)<=theta_threshold and abs(magnitude)>=magnitude_threshold:  # This code will detect an edge so we wont blurr that area
                a=0
            else:
                print ("aaaaaaaa")
                main_call_blurr(image, kernel, sd, r,c)
                








#==============================================================================
# Generate Coordinates for blurr pixels and  edge detection pixels 
#==============================================================================



def generate_coordinates_blurr(image, kernel):
    array_coordinate_blurr=[]
    elimination_rc=(kernel-1)/2
    # if kernel =3 then elimination_rc will be 1
    # if kernel=5 then elimination_rc will be 2
    row,column=(image.shape[0]-1,image.shape[1]-1)
    r,c=0,0
    for r in range (0,row):
        for c in range(0,column):
            if (r>=elimination_rc and r<=(row)-elimination_rc and c>=elimination_rc and c<=(column)-elimination_rc):
                array_coordinate_blurr.append((r,c))

    return array_coordinate_blurr


# to generate pixels
def generate_coordinates_edgedetect(image):
    array_coordinate_edgedetect=[]
    row,column=(image.shape[0],image.shape[1])
    r,c=0,0
    for r in range (0,row-1):
        for c in range(0,column-1):
            if r==0 or c==0 or r==row-1 or c==column-1:
                a=0
            else:
                array_coordinate_edgedetect.append((r,c))

    return array_coordinate_edgedetect


############################## Call one by one ###############################

# image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\Data mining and analysis\\image_processing\\Research_1\\photo_research\\segregate\\DSC_0037.jpg")
# output_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\Data mining and analysis\\image_processing\\Research_1\\photo_research\\segregate\\DSC_0037.jpg")

image=cv2.imread("/Users/sam/All-Program/App-DataSet/Kaggle-Challenges/CIFAR-10/trainDataAirplane/25178.png")
output_image=cv2.imread("/Users/sam/All-Program/App-DataSet/Kaggle-Challenges/CIFAR-10/trainDataAirplane/25178.png")

# image=imutils.resize(image, width=600)
# output_image=imutils.resize(output_image, width=600)
#image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face_sized.jpg")
#output_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face_sized.jpg")
array_coordinate_blurr = generate_coordinates_blurr(image, 3)
array_coordinate_edgedetect = generate_coordinates_edgedetect(image)

# print (array_coordinate_blurr)
print (array_coordinate_edgedetect)
# main_call_edge(image,array_coordinate_blurr, 9,7.5)
# cv2.imshow("d", output_image)
# cv2.imshow("or", image)
# cv2.waitKey(0)
