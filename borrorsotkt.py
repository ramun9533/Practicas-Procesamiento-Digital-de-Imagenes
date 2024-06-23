import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter

# Funciones para cargar, modificar y guardar la imagen
def cargar_imagen():
    global imagen, img_tk
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        imagen = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(imagen)
        panel.config(image=img_tk)
        panel.image = img_tk

def aplicar_borroso():
    global imagen, img_tk
    if imagen:
        imagen_borrosa = imagen.filter(ImageFilter.GaussianBlur(radius=5))
        img_tk = ImageTk.PhotoImage(imagen_borrosa)
        panel.config(image=img_tk)
        panel.image = img_tk
        imagen = imagen_borrosa
    else:
        messagebox.showerror("Error", "Primero cargue una imagen.")

def guardar_imagen():
    if imagen:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg;*.jpeg"),
                                                            ("BMP files", "*.bmp")])
        if file_path:
            imagen.save(file_path)
    else:
        messagebox.showerror("Error", "Primero cargue y modifique una imagen.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Editor de Imágenes Tkinter")

# Variables globales
imagen = None
img_tk = None

# Crear botones y panel para la imagen
btn_cargar = tk.Button(root, text="Cargar Imagen", command=cargar_imagen)
btn_cargar.pack()

btn_borroso = tk.Button(root, text="Aplicar Borroso", command=aplicar_borroso)
btn_borroso.pack()

btn_guardar = tk.Button(root, text="Guardar Imagen", command=guardar_imagen)
btn_guardar.pack()

panel = tk.Label(root)
panel.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
