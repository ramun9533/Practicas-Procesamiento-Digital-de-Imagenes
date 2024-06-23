import cv2
import numpy as np
# Leer la imagen
img = cv2.imread('lenna.png')
# Crear el kernel de promedio
kernel = np.ones((5,5),np.float32)/25
# Aplicar el filtro de promedio
filtered_img = cv2.filter2D(img, -1, kernel)
# Mostrar la imagen filtrada
cv2.imshow('Filtered Image&#39', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()