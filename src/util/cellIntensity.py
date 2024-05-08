####################################################

# import config file
from config.config import *

####################################################

# load modules
import numpy as np
import polars
import matplotlib.pyplot as plt

####################################################

def intensityCalculator(path, img, mask, verbose = False):

    roi = img * mask

    mean = np.mean(roi)
    max = np.max(roi)
    min = np.min(roi)

    if verbose:
        plt.figure()
        plt.hist(roi.flatten(), bins = 256, range = (0, 256))
        plt.show()

    df = polars.DataFrame({"file": path, "mean": mean, "max": max, "min": min})

    return df

####################################################
