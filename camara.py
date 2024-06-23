import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.uic import loadUi
import cv2
import time

class CaptureButton(QMainWindow):
    def __init__(self):
        super(CaptureButton, self).__init__()
        loadUi('camara.ui', self)
        self.setWindowTitle('Capture Button')
        self.captureButton.clicked.connect(self.capture_image)

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            QMessageBox.critical(self, 'Error', 'Unable to open webcam.')
            return

        ret, frame = cap.read()
        if ret:
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            filename = f'captured_{timestamp}.jpg'
            cv2.imwrite(filename, frame)
            QMessageBox.information(self, 'Success', f'Image captured and saved as {filename}.')
        else:
            QMessageBox.critical(self, 'Error', 'Failed to capture image.')

        cap.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CaptureButton()
    mainWindow.show()
    sys.exit(app.exec_())
