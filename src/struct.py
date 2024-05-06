#############################################

# Load modules

from skimage import io

#############################################

# Define classes

class imgStruct:
    def init(self, imgPath, maskPath, img=None, mask=None):
        self.imgPath = imgPath
        self.maskPath = maskPath
        self.img = img
        self.mask = mask

    def loadImg(self, imgPath):
        self.img = io.imread(imgPath)
        self.imgPath = imgPath

    def loadMask(self, maskPath):
        self.mask = io.imread(maskPath)
        self.maskPath = maskPath

#############################################
