from PyQt6 import uic, QtCore, QtGui,QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from cvzone.HandTrackingModule import HandDetector
import cv2
import random
import time

#appt= random.randrange(0, 3)

Ui_MainWindow, QtBaseClass = uic.loadUiType("ppt.ui")

class ppt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.camara = cv2.VideoCapture(0)
        self.detector = HandDetector(detectionCon=0.8, maxHands=2)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sofia_camara)
        self.timer.start(90)
        self.leyenda = QtWidgets.QLabel(self)
        self.jugador= QtWidgets.QTextEdit(self)
        self.maquina= QtWidgets.QTextEdit(self)

    def sofia_camara(self):
        global resultado
        resultado = "Mostrar la mano por favor"
        global usuario
        global maquina
        usuario=0
        maquina=0
        
        success, img = self.camara.read()
        hands, img = self.detector.findHands(img)

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"] 
            bbox1 = hand1["bbox"] 
            centerPoint1 = hand1['center'] 
            handType1 = hand1["type"]  
            fingers1 = self.detector.fingersUp(hand1)

            t = cv2.waitKey(0)
                
            usuario1=""
            if(fingers1[0]==0 and fingers1[1]==0 and fingers1[2]==0 and fingers1[3]==0 and fingers1[4]==0 ):
                usuario1="Piedra"
                pixmap = QPixmap("img\piedra.png")
                self.jugador_ppt.setPixmap(pixmap)
            if(fingers1[0]==0 and fingers1[1]==1 and fingers1[2]==1 and fingers1[3]==0 and fingers1[4]==0 ):
                usuario1="Tijera"
                pixmap = QPixmap("img\ijeras.png")
                self.jugador_ppt.setPixmap(pixmap)
            if(fingers1[0]==1 and fingers1[1]==1 and fingers1[2]==1 and fingers1[3]==1 and fingers1[4]==1 ):
                usuario1="Papel"
                pixmap = QPixmap("img\papel.png")
                self.jugador_ppt.setPixmap(pixmap)

            appt= random.randint(0,2)
            maquina1 = ""
            if appt== 0:
                maquina1 = "Piedra"
            elif appt== 1:
                maquina1 = "Papel"
            elif appt== 2:
                maquina1 = "Tijera"


            if maquina1 == "Piedra" and usuario1 =="Papel":
                resultado="Ganaste"
                pixmap = QPixmap("img\piedra.png")
                self.maquina_ppt.setPixmap(pixmap)
                usuario=usuario+1
            elif maquina1 == "Papel" and usuario1 == "Tijera":
                resultado="Ganaste"
                pixmap = QPixmap("img\papel.png")
                self.maquina_ppt.setPixmap(pixmap)
                usuario=usuario+1
            elif maquina1 == "Tijera" and usuario1 == "Piedra":
                resultado="Ganaste"
                pixmap = QPixmap("img\ijeras.png")
                self.maquina_ppt.setPixmap(pixmap)
                usuario=usuario+1            
            elif maquina1 == "Papel" and usuario1 == "Piedra":
                resultado="perdiste"
                pixmap = QPixmap("img\papel.png")
                self.maquina_ppt.setPixmap(pixmap)
                maquina=maquina+1
            elif maquina1 == "Tijera" and usuario1 =="Papel":
                resultado="perdiste"
                pixmap = QPixmap("img\ijeras.png")
                self.maquina_ppt.setPixmap(pixmap)
                maquina=maquina+1
            elif maquina1 == "Piedra" and usuario1 == "Tijera":
                resultado="perdiste"
                pixmap = QPixmap("\piedra.png")
                self.maquina_ppt.setPixmap(pixmap)
                maquina=maquina+1
            elif maquina1 == usuario1:
                resultado="empate"
                
            self.leyenda.setText(resultado)
            self.jugador.setText(str(usuario))
            self.maquina.setText(str(maquina))
            time.sleep(2)

            if len(hands) == 2:
                hand2 = hands[1]
                lmList2 = hand2["lmList"] 
                bbox2 = hand2["bbox"] 
                centerPoint2 = hand2['center'] 
                handType2 = hand2["type"] 
                fingers2 = self.detector.fingersUp(hand2)
                    
                t = cv2.waitKey(0)
                
                usuario1=""
                if(fingers1[0]==0 and fingers1[1]==0 and fingers1[2]==0 and fingers1[3]==0 and fingers1[4]==0 ):
                    usuario1="Piedra"
                    pixmap = QPixmap("img\piedra.png")
                    self.jugador_ppt.setPixmap(pixmap)
                if(fingers1[0]==0 and fingers1[1]==1 and fingers1[2]==1 and fingers1[3]==0 and fingers1[4]==0 ):
                    usuario1="Tijera"
                    pixmap = QPixmap("img\ijeras.png")
                    self.jugador_ppt.setPixmap(pixmap)
                if(fingers1[0]==1 and fingers1[1]==1 and fingers1[2]==1 and fingers1[3]==1 and fingers1[4]==1 ):
                    usuario1="Papel"
                    pixmap = QPixmap("img\papel.png")
                    self.jugador_ppt.setPixmap(pixmap)

                appt= random.randint(0,2)
                maquina1 = ""
                if appt== 0:
                    maquina1 = "Piedra"
                elif appt== 1:
                    maquina1 = "Papel"
                elif appt== 2:
                    maquina1 = "Tijera"


                if maquina1 == "Piedra" and usuario1 =="Papel":
                    resultado="Ganaste"
                    pixmap = QPixmap("img\piedra.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    usuario=usuario+1
                elif maquina1 == "Papel" and usuario1 == "Tijera":
                    resultado="Ganaste"
                    pixmap = QPixmap("img\papel.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    usuario=usuario+1
                elif maquina1 == "Tijera" and usuario1 == "Piedra":
                    resultado="Ganaste"
                    pixmap = QPixmap("img\ijeras.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    usuario=usuario+1
                elif maquina1 == "Papel" and usuario1 == "Piedra":
                    resultado="perdiste"
                    pixmap = QPixmap("img\papel.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    maquina=maquina+1
                elif maquina1 == "Tijera" and usuario1 =="Papel":
                    resultado="perdiste"
                    pixmap = QPixmap("img\ijeras.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    maquina=maquina+1
                elif maquina1 == "Piedra" and usuario1 == "Tijera":
                    resultado="perdiste"
                    pixmap = QPixmap("img\piedra.png")
                    self.maquina_ppt.setPixmap(pixmap)
                    maquina=maquina+1
                elif maquina1 == usuario1:
                    resultado="empate"
                    
                self.leyenda.setText(resultado)
                self.jugador.setText(str(usuario))
                self.maquina.setText(str(maquina))
                time.sleep(2)
                        


        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        altura, ancho, canales = img.shape
        byteslinea = canales * ancho
        convertToQtFormat = QImage(img.data, ancho, altura, byteslinea, QImage.Format.Format_RGB888)
        labelviedo = convertToQtFormat.scaled(self.video.width(), self.video.height(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.video.setPixmap(QPixmap.fromImage(labelviedo))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ppt()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
