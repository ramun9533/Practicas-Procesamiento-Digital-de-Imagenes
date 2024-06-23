import cv2 
import numpy as np 
from tkinter import Tk, filedialog

# Crear una ventana Tkinter oculta para manejar el diálogo de selección de archivo
root = Tk()
root.withdraw()

# Pedir al usuario que seleccione un archivo de imagen
file_path = filedialog.askopenfilename(title="Seleccione una imagen", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")])

if file_path:
    # Leer la imagen seleccionada
    img = cv2.imread(file_path)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Establecer un umbral en la imagen en escala de grises
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

    # Encontrar contornos en la imagen umbralizada
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    # Lista para almacenar los nombres de las formas
    for contour in contours: 
        # Aproximar el contorno a un polígono
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True) 

        # Verificar si el contorno es un rectángulo
        if len(approx) == 4:
            # Calcular el área del contorno
            area = cv2.contourArea(contour)
            # Definir el área mínima y máxima para los rectángulos
            min_area = 500
            max_area = 5000
            # Verificar si el área del contorno está dentro del rango especificado
            if min_area < area < max_area:
                # Dibujar el contorno del rectángulo
                cv2.drawContours(img, [contour], 0, (0, 255, 0), 2) 

    # Mostrar la imagen después de dibujar los contornos
    cv2.imshow('Rectángulos', img) 

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
