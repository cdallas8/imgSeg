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

####################################################

# define data path

path = inputDir
files = os.listdir(path)

counter = 0

dfs = []

for i in files:
    if counter < 5:
        print("segmenting image: ", i)
        mask = cellSegmenter(os.path.join(path, i))
        print("creating df with cell morphology info & coordinates")
        df = cellProps(os.path.join(path, i), mask, os.path.join(path, i))
        dfs.append(df)
        counter += 1
    else:
        break

df = polars.concat(dfs)
print(df[1:10])

df.write_csv(graphDir + "/" + "CellMorph.csv")
