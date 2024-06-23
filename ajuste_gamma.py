import cv2
import numpy as np
import matplotlib.pyplot as plt

def ajuste_gamma(imagen, gamma):
    # Normalizar los valores de los píxeles entre 0 y 1
    imagen_normalizada = imagen / 255.0
    
    # Aplicar la corrección gamma
    imagen_corregida = np.power(imagen_normalizada, gamma)
    
    # Escalar de nuevo a valores de píxeles entre 0 y 255
    imagen_corregida = np.uint8(imagen_corregida * 255)
    
    return imagen_corregida

# Cargar la imagen en escala de grises
imagen_gris = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Definir los valores de gamma a probar
valores_gamma = [0.5, 1.0, 1.5, 2.0, 2.5]

# Mostrar la imagen original y las imágenes corregidas con diferentes valores de gamma
plt.figure(figsize=(15, 5))
plt.subplot(1, len(valores_gamma) + 1, 1)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Original')

for i, gamma in enumerate(valores_gamma):
    imagen_corregida = ajuste_gamma(imagen_gris, gamma)
    plt.subplot(1, len(valores_gamma) + 1, i + 2)
    plt.imshow(imagen_corregida, cmap='gray')
    plt.title('Gamma = {}'.format(gamma))

plt.show()
