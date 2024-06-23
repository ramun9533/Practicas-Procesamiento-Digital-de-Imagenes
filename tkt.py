import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi ventana Tkinter")

# Crear un label (etiqueta)
label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
