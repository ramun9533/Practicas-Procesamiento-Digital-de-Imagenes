import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('lenna.png', 0)
img_erosionada = cv2.erode(img,kernel)

# Usar matplotlib para mostrar las imágenes
plt.subplot(1, 2, 1)
plt.title('Imagen original')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Imagen erosionada')
plt.imshow(img_erosionada, cmap='gray')

plt.show()
