import cv2
# Cargar el clasificador pre-entrenado para la detección de caras frontales
frontal_face_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Cargar el clasificador pre-entrenado para la detección de caras laterales 
profile_face_cascade = cv2.CascadeClassifier("haarcascade_profileface.xml')
# Verificar si el clasificador de caras laterales se ha cargado correctamente 
if profile_face_cascade.empty():
    print("Error: No se pudo cargar el clasificador de caras laterales.")
else:
    print("Clasificador de caras laterales cargado correctamente.")
# Cargar el video
video_capture = cv2.VideoCapture('persona.mp4')
while True:
# Leer un frame del video
    ret, frame = video_capture.read()
# Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Detectar caras frontales en el frame
    frontal_faces = frontal_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))| # Detectar caras laterales en el frame
    profile_faces=profile_face_cascade.detectMultiscale(gray, scalefactor=1.1, minNeighbors=5, minSize=(30, 30))
# Dibujar un rectángulo alrededor de cada cara frontal detectada for (x, y, w, h) in frontal_faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, 'Cara Frontal', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
# Dibujar un rectángulo alrededor de cada cara lateral detectada
    for (x, y, w, h) in profile_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Cara Lateral', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
# Mostrar el frame con las caras detectadas
cv2.imshow('Reconocimiento de caras en video', frame)
# Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar el objeto de captura y cerrar todas las ventanas
video_capture.release()
cv2.destroyAllWindows()
