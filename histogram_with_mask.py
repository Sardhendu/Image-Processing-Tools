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


'''
This package is meant to plot histogram by taking few arguments like the image, title and mask area

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# We define a function that will plot the histogram for the three channels (BGR) for the masked area

def plot_histogram(image, title, mask=None): # Mask is set default to none when no masking region is provided
    chan_image=cv2.split(image) # we split the image into different channels
    colors= ("b","g","r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan_image, color) in zip(chan_image, colors):
        hist=cv2.calcHist([chan_image], [0], mask, [256],[0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])