import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# Función para cargar una imagen desde la computadora
def cargar_imagen():
    global imagen_original, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        imagen_original = Image.open(file_path)
        # Redimensionar la imagen
        imagen_original = imagen_original.resize((300, 300), Image.LANCZOS)
        imagen_original_tk = ImageTk.PhotoImage(imagen_original)
        label_original.config(image=imagen_original_tk)
        label_original.image = imagen_original_tk
        boton_mostrar_gris.config(state=tk.NORMAL)
        boton_mostrar_difuminado.config(state=tk.NORMAL)
        boton_mostrar_filtrado.config(state=tk.NORMAL)
        boton_mostrar_erosion.config(state=tk.NORMAL)
        boton_mostrar_contorno.config(state=tk.NORMAL)
        boton_mostrar_um.config(state=tk.NORMAL)

# Función para comenzar la grabación de video
def empezar_grabacion():
    global video_capture, video_writer, grabando
    grabando = True
    video_writer = cv2.VideoWriter('video_grabado.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

# Función para detener la grabación de video
def detener_grabacion():
    global video_writer, grabando
    grabando = False
    if video_writer is not None:
        video_writer.release()

# Función para mostrar la cámara web en una ventana secundaria
def mostrar_video():
    ventana_video = tk.Toplevel()
    ventana_video.title("Cámara Web")
    
    def cerrar_ventana():
        detener_grabacion()  # Detener la grabación al cerrar la ventana
        ventana_video.destroy()

    boton_cerrar = tk.Button(ventana_video, text="Cerrar Video", command=cerrar_ventana)
    boton_cerrar.pack()

    video_capture = cv2.VideoCapture(0)
    grabando = False
    video_writer = None

    boton_empezar = tk.Button(ventana_video, text="Comenzar Grabación", command=empezar_grabacion)
    boton_empezar.pack()

    boton_detener = tk.Button(ventana_video, text="Detener Grabación", command=detener_grabacion)
    boton_detener.pack()

    def actualizar_video():
        ret, frame = video_capture.read()
        if ret:
            if grabando:
                video_writer.write(frame)  # Escribir el frame en el archivo de video
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (400, 300))
            frame = Image.fromarray(frame)
            frame_tk = ImageTk.PhotoImage(image=frame)
            label_video.config(image=frame_tk)
            label_video.image = frame_tk
            ventana_video.after(10, actualizar_video)

    label_video = tk.Label(ventana_video, width=400, height=300)
    label_video.pack()

    actualizar_video()

# Función para mostrar la imagen en escala de grises
def mostrar_gris():
    global imagen_gris
    imagen_gris_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
    imagen_gris_pil = Image.fromarray(imagen_gris_cv)
    imagen_gris_pil = imagen_gris_pil.resize((300, 300), Image.LANCZOS)
    imagen_gris_tk = ImageTk.PhotoImage(imagen_gris_pil)
    label_filtrado.config(image=imagen_gris_tk)
    label_filtrado.image = imagen_gris_tk

# Función para mostrar la imagen en erosion
def mostrar_erosion():
    global imagen_erosion
    imagen_erosionada_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
    kernel = np.ones((5, 5), np.uint8)
    imagen_erosionada_cv = cv2.erode(imagen_erosionada_cv, kernel, iterations=1)
    imagen_erosionada_pil = Image.fromarray(imagen_erosionada_cv)
    imagen_erosionada_pil = imagen_erosionada_pil.resize((300, 300), Image.LANCZOS)
    imagen_erosionada_tk = ImageTk.PhotoImage(imagen_erosionada_pil)
    label_filtrado.config(image=imagen_erosionada_tk)
    label_filtrado.image = imagen_erosionada_tk

# Función para mostrar la imagen en filtrado
def mostrar_filtrado():
    global imagen_filtrado
    imagen_filtrado_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
    filtro_personalizado = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]]) / 9.0
    imagen_filtrado_cv = cv2.filter2D(imagen_filtrado_cv, -1, filtro_personalizado)
    imagen_filtrado_pil = Image.fromarray(imagen_filtrado_cv)
    imagen_filtrado_pil = imagen_filtrado_pil.resize((300, 300), Image.LANCZOS)
    imagen_filtrado_tk = ImageTk.PhotoImage(imagen_filtrado_pil)
    label_filtrado.config(image=imagen_filtrado_tk)
    label_filtrado.image = imagen_filtrado_tk

# Función para mostrar la imagen en difuminado
def mostrar_difuminado():
    global imagen_difuminado
    imagen_difuminado_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
    imagen_difuminado_cv = cv2.GaussianBlur(imagen_difuminado_cv, (5, 5), 0)
    imagen_difuminado_pil = Image.fromarray(imagen_difuminado_cv)
    imagen_difuminado_pil = imagen_difuminado_pil.resize((300, 300), Image.LANCZOS)
    imagen_difuminado_tk = ImageTk.PhotoImage(imagen_difuminado_pil)
    label_filtrado.config(image=imagen_difuminado_tk)
    label_filtrado.image = imagen_difuminado_tk

# Función para mostrar la imagen con contorno 
def mostrar_contorno():
    global imagen_contorno
    imagen_contorno_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
    imagen_contorno_cv = cv2.Canny(imagen_contorno_cv, threshold1=30, threshold2=100)
    imagen_contorno_pil = Image.fromarray(imagen_contorno_cv)
    imagen_contorno_pil = imagen_contorno_pil.resize((300, 300), Image.LANCZOS)
    imagen_contorno_tk = ImageTk.PhotoImage(imagen_contorno_pil)
    label_filtrado.config(image=imagen_contorno_tk)
    label_filtrado.image = imagen_contorno_tk

def mostrar_lumbralizado():
    global imagen_lum
    imagen_lum_cv = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
    umbral, imagen_lum_cv = cv2.threshold(imagen_lum_cv, 128, 255, cv2.THRESH_BINARY)
    imagen_lum_pil = Image.fromarray(imagen_lum_cv)
    imagen_lum_pil = imagen_lum_pil.resize((300, 300), Image.LANCZOS)
    imagen_lum_tk = ImageTk.PhotoImage(imagen_lum_pil)
    label_filtrado.config(image=imagen_lum_tk)
    label_filtrado.image = imagen_lum_tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Imágenes")
ventana.geometry("800x500")

# Crear el marco para los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(side=tk.LEFT, padx=10, pady=10)

# Crear los botones
boton_cargar_imagen = tk.Button(marco_botones, text="Cargar Imagen", command=cargar_imagen)
boton_mostrar_gris = tk.Button(marco_botones, text="Mostrar en Escala de Grises", command=mostrar_gris, state=tk.DISABLED)
boton_mostrar_erosion = tk.Button(marco_botones, text="Mostrar con Erosión", command=mostrar_erosion, state=tk.DISABLED)
boton_mostrar_filtrado = tk.Button(marco_botones, text="Mostrar con Filtrado", command=mostrar_filtrado, state=tk.DISABLED)
boton_mostrar_difuminado = tk.Button(marco_botones, text="Mostrar con Difuminado", command=mostrar_difuminado, state=tk.DISABLED)
boton_mostrar_contorno = tk.Button(marco_botones, text="Mostrar con Contorno", command=mostrar_contorno, state=tk.DISABLED)
boton_mostrar_um = tk.Button(marco_botones, text="Mostrar con Umbralizado", command=mostrar_lumbralizado, state=tk.DISABLED)
boton_video = tk.Button(marco_botones, text="Video", command=mostrar_video)  # Botón para mostrar la cámara web

# Colocar los botones en el marco
boton_cargar_imagen.pack(pady=10)
boton_mostrar_gris.pack(pady=10)
boton_mostrar_erosion.pack(pady=10)
boton_mostrar_filtrado.pack(pady=10)
boton_mostrar_difuminado.pack(pady=10)
boton_mostrar_contorno.pack(pady=10)
boton_mostrar_um.pack(pady=10)
boton_video.pack(pady=10)  # Agregar el botón "Video"

# Crear labels para mostrar las imágenes
label_original = tk.Label(ventana, width=300, height=300)
label_filtrado = tk.Label(ventana, width=300, height=300)

# Colocar los elementos en la ventana
label_original.pack(side=tk.LEFT, padx=10)
label_filtrado.pack(side=tk.RIGHT, padx=10)

# Variables globales para las imágenes
imagen_original = None
file_path = None

# Iniciar el bucle de la aplicación
ventana.mainloop()