import numpy as np
import matplotlib.pyplot as plt


def normalize (i):
  return (i - np.min(i)) / (np.max(i) - np.min(i))


def binarize (i, threshold = 0):
    return i > threshold


def plots(img, img2, img3):
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.subplot(1, 3, 2)
    plt.imshow(img2)
    plt.subplot(1, 3, 3)
    plt.imshow(img3)
