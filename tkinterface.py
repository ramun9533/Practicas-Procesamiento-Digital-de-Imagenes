import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import time

filename = None
original_image = None
final_image = None

def cargarImagen():
    global filename, original_image
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    if filename:
        original_image = cv2.imread(filename)
        setPhoto(original_image, label_original)
        final_image = original_image.copy()
        setPhoto(final_image, label_procesada)

def setPhoto(image, label):
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img_tk = ImageTk.PhotoImage(image=img)
    label.config(image=img_tk)
    label.image = img_tk

def salvarImagen():
    global final_image
    if final_image is not None:
        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        cv2.imwrite(f"imagen_{tiempo}.jpg", final_image)
        messagebox.showinfo("Guardar Imagen", "Imagen guardada exitosamente")
    else:
        messagebox.showerror("Guardar Imagen", "No se puede guardar la imagen porque no se ha procesado ninguna")

def aplicarRuido():
    global final_image
    if final_image is not None:
        row, col, ch = final_image.shape
        mean = 0
        sigma = 0.1 * 255
        gauss = np.random.normal(mean, sigma, (row, col, ch)).astype('uint8')
        noisy = cv2.add(final_image, gauss)
        final_image = noisy
        setPhoto(final_image, label_procesada)
    else:
        messagebox.showerror("Error", "No se ha cargado ninguna imagen")

def eliminarRuido():
    global final_image, original_image
    if original_image is not None:
        final_image = original_image.copy()
        setPhoto(final_image, label_procesada)
    else:
        messagebox.showerror("Error", "No se ha cargado ninguna imagen")

# Crear ventana principal
root = tk.Tk()
root.title("Editor de Imágenes Tkinter")
root.geometry("928x478")
root.configure(bg="#2C3E50")

# Estilo de los widgets
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=6,
                relief="flat",
                background="#3498DB",
                foreground="white",
                borderwidth=0)
style.map("TButton",
          background=[("active", "#2980B9")])
style.configure("TLabel",
                background="#2C3E50",
                foreground="white",
                font=("Arial", 12))

# Crear widgets
label_original = tk.Label(root, text="", borderwidth=1, relief="solid")
label_original.place(x=50, y=60, width=361, height=231)

label_procesada = tk.Label(root, text="", borderwidth=1, relief="solid")
label_procesada.place(x=520, y=60, width=361, height=231)

btn_cargar = ttk.Button(root, text="Cargar Imagen", command=cargarImagen)
btn_cargar.place(x=150, y=340, width=150, height=40)

btn_guardar = ttk.Button(root, text="Guardar Imagen", command=salvarImagen)
btn_guardar.place(x=630, y=340, width=160, height=40)

btn_aplicar_ruido = ttk.Button(root, text="Aplicar Ruido", command=aplicarRuido)
btn_aplicar_ruido.place(x=310, y=340, width=150, height=40)

btn_eliminar_ruido = ttk.Button(root, text="Eliminar Ruido", command=eliminarRuido)
btn_eliminar_ruido.place(x=470, y=340, width=150, height=40)

btn_salir = ttk.Button(root, text="Salir", command=root.quit)
btn_salir.place(x=650, y=400, width=121, height=31)

# Etiquetas de texto
label1 = ttk.Label(root, text="Original", font=("Arial", 14, "bold"))
label1.place(x=60, y=0, width=341, height=61)

label2 = ttk.Label(root, text="Procesada", font=("Arial", 14, "bold"))
label2.place(x=530, y=0, width=341, height=61)

# Ejecutar la aplicación
root.mainloop()
