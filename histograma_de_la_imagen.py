import cv2
import matplotlib.pyplot as plt

def calcular_histograma(imagen):
    # Convertir la imagen a escala de grises si es a color
    if len(imagen.shape) > 2:
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    else:
        imagen_gris = imagen
    
    # Calcular el histograma utilizando cv2.calcHist()
    histograma = cv2.calcHist([imagen_gris], [0], None, [256], [0, 256])
    return histograma

def graficar_histograma(histograma):
    plt.figure()
    plt.title("Histograma de la Imagen")
    plt.xlabel("Intensidad de Píxeles")
    plt.ylabel("Número de Píxeles")
    plt.plot(histograma, color='black')
    plt.xlim([0, 256])
    plt.show()

# Cargar la imagen
imagen = cv2.imread('lenna.png')

# Calcular el histograma
histograma = calcular_histograma(imagen)

# Graficar el histograma
graficar_histograma(histograma)
