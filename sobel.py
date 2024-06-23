import numpy as np
from scipy.ndimage import convolve
import cv2

def sobel_filter(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    grad_x = convolve(image, sobel_x)
    grad_y = convolve(image, sobel_y)
    grad = np.hypot(grad_x, grad_y)
    return grad

def normalize_image(image):
    image = image - np.min(image)
    image = image / np.max(image)
    image = (image * 255).astype(np.uint8)
    return image

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro Sobel
sobel_image = sobel_filter(image)

# Normalizar la imagen resultante para que sea adecuada para mostrar
sobel_image = normalize_image(sobel_image)

# Mostrar la imagen con el filtro aplicado
cv2.imshow("Sobel Image", sobel_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir la imagen con el filtro aplicado
print(sobel_image)
