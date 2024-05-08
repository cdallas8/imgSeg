####################################################

# import config file
from config.config import *

####################################################

# load modules

import os
import numpy as np
from skimage import io
import cellpose
from cellpose import models

####################################################

# import functions

from util.imgUtils import *

####################################################

# function to segment images & obtain masks with cellpose

def cellSegmenter(path, chan = [0,0], verbose = False):
    # load image
    img = io.imread(path)
    # normalize image
    img = normalize(img)
    # initialize model
    model = models.Cellpose(gpu=False, model_type='cyto')
    # segment image
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan)
    if verbose:
        fig = plt.figure()
        cellpose.plot.show_segmentation(fig, img, masks, flows[0], channels = chan)
        plt.show()
        cellpose.io.save_masks(img, masks, flows, os.path.basename(path), png = True, savedir = maskOutDir)
    else:
        cellpose.io.save_masks(img, masks, flows, os.path.basename(path), png = True, savedir = maskOutDir)
    # binarize mask
    mask = binarize(masks)
    # save mask
    io.imsave(binOutDir + "/" + os.path.splitext(os.path.basename(path))[0] + '.png', mask)
    if verbose:
        fig = plt.figure()
        plots(img, masks, mask)
        plt.show()
        # save plot
        plt.savefig(graphDir + "/" + os.path.splitext(os.path.basename(path))[0] + ".png")
    else:
        plots(img, masks, mask)
        # save plot
        plt.savefig(graphDir + "/" + os.path.splitext(os.path.basename(path))[0] + ".png")
    return mask

####################################################
