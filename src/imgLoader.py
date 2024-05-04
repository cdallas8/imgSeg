#############################################

# Load modules

from skimage import io

#############################################

# Declare path

img_path = "data/images/C22_s2_x1_y0_Fluorescence_638_nm_Ex.tiff"

#############################################

img = io.imread(img_path)

print(img.shape)

#############################################
