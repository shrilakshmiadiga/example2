
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
from skimage import measure
import matplotlib.pyplot as plt

original = imread('C:/Users/dell/Desktop/LIDC/segmented/training/LIDC_1,2.png')
blurred = gaussian(original, sigma=.8)
binary = blurred > threshold_otsu(blurred)
labels = measure.label(binary)

plots = {'Original': original, 'Blurred': blurred, 
         'Binary': binary, 'Labels': labels}
fig, ax = plt.subplots(1, len(plots))
for n, (title, img) in enumerate(plots.items()):
    cmap = plt.cm.gnuplot if n == len(plots) - 1 else plt.cm.gray
    ax[n].imshow(img, cmap=cmap)
    ax[n].axis('off')
    ax[n].set_title(title)
plt.show(fig)

print("----------------AREA----------------------")
print()
props = measure.regionprops(labels)
for prop in props:
    print('Label: {} >> Object size: {}'.format(prop.label, prop.area))
print()
print()

print("----------------CENTROID----------------------")
print()
for prop in props:
    print('Label: {} >> centroid: {}'.format(prop.label, prop.centroid))
print()
print()

print("----------------MAJOR AXIS LENGTH----------------------")
print()
for prop in props:
    print('Label: {} >> major axis: {}'.format(prop.label, prop.major_axis_length))
print()
print()

print("----------------MINOR AXIS LENGTH----------------------")
print()
for prop in props:
    print('Label: {} >> minor axis: {}'.format(prop.label, prop.minor_axis_length))





