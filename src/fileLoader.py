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

def normalize (i):
  return (i - np.min(i)) / (np.max(i) - np.min(i))

def stats(i):
    m = np.mean(i)
    s = np.std(i)
    return m, s

def statsToDf(f, m, s):
    return polars.DataFrame({"file": f, "mean": m, "std": s})

def saveHist(df):
    plt.hist(df["mean"])
    plt.savefig("mean_hist.png")
    plt.hist(df["std"])
    plt.savefig("std_hist.png")

####################################################

# Define path

path = "data/images"

####################################################

# Load data
files = os.listdir(path)

means = []
stds = []

for i in files:
    img = cellpose.io.imread((os.path.join(path, i)))
    n_img = normalize(img)
    m, s = stats(n_img)
    means.append(m)
    stds.append(s)

df = statsToDf(files, means, stds)
print(df)
#saveHist(df)


# Create a dataframe
#df = polars.DataFrame({"file": files, "mean": means, "std": stds})

# Visualize the data
#print(df)

#plt.hist(means)
#plt.show()
#plt.hist(stds)
#plt.show()

####################################################
