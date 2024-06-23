import numpy as np
import cv2

def max_min_filter(image, kernel_size, operation):
    output = np.zeros_like(image)
    padded_image = np.pad(image, kernel_size // 2, mode='edge')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel_size, j:j+kernel_size]
            if operation == 'max':
                output[i, j] = np.max(region)
            elif operation == 'min':
                output[i, j] = np.min(region)
    return output

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Comprobar si la imagen se ha cargado correctamente
if image is None:
    raise FileNotFoundError("La imagen no se encontró. Verifica la ruta.")

# Aplicar el filtro de máximo con un tamaño de kernel de 3
max_image = max_min_filter(image, 3, 'max')

# Aplicar el filtro de mínimo con un tamaño de kernel de 3
min_image = max_min_filter(image, 3, 'min')

# Imprimir los resultados de los filtros
print("Max Filter Result:\n", max_image)
print("Min Filter Result:\n", min_image)
