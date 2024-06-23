from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
import cv2
import random
import time
from ppt_ui import Ui_Dialog

class ppt(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camara = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sofia_camara)
        self.timer.start(90)
        self.leyenda = QtWidgets.QLabel(self)
        self.jugador = QtWidgets.QTextEdit(self)
        self.maquina = QtWidgets.QTextEdit(self)

    def sofia_camara(self):
        global resultado
        resultado = "Mostrar la mano por favor"
        global usuario
        global maquina
        usuario = 0
        maquina = 0

        success, img = self.camara.read()

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar umbral adaptativo para obtener una imagen binaria
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        # Encontrar contornos en la imagen binaria
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Encontrar el contorno de la mano más grande
        if contours:
            hand_contour = max(contours, key=cv2.contourArea)

            # Calcular el centro de la mano
            M = cv2.moments(hand_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Dibujar un círculo en el centro de la mano
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)

        # Mostrar la imagen en un QLabel
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(convertToQtFormat)
        self.video.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ppt()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
