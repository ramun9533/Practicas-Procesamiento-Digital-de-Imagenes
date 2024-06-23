import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_imagen():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        imagen = cv2.imread(ruta_imagen)
        mostrar_imagen(imagen)
        guardar_btn['state'] = 'normal'
        ajustar_btn['state'] = 'normal'

def mostrar_imagen(imagen):
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imagen = Image.fromarray(imagen)
    imagen = ImageTk.PhotoImage(imagen)
    panel_imagen.config(image=imagen)
    panel_imagen.image = imagen

def ajustar_contraste_y_brillo(contraste, brillo):
    global imagen_original
    imagen_modificada = cv2.convertScaleAbs(imagen_original, alpha=contraste_scale, beta=brillo_scale)
    mostrar_imagen(imagen_modificada)

def guardar_imagen():
    ruta_guardar = filedialog.asksaveasfilename(defaultextension=".jpg")
    if ruta_guardar:
        cv2.imwrite(ruta_guardar, cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB))

# Configuración de la ventana
root = tk.Tk()
root.title("Ajuste de Contraste y Brillo")

# Crear panel para la imagen
panel_imagen = tk.Label(root)
panel_imagen.pack()

# Botones
abrir_btn = tk.Button(root, text="Abrir Imagen", command=abrir_imagen)
abrir_btn.pack(side="left", padx=10, pady=10)

guardar_btn = tk.Button(root, text="Guardar Imagen", command=guardar_imagen, state='disabled')
guardar_btn.pack(side="left", padx=10, pady=10)

ajustar_btn = tk.Button(root, text="Ajustar", command=lambda: ajustar_contraste_y_brillo(contraste_scale.get(), brillo_scale.get()), state='disabled')
ajustar_btn.pack(side="left", padx=10, pady=10)

# Escalas para ajustar contraste y brillo
contraste_scale = tk.Scale(root, label="Contraste", from_=0.1, to=3, resolution=0.1, orient="horizontal")
contraste_scale.pack(side="left", padx=10, pady=10)

brillo_scale = tk.Scale(root, label="Brillo", from_=-100, to=100, orient="horizontal")
brillo_scale.pack(side="left", padx=10, pady=10)

root.mainloop()
