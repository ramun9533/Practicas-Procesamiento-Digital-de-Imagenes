import numpy as np
from scipy.stats import mode
import cv2

def mode_filter(image, kernel_size):
    output = np.zeros_like(image)
    padded_image = np.pad(image, kernel_size // 2, mode='edge')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel_size, j:j+kernel_size].flatten()
            try:
                mode_value = mode(region, axis=None)[0][0]
            except IndexError:
                mode_value = region[len(region) // 2]  # Si falla, elige el valor central
            output[i, j] = mode_value
    return output

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Comprobar si la imagen se ha cargado correctamente
if image is None:
    raise FileNotFoundError("La imagen no se encontró. Verifica la ruta.")

# Aplicar el filtro de moda con un tamaño de kernel de 3
mode_image = mode_filter(image, 3)

# Mostrar la imagen resultante
cv2.imshow("Mode Filtered Image", mode_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir la imagen resultante (opcional)
print(mode_image)
