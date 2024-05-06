####################################################

from functions import *


####################################################

# Define path

path = "data/images"

####################################################

# Load data

files = os.listdir(path)

counter = 0

dfs = []

for i in files:
    if counter < 5:
        print("segmenting image: ", i)
        mask = imgSegmentation(os.path.join(path, i), chan = [0,0])
        print("creating dataframe with cell coordinates")
        df = cellProps(os.path.join(path, i), mask, os.path.join(path, i))
        dfs.append(df)
        counter += 1
    else:
        break

df = polars.concat(dfs)
print(df[1:10])

df.write_csv("out/segmented_cells.csv")
