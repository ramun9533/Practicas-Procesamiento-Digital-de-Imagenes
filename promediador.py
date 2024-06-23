import numpy as np
from scipy.ndimage import convolve
import cv2

def averaging_filter(image):
    kernel = np.ones((3, 3)) / 9
    return convolve(image, kernel)

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro de promedio
averaged_image = averaging_filter(image)

# Mostrar la imagen resultante
cv2.imshow("Averaged Image", averaged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir la imagen resultante
print(averaged_image)
