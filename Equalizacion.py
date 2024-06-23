import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen_gris = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar la equalización del histograma
imagen_equalizada = cv2.equalizeHist(imagen_gris)

# Mostrar la imagen original y la imagen equalizada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(imagen_equalizada, cmap='gray')
plt.title('Imagen Equalizada')

plt.show()
