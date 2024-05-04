####################################################

# Load modules

import cellpose
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

print(img.shape)
print(img.dtype)
print(np.max(img))
print(np.min(img))

#plt.imshow(img, cmap = "gray")
#plt.show()

normal_img = (img - np.min(img))/(np.max(img) - np.min(img))

print(normal_img.dtype)

model = models.Cellpose(gpu=False, model_type='cyto')
# alternative model type is 'nuclei'

masks, flows, styles, diams = model.eval(normal_img, diameter=None, channels=[0,0])
# channels = [0,0] gray scale image

#print(masks)
cellpose.io.save_masks(img, masks, flows, names, png = True)

####################################################
