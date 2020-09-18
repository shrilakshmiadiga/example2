import numpy as np
import cv2
from matplotlib import pyplot as plt


#code for watershed algorithm.

#reading the input image and creating a copy of that
img = cv2.imread('C:/Users/dell/Desktop/LIDC/LIDC_2/IMG-0038-00001.jpg')
b,g,r = cv2.split(img)
rgb_img = cv2.merge([r,g,b])

#grayscale conversion and binarization
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



# noise removal
kernel = np.ones((2,2),np.uint8)

closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)


# sure background area
sure_bg = cv2.dilate(closing,kernel,iterations=3)



# Finding sure foreground area
dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,3)



# Threshold
ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)



# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)


# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]





plt.subplot(331),plt.imshow(rgb_img)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(332),plt.imshow(gray)
plt.title('gray image'), plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(thresh, 'gray')
plt.title("Otsu's binary threshold"), plt.xticks([]), plt.yticks([])

plt.subplot(334),plt.imshow(closing, 'gray')
plt.title("morphological closing"), plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.imshow(sure_bg, 'gray')
plt.title("Dilation"), plt.xticks([]), plt.yticks([])

plt.subplot(336),plt.imshow(dist_transform, 'gray')
plt.title("Distance Transform"), plt.xticks([]), plt.yticks([])
plt.subplot(337),plt.imshow(sure_fg, 'gray')
plt.title("Thresholding"), plt.xticks([]), plt.yticks([])

plt.subplot(338),plt.imshow(unknown, 'gray')
plt.title("Border detection"), plt.xticks([]), plt.yticks([])

plt.subplot(339),plt.imshow(img, 'gray')
plt.title("Result from Watershed"), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()


#taking images and their title in a list
imagelist=[rgb_img,gray,thresh,closing,sure_bg,dist_transform,sure_fg,unknown,img]
titles=['input image','gray image','binarization','closing operation','Background','erosion','foreground','borders','Result of watershed']

#displaying the images along with their title
for i in range(9):
    ttl=titles[i]
    plt.subplot(3,3,i+1)
    plt.imshow(imagelist[i])
    plt.title(ttl)
    plt.xticks([])
    plt.yticks([])
plt.show()

"""
#code for thresholding goes here

ret,o1 = cv2.threshold(rgb_img,127,255,cv2.THRESH_BINARY)
ret,o2 = cv2.threshold(rgb_img,127,255,cv2.THRESH_BINARY_INV)
ret,o3 = cv2.threshold(rgb_img,127,255,cv2.THRESH_TOZERO)
ret,o4 = cv2.threshold(rgb_img,127,255,cv2.THRESH_TOZERO_INV)
ret,o5 = cv2.threshold(rgb_img,127,255,cv2.THRESH_TRUNC)

imglist=[rgb_img,o1,o2,o3,o4,o5]
titl=['Input image','Binary thresholding','Binary inverted','Zero','Zero inverted','Truncated']

for i in range(6):
    t=titl[i]
    plt.subplot(2,3,i+1)
    plt.imshow(imglist[i])
    plt.title(t)
    plt.xticks([])
    plt.yticks([])
plt.show()
"""
