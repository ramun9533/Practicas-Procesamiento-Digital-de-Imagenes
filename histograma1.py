import cv2
import numpy as np
from matplotlib import pyplot as plt 


img1 = cv2.imread('lenna.png')
cv2.imshow('lenna.png', img1)
color = ('b', 'g', 'r')

for i, c in enumerate(color):
    hist1 = cv2.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(hist1, color = c)
    plt.xlim([0, 256])
plt.show()

cv2.destroyAllWindows() 
