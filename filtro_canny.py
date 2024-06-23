import cv2
import matplotlib.pyplot as plt

# Leer la imagen en modo gris (0 para escala de grises)
img = cv2.imread('shapes.png', 0)

if img is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Aplicar el filtro Canny
    img_canny = cv2.Canny(img, 100, 200)
    
    # Mostrar la imagen filtrada usando matplotlib
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Imagen original'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(img_canny, cmap='gray')
    plt.title('Imagen filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()
