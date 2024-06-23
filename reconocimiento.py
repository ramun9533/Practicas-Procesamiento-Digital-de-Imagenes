import cv2

# Cargar el clasificador pre-entrenado para la detección de caras frontales
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Cargar el video
video_capture = cv2.VideoCapture('Esparta.mp4')

while True:

    # Leer un frame del video

    ret, frame = video_capture.read()

# Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Detectar caras frontales en el frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
# Dibujar un rectángulo alrededor de cada cara detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Cara', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
# Mostrar el frame con las caras detectadas
    cv2.imshow('Reconocimiento de caras en video', frame)
# Salir del bucle si se presiona la tecla 'q' if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# Liberar el objeto de captura y cerrar todas las ventanas
video_capture.release()
cv2.destroyAllwindows()
