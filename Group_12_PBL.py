#import cv2 for reading image and for converting the color
import cv2
import numpy as np
#import of matplotlib. pyplot is for detecting the spot in shape 
import matplotlib.pyplot as pt
#cv2.imread is use to read the mage form its path
image=cv2.imread('image.jpg')
#cv2.risize is use to resize the image  
image1=cv2.resize(image,(500,700))

#convert the image color to grayscale
grayscale= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img1=cv2.resize(grayscale,(500,700))
#use of minmaxLoc for coordinate of the brightest spot
(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(img1)
#circle shape if the brightest point
cv2.circle(image1, maxLoc, 5, (255, 0, 0), 2)
#show the brightest spot 
cv2.imshow("Robust", image1)
print("The Coordinate of Brightest spot is : ",maxLoc)
cv2.waitKey(0)
#the brightest spot is shown in circle

