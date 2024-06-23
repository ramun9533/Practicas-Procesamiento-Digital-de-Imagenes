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

# Función para sumar dos imágenes
def suma_imagenes(imagen1, imagen2):
    if imagen1.shape != imagen2.shape:
        raise ValueError("Las imágenes deben tener las mismas dimensiones")

    suma = cv2.add(imagen1, imagen2)
    return suma

# Función para restar dos imágenes
def resta_imagenes(imagen1, imagen2):
    if imagen1.shape != imagen2.shape:
        raise ValueError("Las imágenes deben tener las mismas dimensiones")

    resta = cv2.subtract(imagen1, imagen2)
    return resta

# Cargar las imágenes
img1 = cargar_imagen("tierra1.png")
img2 = cargar_imagen("espacio1.png")

if img1 is not None and img2 is not None:
    cv2.imshow('IMAGEN 1', img1)
    cv2.imshow('IMAGEN 2', img2)
    cv2.waitKey(0)

    # Sumar las imágenes
    suma = suma_imagenes(img1, img2)
    cv2.imshow('Suma', suma)

    # Restar las imágenes
    resta = resta_imagenes(img1, img2)
    cv2.imshow('Resta', resta)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
