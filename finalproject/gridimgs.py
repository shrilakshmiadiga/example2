import cv2
import numpy as np
import matplotlib.pyplot as plt

i1=cv2.imread('C:/final project/cancer1.jpg')
i2=cv2.imread('C:/final project/input_file.jpg')
i3=cv2.imread('C:/final project/output_file.jpg')
i4=cv2.imread('C:/final project/output1_file.jpg')

list=[i1,i2,i3,i4]
ttl = ['image1','image2','image3','image4']

for i in range(4):
    titles= ttl[i]
    plt.subplot(3,4,i+1)
    plt.imshow(list[i])
    plt.title(titles)
    plt.xticks([])
    plt.yticks([])
plt.show()
