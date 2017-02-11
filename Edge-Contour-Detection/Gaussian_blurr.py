#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sardhendu_Mishra
#
# Created:     20/02/2015
# Copyright:   (c) Sardhendu_Mishra 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import cv2


#imutils

# Getting the neighbors
def generate_neighbors_and_weight(kernel,r,c):
    arr_neighbor=[]
    arr_value_weight=[]
    for i in range (0, kernel):
        sub_no=i-((kernel-1)/2)

        for j in range (0, kernel):
            sub_no_2=j-((kernel-1)/2)
            row=r+sub_no
            column=c+sub_no_2
            arr_neighbor.append((row,column))
            arr_value_weight.append((abs(r-row), abs(c-column)))

    return arr_neighbor, arr_value_weight


# Performing gaussian on the neighbors
def gaussian_value(neighbors_weights, sd_sigma):
    # Calculating gausian weight
    arr_gaussian_weight=[]
    for i in range (0, len(neighbors_weights)):
        left_term=0
        right_term=0
        x,y=neighbors_weights[i]
        left_term=1/(2*3.14 * math.pow(sd_sigma,2))
        right_term=math.exp(-1 * ( (math.pow(x,2)+math.pow(y,2)) / (2 * math.pow(sd_sigma,2))))
        arr_gaussian_weight.append(left_term * right_term)

    return arr_gaussian_weight


# to generate pixels:
#Why do we generate pixels, because the code we write will search for neighbors in all the direction i.e x, y, -x, -y but for pixel 0,0 we dont have any y or -x direction
# so according to the kernel provided we get rid of some pixels.


def generate_coordinates(image, kernel):
    array_coordinate=[]
    elimination_rc=(kernel-1)/2
    # if kernel =3 then elimination_rc will be 1
    # if kernel=5 then elimination_rc will be 2
    row,column=(image.shape[0]-1,image.shape[1]-1)
    r,c=0,0
    for r in range (0,row):
        for c in range(0,column):
            if (r>=elimination_rc and r<=(row)-elimination_rc and c>=elimination_rc and c<=(column)-elimination_rc):
                array_coordinate.append((r,c))

    return array_coordinate



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
        #print image[neighbors_coordinates[count]]


    # The below code will multiply the weighted gaussian with the pixel value of each neighbor
    neighbors_weighted_pixel=[a*b for (a,b) in zip(gaussian_fnl_weights, pixel_value)]

    ##for ww in range(0,len(neighbors_weighted_pixel)):
      ##  print  neighbors_weighted_pixel[ww]

    # Now wew compute the sum of the new weighted neighbors and return it to the main_call, because the sum is our new pixel
    return reduce(lambda x, y: x + y, neighbors_weighted_pixel)



def main_call(image, kernel_val, sd):
    #for x_axis in range(0,image.shape[0]):
    #     for y_axis in range(0,image.shape[1]):
    coordinated_arr=generate_coordinates(image, kernel_val)
    for coordinates in range(0, len(coordinated_arr)):
        (r,c)=coordinated_arr[coordinates]
        new_pixel_value=new_pixel_value=main_functionality(image, kernel_val, sd, r,c)
        output_image[r,c]=new_pixel_value





#######################################################################################################
image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face_sized.jpg")
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


output_image=cv2.imread("C:\\Users\\sardhendu_mishra\\Desktop\\StudyHard\\Machine_learning\\photus\\face_sized.jpg")
output_image=cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)

# Blurring using gaussian blurring with OpenCV
#blurred_image=cv2.GaussianBlur(image,(11,11), 5.5)
#cv2.imshow("Blurred gausian CV2 image", blurred_image)

##########################################    Run the below command     ################################

main_call(image,11,5.5)
cv2.imshow("original_image", image)
cv2.imshow("blurred_image", output_image)
cv2.waitKey(0)
# The first image is blurred image with kernel 5 passed to gaussian CV2 function.
# The second image is our original image
# The third image is blurred image with kernel 5 developed by the code.

