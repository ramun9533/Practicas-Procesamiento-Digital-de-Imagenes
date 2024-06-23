import numpy as np
import cv2

# Cargar la imagen original
img = cv2.imread("lenna.png")

# Convertir de BGR a RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convertir de RGB a HSV
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

# Cambiar el matiz de la imagen
hue = 0.5  # 0 a 1 para cambiar los colores, 0.5 para invertirlos
img_hsv[..., 0] = hue * 255

# Convertir de HSV a RGB
img_rgb_final = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

# Guardar la imagen convertida
cv2.imwrite("tres.jpg", img_rgb_final)
