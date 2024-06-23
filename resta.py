import cv2
import numpy as np


# Función para cargar una imagen desde un archivo 4 > 
def cargar_imagen(ruta):
         imagen = cv2.imread(ruta)
    if imagen is None:
      print("No se pudo cargar la imagen desde la ruta:", ruta)
    return imagen

    

# Función para guardar una imagen en un archivo
def guardar_imagen(imagen, ruta):
         try:
        cv2.imwrite(ruta, imagen)
        print("Imagen guardada correctamente en:", ruta)
    except Exception as e:
        print("Error al guardar la imagen:", e)

# Función para sumar dos imágenes
def suma_imagenes (imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]): raise ValueError("Las imágenes deben tener las mismas dimensiones")
    suma = []
    suma imagen1+imagen2
    return suma
# Función para restar dos imágenes
def suma_images (imagen1, imagen2):

    if imagen1.shape != imagen2.shape:
    raise ValueError("Las imágenes deben tener las mismas dimensiones") 
# Inicializar una matriz para almacenar la resta de las imágenes 
    resta = np.zeros(imagen1.shape, dtype=np.float32)
# Realizar la resta elemento a elemento
    for i in range(imagen1.shape[0]):
        for j in range(imagen1.shape[1]):
            resta[i][j] = imagen1[i][j] + imagen2[i][j]
    return resta
# Función para restar dos imágenes
def resta_imagenes (imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len (imagen1[0]) != len(imagen2[0]): 
        raise ValueError("Las imágenes deben tener las mismas dimensiones") 
    resta = []
    resta imagen1-imagen2
    #print (resta)

    return resta

# Función para restar dos imágenes 
def resta_images (imagen1, imagen2):
    if imagen1.shape != imagen2.shape:
        raise ValueError("Las imágenes deben tener las mismas dimensiones") 
    # Inicializar una matriz para almacenar la resta de las imágenes 
    resta = np.zeros(imagen1.shape, dtype=np.float32)
# Realizar la resta elemento a elemento
    for i in range(imagen1.shape[0]):
        for j in range(imagen1.shape[1]):
-
            resta[i][j] = imagen1[i][j] - imagen2[i][j]
    return resta
# Cargar las imágenes
img = cv2.imread("tierra1.png",1) 
img1 = cv2.imread("espacio1.png",1) 
#img= cargar_imagen('tierra.jpg')
#img1= cargar_imagen('espacio.jpg') 
cv2.imshow('IMAGEN 1', img)
cv2.imshow('IMAGEN 2', img1)
cv2.waitKey(0)
#guardar_imagen (suma, "suma_imagenes.txt")
#Sumar las imagenes
suma = suma_imagenes (img, img1)
suma2 = suma_images (img, img1)
cv2.imshow('Suma', suma)
cv2.imshow('Suma 2', suma2) 
# Restar las imágenes
resta = resta_imagenes (img, img1) 
resta2 = resta_images (img, img1)
cv2.imshow('resta', resta)
cv2.imshow('resta 2', resta2)
cv2.waitKey(0)
#guardar_imagen (resta, "resta_imagenes.txt") 
cv2.destroyAllWindows()
