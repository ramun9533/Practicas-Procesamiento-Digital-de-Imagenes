import matplotlib.pyplot as plt
import cv2
import numpy as np

# Leer la imagen
img = cv2.imread("lenna.png")
# Convertir la imagen de BGR a RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostrar la imagen leída
plt.imshow(img_rgb)
plt.title("Imagen Original")
plt.axis('off')  # Ocultar los ejes
plt.show()

# Este es el filtro establecido, que es el núcleo de convolución
fil = np.array([
    [-1, -1, 0], 
    [-1, 0, 1],
    [0, 1, 1]
])

# Utilice la función de convolución de opencv
res = cv2.filter2D(img_rgb, -1, fil)

# Mostrar la imagen después de la convolución
plt.imshow(res)
plt.title("Imagen con Filtro Aplicado")
plt.axis('off')  # Ocultar los ejes
plt.show()

# Guardar la imagen resultante
plt.imsave("res.jpg", res)
