####################################################

# Load modules

import cellpose
import polars
import os
import numpy as np
from skimage import io
from cellpose import models
from matplotlib import pyplot as plt
import pickle


####################################################
# Define functions

class imgStruct:

    def __init__(self, imgPath, maskPath, img, mask):
        self.imgPath = imgPath
        self.maskPath = maskPath
        self.img = img
        self.mask = mask



# function to mask image with cellpose
# i = image, f = file name
def imgSeg(folder, c = [0,0]):

    maskDir = "data/binary"

    # Load data - a sample of 5 images
    imgPath = [os.path.join(folder, i) for i in os.listdir(folder)][:5]
    img = [cellpose.io.imread(i) for i in imgPath]

    # initialize model
    model = models.Cellpose(gpu=False, model_type='cyto')

    # initialize list
    seg = []

    # segment images
    for i, p in zip(img, imgPath):
        print("segmenting image: ", p)
        masks, flows, styles, diams = model.eval(i, diameter=None, channels=c)

        # save mask & path
        # cellpose.io.save_masks(img, masks, flows, p, png = True, savedir = maskDir)
        # sp = os.path.join(maskDir, os.path.basename(p).replace(".tiff", "_cp_mask.png"))

        # apply threshold
        thresh = 0
        binary = masks > thresh
        io.imsave(os.path.join(maskDir, os.path.basename(p).replace(".tiff", "mask_binary.png")), binary)
        bp = os.path.join(maskDir, os.path.basename(p).replace(".tiff", "mask_binary.png"))

        # create imgStruct object & append
        i = imgStruct(p, bp, i, binary)
        seg.append(i)
        print("segmentation complete")
    return seg

####################################################

# Define path
path = "data/images"

# Run function
vc = imgSeg(path)

# Save object
print("saving object")
with open("data/masks.pkl", "wb") as f:
    pickle.dump(vc, f)
print("object saved")

####################################################

# Plot img and mask side by side

fig, ax = plt.subplots(5, 2, figsize = (10, 20))

for i in range(5):

    img = vc[i].img
    mask = vc[i].mask

    ax[i, 0].imshow(img, cmap = "gray")
    ax[i, 1].imshow(mask, cmap = "gray")

plt.show()

#  save plot
plt.savefig("data/segmentation.png")
plt.close()

####################################################
