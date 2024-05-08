####################################################

# import config file
from config.config import *

####################################################

# import modules
import os

####################################################

# import functions
from util.cellSegmenter import *
from util.cellMorph import *
from util.imgStats import *

####################################################

# define data path

path = inputDir
files = os.listdir(path)

####################################################

counter = 0

# initialize lists
dfs = []
stats = []

for i in files:
    if counter < 5:
        # calculate image stats
        s = imgStats(os.path.join(path, i))
        stats.append(s)
        # segment image
        print("segmenting image: ", i)
        mask = cellSegmenter(os.path.join(path, i))
        # cell morphology
        print("creating df with cell morphology info & coordinates")
        df = cellProps(os.path.join(path, i), mask, os.path.join(path, i))
        dfs.append(df)
        counter += 1
    else:
        break

# concatenate dataframes
s = polars.concat(stats)
df = polars.concat(dfs)

saveHist(s)

# write to csv
s.write_csv(graphDir + "/" + "imgStats.csv")
df.write_csv(graphDir + "/" + "CellMorph.csv")

####################################################
