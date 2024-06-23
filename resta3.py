import cv2
import numpy as np

# Función para cargar una imagen desde un archivo
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

# Función para multiplicar dos imágenes
def multi_imagenes (imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]):
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    multi = []
    multi = imagen1*imagen2
    return multi
# Función para dividir dos imágenes
def div_imagenes (imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]):
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    div = []
    div=imagen1/imagen2
    return div



# Función para sumar dos imágenes
def suma_imagenes(imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]):
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    suma = imagen1 + imagen2
    return suma

# Función para restar dos imágenes
def resta_imagenes(imagen1, imagen2):
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]):
        raise ValueError("Las imágenes deben tener las mismas dimensiones")
    resta = imagen1 - imagen2
    return resta

# Cargar las imágenes
img = cv2.imread("tierra1.png", 1)
img1 = cv2.imread("espacio1.png", 1)

cv2.imshow('IMAGEN 1', img)
cv2.imshow('IMAGEN 2', img1)
cv2.waitKey(0)

m = multi_imagenes (img, img1)
cv2.imshow('Multiplicacion', m)
division = div_imagenes (img, img1)
cv2.imshow('Division', division)
cv2.waitKey(0)



# Sumar las imágenes
suma = suma_imagenes(img, img1)
cv2.imshow('Suma', suma)

# Restar las imágenes
resta = resta_imagenes(img, img1)
cv2.imshow('Resta', resta)

cv2.waitKey(0)
cv2.destroyAllWindows()
