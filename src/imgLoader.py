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

# Declare path

img_path = "data/images/C22_s2_x1_y0_Fluorescence_638_nm_Ex.tiff"

####################################################

names = "test"
# img = io.imread(img_path, as_gray=True, dtype = "uint8")
img = cellpose.io.imread(img_path)

#plt.imshow(img, cmap = "gray")
#plt.show()

normal_img = (img - np.min(img))/(np.max(img) - np.min(img))

print(normal_img.dtype)
print(np.mean(normal_img))
print(np.max(normal_img))

#plt.hist(normal_img)
#plt.show()

model = models.Cellpose(gpu=False, model_type='cyto')
# alternative model type is 'nuclei'

chan = [0,0]
masks, flows, styles, diams = model.eval(normal_img, diameter=None, channels=chan)
# channels = [0,0] gray scale image

plt.hist(masks)
plt.show()

print(masks.shape)
print(flows[0].shape)
print(masks[0].shape)

fig = plt.figure()
cellpose.plot.show_segmentation(fig, normal_img, masks, flows[0], channels = chan)
plt.show()

cellpose.io.save_masks(img, masks, flows, names, png = True)

####################################################
