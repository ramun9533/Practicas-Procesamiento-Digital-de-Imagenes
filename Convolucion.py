import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

def conv(image, kernel):
    height, width = image.shape  # Obtener dimensiones de la imagen
    h, w = kernel.shape          # Dimensiones del núcleo de convolución

    # Tamaño de la nueva imagen obtenida después de la operación de convolución
    new_h = height - h + 1
    new_w = width - w + 1

    # Inicializar la nueva matriz de imagen
    new_image = np.zeros((new_h, new_w), dtype=np.float64)

    # Realice la operación de convolución
    for i in range(new_h):
        for j in range(new_w):
            new_image[i, j] = np.sum(image[i:i+h, j:j+w] * kernel)

    # Recortar valores para estar en el rango [0, 255]
    new_image = new_image.clip(0, 255)

    # Convertir a entero sin signo de 8 bits
    new_image = np.rint(new_image).astype('uint8')
    return new_image

if __name__ == "__main__":
    try:
        # Lea la información de la imagen y conviértala en una matriz de numpy
        image = Image.open("lenna.png")
    except FileNotFoundError:
        print("La imagen 'lenna.png' no se encontró.")
        exit()

    output_path = "./LILY_ALONZO/"
    os.makedirs(output_path, exist_ok=True)
    a = np.array(image)

    # Definir los operadores
    kernels = {
        "sobel_x": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        "sobel_y": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        "sobel": np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]]),
        "prewitt_x": np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
        "prewitt_y": np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]),
        "prewitt": np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]),
        "laplacian": np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]),
        "laplacian_2": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    }

    print("Detección de gradientes\n")
    for name, kernel in kernels.items():
        print(f"Starting {name}...")
        print(f"Kernel:\n{kernel}")

        R = conv(a[:, :, 0], kernel)
        G = conv(a[:, :, 1], kernel)
        B = conv(a[:, :, 2], kernel)

        # Fusionar los resultados de los tres canales
        I = np.stack((R, G, B), axis=2)
        output_file = os.path.join(output_path, f"bigger-{name}.jpg")
        
        Image.fromarray(I).save(output_file)
        print(f"Guardado {output_file}")
