import os
import cv2

data=[]
for file in os.listdir("F:\demoimages"):
    img=cv2.imread(file)
    data.append(img)

img1=data[0]
cv2.imshow('imgis',img1)
