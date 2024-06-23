import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en color
imagen_color = cv2.imread('lenna.png')

# Convertir la imagen de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

# Guardar la imagen original
cv2.imwrite('imagen_original.jpg', cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB))

# Mostrar la imagen original
plt.figure(figsize=(8, 8))
plt.imshow(imagen_rgb)
plt.title('Imagen Original')
plt.axis('off')
plt.show()

# Cambiar el espacio de color de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2HSV)

# Ajustar los canales de color individualmente (por ejemplo, aumentar la saturación)
aumento_saturacion = 1.5
imagen_hsv[:, :, 1] = imagen_hsv[:, :, 1] * aumento_saturacion

# Convertir la imagen de HSV a RGB
imagen_transformada = cv2.cvtColor(imagen_hsv, cv2.COLOR_HSV2RGB)

# Guardar la imagen transformada
cv2.imwrite('imagen_transformada.jpg', cv2.cvtColor(imagen_transformada, cv2.COLOR_RGB2BGR))

# Mostrar la imagen transformada
plt.figure(figsize=(8, 8))
plt.imshow(imagen_transformada)
plt.title('Imagen Transformada')
plt.axis('off')
plt.show()
