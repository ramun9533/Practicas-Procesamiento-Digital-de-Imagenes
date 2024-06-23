import cv2
import numpy as np

def composicion_imagenes():
    img1 = cv2.imread('lenna.png', 1)
    img2 = cv2.imread('lenna.png', 1)
    img = cv2.addWeighted(img1, 0.4, img2, 0.8, 0)
    cv2.imshow('Composicion imagenes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crear_imagen_color():
    ancho, alto = 300, 300
    img = np.ones((alto, ancho, 3), np.uint8)
    img[:] = (255, 0, 0)
    cv2.imshow('Imagen color', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crear_imagen_negra():
    ancho, alto = 300, 300
    img = np.zeros((alto, ancho), np.uint8)
    cv2.imshow('Imagen negra', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mostrar_canales(imagen):
    img = cv2.imread(imagen, 1)
    img_azul, img_verde, img_roja = cv2.split(img)
    cv2.imshow('Azul', img_azul)
    cv2.imshow('Verde', img_verde)
    cv2.imshow('Roja', img_roja)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crear_rejilla(color=(0, 0, 255), step=50):
    ancho, alto = 300, 300
    img = np.ones((alto, ancho, 3), np.uint8) * 255
    for x in range(ancho):
        for y in range(alto):
            if x % step == 0 or y % step == 0:
                img[y, x] = color
    cv2.imshow('Rejilla', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def encontrar_patron():
    color = (0, 155, 255)
    grosor = 2
    img = cv2.imread('lenna.png')
    patron = cv2.imread('lenna.png')
    res = cv2.matchTemplate(img, patron, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    esq_sup_izq = min_loc
    alto, ancho, _ = patron.shape
    esq_inf_der = (esq_sup_izq[0] + ancho, esq_sup_izq[1] + alto)
    cv2.rectangle(img, esq_sup_izq, esq_inf_der, color, grosor)
    cv2.imshow("Imagen original", img)
    cv2.imshow('Patron', patron)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def informacion_imagen():
    img = cv2.imread('lenna.png', 1)
    tamanio = img.size
    alto, ancho, canales = img.shape
    tipo = img.dtype
    print("Tamaño:", tamanio, "bytes")
    print("Ancho:", ancho, "píxeles")
    print("Alto:", alto, "píxeles")
    print("No canales:", canales)
    print("Tipo:", tipo)

def menu():
    print("Menú:")
    print("1. Composición de imágenes")
    print("2. Crear imagen de color")
    print("3. Crear imagen negra")
    print("4. Mostrar canales de una imagen")
    print("5. Crear rejilla")
    print("6. Encontrar patrón")
    print("7. Información de la imagen")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        composicion_imagenes()
    elif opcion == '2':
        crear_imagen_color()
    elif opcion == '3':
        crear_imagen_negra()
    elif opcion == '4':
        imagen = input("Ingrese la ruta de la imagen: ")
        mostrar_canales(imagen)
    elif opcion == '5':
        crear_rejilla()
    elif opcion == '6':
        encontrar_patron()
    elif opcion == '7':
        informacion_imagen()
    elif opcion == '0':
        print("Saliendo del programa...")
        return
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

    menu()

# Ejecutar el menú
menu()
