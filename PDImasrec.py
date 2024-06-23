from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import numpy as np
import time

# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar archivos .ui
window = uic.loadUi("interface.ui")

filename = None
final_image = None

def cargarImagen():
    global filename
    filename, _ = QFileDialog.getOpenFileName(filter="Image (*.*)")
    if filename:
        imagen = cv2.imread(filename)
        setPhoto(imagen)
        rectangulos, imagen_con_rectangulos = detectarRectangulos(imagen)
        print("Rectángulos detectados:")
        for rectangulo in rectangulos:
            print("Coordenadas (x, y):", rectangulo[0], "Tamaño (ancho, alto):", rectangulo[1])

def detectarRectangulos(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # Establecer umbral en la imagen en escala de grises
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    rectangulos = []

    # Lista para almacenar nombres de formas
    for contour in contours: 
        # Aproximar el contorno a un polígono
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True) 

        # Verificar si el contorno es un rectángulo
        if len(approx) == 4:
            # Calcular el área del contorno
            area = cv2.contourArea(contour)
            # Definir el área mínima y máxima para los rectángulos
            min_area = 2500
            max_area = 3215
            # Verificar si el área del contorno está dentro del rango especificado
            if min_area < area < max_area:
                # Dibujar el contorno del rectángulo
                cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
                # Obtener las coordenadas y el tamaño del rectángulo
                x, y, w, h = cv2.boundingRect(contour)
                rectangulos.append(((x, y), (w, h)))

    # Mostrar la imagen después de dibujar los contornos
    setPhoto(image)

    return rectangulos, image

def setPhoto(image):
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
    imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
    window.label.setPixmap(QtGui.QPixmap.fromImage(imagen))

def salvarImagen():
    global final_image
    if final_image is not None:
        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        cv2.imwrite(f"pollito_{tiempo}.jpg", final_image)
        print("Imagen guardada")
    else:
        print("No se puede guardar la imagen porque no se ha procesado ninguna")

# Botones
window.cargar_imagen.clicked.connect(cargarImagen)
window.salir.clicked.connect(app.exit)
window.guardar.clicked.connect(salvarImagen)

# Ejecutable
window.show()
app.exec()
