import cv2
import matplotlib.pyplot as plt

# Leer la imagen en modo gris (0 para escala de grises)
img = cv2.imread('shapes.png', 0)

if img is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Aplicar el filtro Canny
    img_canny = cv2.Canny(img, 100, 200)
    
    # Invertir la imagen utilizando el umbral binario inverso
    _, img_inversa = cv2.threshold(img_canny, 0, 255, cv2.THRESH_BINARY_INV)

    # Mostrar la imagen original y la imagen filtrada usando matplotlib
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Imagen original'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(img_inversa, cmap='gray')
    plt.title('Imagen filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()
