####################################################

# Load modules

import polars
import os
import numpy as np
import cellpose
from skimage import io
from skimage.filters import threshold_otsu
from skimage import measure, morphology
from matplotlib import pyplot as plt

####################################################

# Load masks
path = "data/masks"
path2 = "data/images"

files = os.listdir(path)
files2 = os.listdir(path2)

for i in range(len(files)):
    mask = io.imread((os.path.join(path, files[i])))
    img = io.imread((os.path.join(path2, files2[i])))
    print("files: ", files[i], files2[i])


# for i in files:
#     mask = io.imread((os.path.join(path, i)))
#     #plt.hist(mask)
#     #plt.show()
#     print(mask.shape)


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

    e = morphology.binary_erosion(binary)

    l = measure.label(e, background=0)
    props = measure.regionprops(l)

    print(f"Number of objects: {len(props)}")
    # plot one area and perimeter
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.subplot(1, 3, 2)
    plt.imshow(e)
    plt.subplot(1, 3, 3)
    plt.imshow(l == 1)
    plt.show()
    print(f"Area: {props[0].area}, Perimeter: {props[0].perimeter}")

    # for p in props:
    #     print(f"Area: {p.area}, Perimeter: {p.perimeter}, label: {p.label}")
    #     print(f"Centroid: {p.centroid}, Bounding box: {p.bbox}")


####################################################
