import cv2
import numpy as np

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro de mediana con un tamaño de kernel de 3
median_image = median_filter(image, 3)

# Mostrar la imagen resultante
cv2.imshow("Median", median_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir la imagen resultante (opcional)
print(median_image)
