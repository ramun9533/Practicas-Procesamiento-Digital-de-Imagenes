import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('lenna.png', img)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color = 'gray')

plt.xlabel('intensidad de luminusidad')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()