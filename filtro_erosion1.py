import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('lenna.png', 0)
img_erosionada = cv2.erode(img,kernel)

# Guardar las imágenes en el disco
cv2.imwrite('imagen_original.jpg', img)
cv2.imwrite('imagen_erosionada.jpg', img_erosionada)
