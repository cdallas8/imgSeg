####################################################

# import config file
from config.config import *

####################################################

# load modules

import numpy as np
import polars
from skimage import io, measure, morphology
from matplotlib import pyplot as plt

####################################################

# import functions

from util.imgUtils import *

####################################################

# function to extract cell morphology from binary masks

def cellProps(img, mask, path, verbose = False):
    # erode mask
    e = morphology.binary_erosion(mask)
    # label mask
    labeled_mask = measure.label(mask)

    if verbose:
        plots(io.imread(img), mask, labeled_mask == 1)
        plt.show()
        plt.savefig(laOutDir + "/" + os.path.splitext(os.path.basename(path))[0] + ".png")
    else:
        plots(io.imread(img), mask, labeled_mask == 1)
        plt.savefig(laOutDir + "/" + os.path.splitext(os.path.basename(path))[0] + ".png")

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
