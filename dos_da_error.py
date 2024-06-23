import numpy as np 
import cv2
from colour.models import RGB_to_RYB  # Importa la función RGB_to_RYB específicamente

# Cargar la imagen original
img = cv2.imread("lenna.png")

# Convertir de RGB a RYB
img_ryb = RGB_to_RYB(img)

# Guardar la imagen convertida 
cv2.imwrite("imagen_ryb.jpg", img_ryb)  # Corregido el nombre de la variable img_ryb
