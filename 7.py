import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para agregar ruido gaussiano
def agregar_ruido_gaussiano(imagen, media=0, desviacion_estandar=25):
    gauss = np.random.normal(media, desviacion_estandar, imagen.shape).astype('uint8')
    imagen_ruidosa = cv2.add(imagen, gauss)
    return imagen_ruidosa

# Función para agregar ruido aleatorio (sal y pimienta)
def agregar_ruido_aleatorio(imagen, probabilidad_sal=0.05, probabilidad_pimienta=0.05):
    imagen_ruidosa = np.copy(imagen)
    mascara_sal = np.random.rand(*imagen.shape) < probabilidad_sal
    mascara_pimienta = np.random.rand(*imagen.shape) < probabilidad_pimienta
    imagen_ruidosa[mascara_sal] = 255
    imagen_ruidosa[mascara_pimienta] = 0
    return imagen_ruidosa

# Función para aplicar filtro de paso bajo Gaussiano
def aplicar_filtro_paso_bajo(imagen, tamano_kernel):
    return cv2.GaussianBlur(imagen, (tamano_kernel, tamano_kernel), 0)

# Cargar la imagen
direccion_imagen = 'circuito.jpg'
imagen = cv2.imread(direccion_imagen, cv2.IMREAD_GRAYSCALE)

# Agregar ruido gaussiano
imagen_ruido_gaussiano = agregar_ruido_gaussiano(imagen)

# Agregar ruido aleatorio (sal y pimienta)
imagen_ruido_aleatorio = agregar_ruido_aleatorio(imagen)

# Aplicar filtro de paso bajo de orden 5x5
imagen_filtro_paso_bajo = aplicar_filtro_paso_bajo(imagen, 5)
imagen_filtro_paso_bajo_gaussiano = aplicar_filtro_paso_bajo(imagen_ruido_gaussiano, 5)
imagen_filtro_paso_bajo_aleatorio = aplicar_filtro_paso_bajo(imagen_ruido_aleatorio, 5)

# Mostrar las imágenes en un solo plot
figura, ejes = plt.subplots(2, 3, figsize=(15, 10))

ejes[0, 0].imshow(imagen, cmap='gray')
ejes[0, 0].set_title('Imagen Original')
ejes[0, 0].axis('off')

ejes[0, 1].imshow(imagen_ruido_gaussiano, cmap='gray')
ejes[0, 1].set_title('Ruido Gaussiano')
ejes[0, 1].axis('off')

ejes[0, 2].imshow(imagen_ruido_aleatorio, cmap='gray')
ejes[0, 2].set_title('Ruido Sal y Pimienta')
ejes[0, 2].axis('off')

ejes[1, 0].imshow(imagen_filtro_paso_bajo, cmap='gray')
ejes[1, 0].set_title('Filtro Paso Bajo 5x5 (Original)')
ejes[1, 0].axis('off')

ejes[1, 1].imshow(imagen_filtro_paso_bajo_gaussiano, cmap='gray')
ejes[1, 1].set_title('Filtro Paso Bajo 5x5 (Gaussiano)')
ejes[1, 1].axis('off')

ejes[1, 2].imshow(imagen_filtro_paso_bajo_aleatorio, cmap='gray')
ejes[1, 2].set_title('Filtro Paso Bajo 5x5 (Aleatorio)')
ejes[1, 2].axis('off')

plt.tight_layout()
plt.show()
