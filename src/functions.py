####################################################

# Load modules

import cellpose
from cellpose import models
from skimage import io, measure, morphology
import os
import numpy as np
import polars
from matplotlib import pyplot as plt

####################################################

# Define functions

def normalize (i):
  return (i - np.min(i)) / (np.max(i) - np.min(i))


def binarize (i, threshold = 0):
    return i > threshold


def plots(img, mask, mask2, plotName):
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.subplot(1, 3, 2)
    plt.imshow(mask)
    plt.subplot(1, 3, 3)
    plt.imshow(mask2)
    plt.show()
    plt.savefig("out/" + plotName + ".png")


def imgSegmentation(path, chan = [0,0]):
    # load image
    img = io.imread(path)
    # normalize image
    img = normalize(img)
    # initialize model
    model = models.Cellpose(gpu=False, model_type='cyto')
    # segment image
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan)
    # binarize mask
    mask = binarize(masks)

    plots(img, masks, mask, "masks")

    return mask


def cellProps(i, mask, path):
    # erode mask
    e = morphology.binary_erosion(mask)
    # label mask
    labeled_mask = measure.label(mask)
    # plot images
    plots(io.imread(i), mask, labeled_mask == 1, "labeled_mask")
    # get cell properties
    cell_props = measure.regionprops(labeled_mask)
    # get number of cells
    cells = len(cell_props)
    # get area of cells
    cell_area = [prop.area for prop in cell_props]
    # get perimeter of cells
    cell_perimeter = [prop.perimeter for prop in cell_props]
    # get cell coordinates
    cell_coords = [prop.centroid for prop in cell_props]
    coordinates = np.array(cell_coords).flatten()
    # create dataframe
    df = polars.DataFrame({"file": path, "num_cells": cells, "area": cell_area, "perimeter": cell_perimeter, "x": coordinates[0::2], "y": coordinates[1::2]})

    return df






####################################################
