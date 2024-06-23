import cv2

def main():
    # Inicializar el objeto capturador de video
    cap = cv2.VideoCapture(0)  # 0 indica que se usará la primera cámara disponible
    
    # Verificar si la cámara se ha abierto correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    # Bucle principal para leer y mostrar el vídeo de la cámara
    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()

        # Verificar si el frame se ha leído correctamente
        if not ret:
            print("Error: No se pudo leer el frame.")
            break

        # Mostrar el frame en una ventana
        cv2.imshow("Webcam", frame)

        # Esperar 1 milisegundo y verificar si se ha presionado la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el objeto capturador de video y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
