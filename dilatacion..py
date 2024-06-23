import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion
from PIL import Image, ImageOps

# Cargar la imagen
image_path = 'VaultBoyFO3.jpg'  # Reemplaza con la ruta a tu imagen
image = Image.open(image_path).convert('L')  # Convertir a escala de grises

# Convertir la imagen a binaria
threshold = 128
binary_image = np.array(image) > threshold

# Definir el elemento estructural (una cruz en este caso)
structuring_element = np.array([[0, 1, 0],
                                [1, 1, 1],
                                [0, 1, 0]])

# Aplicar dilatación
dilated_image = binary_dilation(binary_image, structure=structuring_element)

# Aplicar erosión
eroded_image = binary_erosion(binary_image, structure=structuring_element)

# Visualizar las imágenes
fig, ax = plt.subplots(1, 4, figsize=(16, 4))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Imagen Original en Escala de Grises')
ax[1].imshow(binary_image, cmap='gray')
ax[1].set_title('Imagen Binaria')
ax[2].imshow(dilated_image, cmap='gray')
ax[2].set_title('Imagen Dilatada')
ax[3].imshow(eroded_image, cmap='gray')
ax[3].set_title('Imagen Erosionada')
for a in ax:
    a.axis('off')
plt.show()

