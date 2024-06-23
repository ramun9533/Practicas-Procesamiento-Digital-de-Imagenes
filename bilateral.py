import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en color o escala de grises
imagen = cv2.imread('lenna.png')

# Convertir la imagen a escala de grises si es en color
if len(imagen.shape) > 2:
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
else:
    imagen_gris = imagen

# Aplicar el filtrado bilateral
imagen_filtrada = cv2.bilateralFilter(imagen_gris, d=9, sigmaColor=75, sigmaSpace=75)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) if len(imagen.shape) > 2 else imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')
plt.title('Imagen Filtrada (Bilateral)')
plt.axis('off')

plt.show()
