from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open("/home/hari/Desktop/ImageComp/f1_samp.png"))
print(repr(img))

imgplot = plt.imshow(img)
plt.show()
