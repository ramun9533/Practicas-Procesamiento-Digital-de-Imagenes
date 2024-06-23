import numpy as np 
import cv2

# Función para convertir de RGB a RYB
def rgb_to_ryb(rgb):
    # Constantes para la conversión
    RYB_TO_RGB_MATRIX = np.array([[0.5141364, 0.3248667, 0.16036376],
                                  [0.265068,  0.67023428, 0.06409157],
                                  [0.0241188,  0.12475776, 0.85023467]])
    RGB_TO_RYB_MATRIX = np.linalg.inv(RYB_TO_RGB_MATRIX)

    # Convertir de RGB a RYB
    ryb = np.dot(RGB_TO_RYB_MATRIX, rgb)
    return ryb.astype(np.uint8)

# Cargar la imagen original
img = cv2.imread("lenna.png")

# Convertir la imagen a RYB
img_ryb = np.apply_along_axis(rgb_to_ryb, 2, img)

# Guardar la imagen convertida 
cv2.imwrite("imagen_ryb.jpg", img_ryb)
