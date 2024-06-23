import cv2
import numpy as np

def gaussian_filter(image, sigma):
    return cv2.GaussianBlur(image, (5, 5), sigma)

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro Gaussiano con sigma = 1
gaussian_image = gaussian_filter(image, 1)

# Mostrar la imagen resultante
cv2.imshow("Gaussian", gaussian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir la imagen resultante (opcional)
print(gaussian_image)
