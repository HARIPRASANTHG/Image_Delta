import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

img = cv.imread("./f1_samp.png", cv.IMREAD_COLOR)
plt.imsave(img, 'foo.png')
