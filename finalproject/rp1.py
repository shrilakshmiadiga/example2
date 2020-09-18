
from skimage import graph, data,segmentation
from matplotlib import pyplot as plt
import numpy as np

#creating a segmented image
im = data.immunohistochemistry()
seg = segmentation.felzenszwalb(im, scale=200, sigma=0.7, min_size=50)
BW = segmentation.find_boundaries(seg)
im[BW==1]=0
plt.imshow(im)
plt.show()

from skimage.measure import regionprops
Props = regionprops(seg,['Area'])

#here is the code for creating the regionprops image
labels = np.unique(seg) #a vector of label vals
PropIM = np.zeros_like(seg) # allocated blank array
for label in labels:
    propval=Props[label-1]['Area'] 
    PropIM[seg==label]=propval

#for visualising with segment boundaries
PropIM[BW==1]=0

plt.imshow(PropIM, vmin=PropIM.min(), vmax=PropIM.max())
plt.colorbar()
plt.show()
