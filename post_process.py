import cv2
from PIL import Image
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

test = cv2.imread('disp.png')
# print test
test = np.power(test, 0.2).astype(np.float)
print test
plt.imshow(test)
plt.axis('off')
plt.savefig('result.png')
