####################################################

# import config file
from src.config.config import *

####################################################

# import modules
import os

####################################################

# import functions
from src.util.cellSegmenter import *
from src.util.cellMorph import *

####################################################

# define data path

path = inputDir
files = os.listdir(path)
print(files[1:5])
