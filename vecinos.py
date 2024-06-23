import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, Label
from PIL import Image, ImageTk

# Función para abrir la imagen
def open_imagen():
    file_path = filedialog.askopenfilename()
    if file_path:
        img1 = cv2.imread(file_path)
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        
        # Convertir la imagen de OpenCV a PIL para mostrarla en Tkinter
        img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img1_rgb)
        img_tk = ImageTk.PhotoImage(image=img_pil)

        # Mostrar la imagen en Tkinter
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector

        process_image(img)

# Función para mostrar los vecinos
def show_vecinos(vecinos, window_title):
    neighbor_window = tk.Toplevel(root)
    neighbor_window.title(window_title)
    text_widget = tk.Text(neighbor_window, wrap='word')
    text_widget.pack(expand=1, fill='both')
    text_widget.insert('1.0', str(vecinos))

# Función para procesar la imagen y encontrar los vecinos
def process_image(img):
    ren, Columnas = img.shape
    four_neighbors = np.zeros((ren, Columnas), dtype=object)
    eight_neighbors = np.zeros((ren, Columnas), dtype=object)
    for i in range(ren):
        for j in range(Columnas):
            four_neighbors[i, j] = get_four_neighbors(img, i, j)
            eight_neighbors[i, j] = get_eight_neighbors(img, i, j)
    show_vecinos(four_neighbors, "4 Vecinos")
    show_vecinos(eight_neighbors, "8 Vecinos")

# Función para obtener los 4 vecinos
def get_four_neighbors(img, x, y):
    ren, Columnas = img.shape
    vecinos = []
    if x > 0:
        vecinos.append(img[x-1, y])
    if x < ren - 1:
        vecinos.append(img[x+1, y])
    if y > 0:
        vecinos.append(img[x, y-1])
    if y < Columnas - 1:
        vecinos.append(img[x, y+1])
    return vecinos

# Función para obtener los 8 vecinos
def get_eight_neighbors(img, x, y):
    ren, Columnas = img.shape
    vecinos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < ren and 0 <= y + j < Columnas:
                vecinos.append(img[x + i, y + j])
    return vecinos

# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Vecinos de la Imagen")
open_button = tk.Button(root, text="Abrir Imagen", command=open_imagen)
open_button.pack()
image_label = tk.Label(root)
image_label.pack()
root.mainloop()
