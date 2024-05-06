####################################################

# Load modules

import polars
import os
import numpy as np
import cellpose
from skimage import io
from skimage.filters import threshold_otsu
from skimage import measure
from matplotlib import pyplot as plt

####################################################

# Load masks
path = "data/masks"

files = os.listdir(path)

for i in files:
    mask = io.imread((os.path.join(path, i)))
    #plt.hist(mask)
    #plt.show()
    print(mask.shape)


    #thresh = threshold_otsu(mask)
    #binary = mask > thresh
    thresh = 0
    binary = mask > thresh

    # plot in same figure mask and binary
    # plt.subplot(1, 2, 1)
    # plt.imshow(mask)
    # plt.subplot(1, 2, 2)
    # plt.imshow(binary)
    # plt.show()

    # save binary image
    # io.imsave("data/binary/" + i, binary)

    l = measure.label(binary)
    props = measure.regionprops(l)

    # for p in props:
    #     print(f"Area: {p.area}, Perimeter: {p.perimeter}, label: {p.label}")
    #     print(f"Centroid: {p.centroid}, Bounding box: {p.bbox}")


####################################################
