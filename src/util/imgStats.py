####################################################

# import config file
from config.config import *

####################################################

# load modules
from skimage import io

####################################################

# import functions

from util.imgUtils import *

####################################################

def imgStats(path, verbose = False):
    # load image
    img = io.imread(path)
    # normalize image
    img = normalize(img)
    # img stats (mean, std)
    m, s = stats(img)
    # save stats
    df = statsToDf(path, m, s)
    return df

####################################################

def saveHist(df):
    plt.hist(df["mean"])
    plt.savefig(plotDir + "/" + "mean_hist.png")
    plt.hist(df["std"])
    plt.savefig(plotDir + "/" + "std_hist.png")

####################################################
