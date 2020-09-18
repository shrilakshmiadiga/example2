import numpy as np
import cv2
from PIL import Image


from skimage.filters import threshold_otsu
from skimage import measure
from scipy import ndimage
from skimage import exposure

def get1Maximum2DRegion(max_second_binary):
    """Get the largest 2D region from multiple 2D regions"""
    
    new_binary = np.zeros(max_second_binary.shape, dtype = np.float32)
    for i in range(max_second_binary.shape[0]):
        xy_binary = max_second_binary[i,:,:]
        xy_labels = measure.label(xy_binary)
        xy_props = measure.regionprops(xy_labels)
        xy_areas = [prop.area for prop in xy_props]
        #print i, xy_areas_1
        if xy_areas == []:
            continue
        else:
            max_area_label = 1 + np.argmax(xy_areas)
            new_binary[i,:,:] = np.float32(xy_labels == max_area_label)
            
    return new_binary


img=cv2.imread('C:/Users/dell/Desktop/LIDC/segmented/testing/LIDC_2,4.png')
ret, bw_img = cv2. threshold(img,127,255,cv2. THRESH_BINARY)
#cv2. imshow("Binary Image",bw_img)
cv2. waitKey(0)
cv2. destroyAllWindows()

imge=get1Maximum2DRegion(bw_img)
cv2.imshow('image',imge)
