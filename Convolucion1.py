import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
from PIL import Image
import os

def conv(image, kernel):
    height, width = image.shape        # Obtener dimensiones de imagen
    h, w = kernel.shape                 # Dimensiones del núcleo de convolución
    # Tamaño de la nueva imagen obtenida después de la operación de convolución
    new_h = height - h + 1
    new_w = width - w + 1
    # Inicializar la nueva matriz de imagen
    new_image = np.zeros((new_h, new_w),dtype=np.float64)     

    # Realice la operación de convolución, multiplique los valores de elementos correspondientes de la matriz
    for i in range(new_w):
        for j in range(new_h):
            new_image[i, j] = np.sum(image[i:i+h, j:j+w] * kernel)    # Los elementos de la matriz se multiplican y acumulan

    # Elimine los valores originales menores que 0 y mayores que 255 después de la multiplicación de la matriz, restablezca a 0 y 255
    # Use la función de recorte para procesar los elementos de la matriz de modo que los valores de los elementos estén entre (0, 255)
    new_image = new_image.clip(0, 255)   

    # Redondea el valor de cada elemento de la nueva imagen y luego conviértelo a un entero sin signo de 8 bits
    new_image = np.rint(new_image).astype('uint8')     
    return new_image

if __name__ == "__main__":
    # Lea la información de la imagen y conviértala en una matriz bajo numpy
    image = Image.open("lenna.png", 'r')
    output_path = "./LILY ALONZO/"
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    a = np.array(image)

    # operador sobel
    sobel_x = np.array(([-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]))
    sobel_y = np.array(([-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]))
    sobel = np.array(([-1, -1, 0],
                      [-1, 0, 1],
                      [0, 1, 1]))

    # operadores prewitt en todas las direcciones
    prewitt_x = np.array(([-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]))
    prewitt_y = np.array(([-1, -1, -1],
                          [0, 0, 0],
                          [1, 1, 1]))
    prewitt = np.array(([-2, -1, 0],
                        [-1, 0, 1],
                        [0, 1, 2]))

    # Operador de Laplace
    laplacian = np.array(([0, -1, 0],
                          [-1, 4, -1],
                          [0, -1, 0]))
    laplacian_2 = np.array(([-1, -1, -1],
                            [-1, 8, -1],
                            [-1, -1, -1]))

    kernel_list = ("sobel_x", "sobel_y", "sobel", "prewitt_x", "prewitt_y", "prewitt", "laplacian", "laplacian_2")

    print("Gridient detection\n")
    for w in kernel_list:
        print("starting %s....." % w)
        print("kernel:\n")
        print("R\n")
        R = conv(a[:, :, 0], eval(w))
        print("G\n")
        G = conv(a[:, :, 1], eval(w))
        print("B\n")
        B = conv(a[:, :, 2], eval(w))

        I = np.stack((R, G, B), axis=2)     # Fusionar los resultados de los tres canales
        Image.fromarray(I).save("%s//bigger-%s.jpg" % (output_path, w))