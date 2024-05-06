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

dfs = []

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

    cell_props = measure.regionprops(l)
    cell_locs = [prop.centroid for prop in cell_props]

    # flatten cell_locs
    coordinates = np.array(cell_locs).flatten()
    #print(f"Coordinates: {coordinates}")

    df = polars.DataFrame({"file": files2[i], "x": coordinates[0::2], "y": coordinates[1::2]})
    dfs.append(df)

    # plot one area and perimeter
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.subplot(1, 3, 2)
    plt.imshow(e)
    plt.subplot(1, 3, 3)
    plt.imshow(l == 13)
    plt.show()
    print(f"Area: {cell_props[13].area}, Perimeter: {cell_props[13].perimeter}")


df_complete = polars.concat(dfs)
print(df_complete[-15:])


    # for p in props:
    #     print(f"Area: {p.area}, Perimeter: {p.perimeter}, label: {p.label}")
    #     print(f"Centroid: {p.centroid}, Bounding box: {p.bbox}")

####################################################
