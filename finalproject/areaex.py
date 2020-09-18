import cv2
import numpy as np

image=cv2.imread('C:/Users/dell/Desktop/LIDC/segmented/testing/LIDC_2,4.png')
cv2.imshow('input image',image)
cv2.waitKey(0)

edged=cv2.Canny(image,30,200)
cv2.imshow('canny edges',edged)
cv2.waitKey(0)

#use a copy of your image, e.g. - edged.copy(), since finding contours alter the image
#we have to add _, before the contours as an empty argument due to upgrade of the OpenCV version
contours =cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.imshow('canny edges after contouring', edged)
cv2.waitKey(0)

print(contours)
print('Numbers of contours found=' + str(len(contours)))

#use -1 as the 3rd parameter to draw all the contours
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
