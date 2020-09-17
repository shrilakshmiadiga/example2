import matplotlib.image as mpimg
import os

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = mpimg.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images
folder="F:\demoimages"
load_images(folder)
