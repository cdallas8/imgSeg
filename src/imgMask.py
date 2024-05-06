####################################################

# Load modules

import cellpose
import polars
import os
import numpy as np
from skimage import io
from cellpose import models
from matplotlib import pyplot as plt

####################################################
# Define functions

# function to mask image with cellpose
# i = image, f = file name
def imgMask(i, f):
    model = models.Cellpose(gpu=False, model_type='cyto')

    chan = [0,0]
    masks, flows, styles, diams = model.eval(i, diameter=None, channels=chan)

    fig = plt.figure()
    cellpose.plot.show_segmentation(fig, i, masks, flows[0], channels = chan)
    plt.show()

    cellpose.io.save_masks(img, masks, flows, f, png = True, savedir = "data/masks")

####################################################

# Define path

path = "data/images"

####################################################

# Load data
files = os.listdir(path)

counter = 0

for i in files:
    if counter < 5:

        img = cellpose.io.imread((os.path.join(path, i)))
        imgMask(img, i)
        counter += 1
    else:
        break

####################################################
