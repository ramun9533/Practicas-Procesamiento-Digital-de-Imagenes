from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from cvzone.HandTrackingModule import HandDetector
import cv2
import random
import time

Ui_MainWindow, QtBaseClass = uic.loadUiType("frm_PDI2024.ui")

class ppt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(detectionCon=0.8, maxHands=2)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._camara)
        self.timer.start(90)
        self.leyenda = QtWidgets.QLabel(self)
        self.jugador = QtWidgets.QLabel(self)
        self.maquina = QtWidgets.QLabel(self)
        self.imagen = QtWidgets.QPushButton(self)
        self.maquina_ppt = QtWidgets.QPushButton(self)

    def _c(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.label_2.setPixmap(pixmap)

    def _camara(self):
        global resultado
        resultado = "Mostrar la mano por favor"
        global usuario
        global maquina
        usuario = 0
        maquina = 0

        success, img = self.cap.read()
        hands, img = self.detector.findHands(img)
        if hands:
            hand1 = hands[0]
            fingers1 = self.detector.fingersUp(hand1)

            usuario1 = ""
            if fingers1 == [0, 0, 0, 0, 0]:
                usuario1 = "Piedra"
                pixmap = QPixmap("C:\\Users\\LYLYA\\piedra.png")
                self.jugador.setPixmap(pixmap)
            elif fingers1 == [0, 1, 1, 0, 0]:
                usuario1 = "Tijera"
                pixmap = QPixmap("C:\\Users\\LYLYA\\tijera.png")
                self.jugador.setPixmap(pixmap)
            elif fingers1 == [1, 1, 1, 1, 1]:
                usuario1 = "Papel"
                pixmap = QPixmap("C:\\Users\\LYLYA\\papel.png")
                self.jugador.setPixmap(pixmap)

            appt = random.randint(0, 2)
            maquina1 = ["Piedra", "Papel", "Tijera"][appt]

            if maquina1 == "Piedra" and usuario1 == "Papel":
                resultado = "Ganaste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\piedra.png")
                self.maquina.setPixmap(pixmap)
                usuario += 1
            elif maquina1 == "Papel" and usuario1 == "Tijera":
                resultado = "Ganaste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\papel.png")
                self.maquina.setPixmap(pixmap)
                usuario += 1
            elif maquina1 == "Tijera" and usuario1 == "Piedra":
                resultado = "Ganaste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\tijera.png")
                self.maquina.setPixmap(pixmap)
                usuario += 1
            elif maquina1 == "Papel" and usuario1 == "Piedra":
                resultado = "Perdiste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\papel.png")
                self.maquina.setPixmap(pixmap)
                maquina += 1
            elif maquina1 == "Tijera" and usuario1 == "Papel":
                resultado = "Perdiste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\tijera.png")
                self.maquina.setPixmap(pixmap)
                maquina += 1
            elif maquina1 == "Piedra" and usuario1 == "Tijera":
                resultado = "Perdiste"
                pixmap = QPixmap("C:\\Users\\LYLYA\\piedra.png")
                self.maquina.setPixmap(pixmap)
                maquina += 1
            elif maquina1 == usuario1:
                resultado = "Empate"

            self.leyenda.setText(resultado)
            time.sleep(2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.label_2.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ppt()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
