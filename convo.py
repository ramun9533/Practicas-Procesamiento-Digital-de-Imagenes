import matplotlib.pyplot as plt
import numpy as np

def convolve(img, fil, mode='same'):
    def _convolve(img, fil):
        fil_height = fil.shape[0]
        fil_width = fil.shape[1]
        conv_height = img.shape[0] - fil.shape[0] + 1
        conv_width = img.shape[1] - fil.shape[1] + 1

        conv = np.zeros((conv_height, conv_width), dtype='uint8')
        for i in range(conv_height):
            for j in range(conv_width):
                conv[i][j] = wise_element_sum(img[i:i + fil_height, j:j + fil_width], fil)
        return conv

    def wise_element_sum(img, fil):
        res = (img * fil).sum()
        res = min(max(res, 0), 255)
        return res

    if mode == 'fill':
        h = fil.shape[0] // 2
        w = fil.shape[1] // 2
        img = np.pad(img, ((h, h), (w, w), (0, 0)), 'constant')

    conv_b = _convolve(img[:, :, 0], fil)
    conv_g = _convolve(img[:, :, 1], fil)
    conv_r = _convolve(img[:, :, 2], fil)

    dstack = np.dstack([conv_b, conv_g, conv_r])
    return dstack

# Lea la imagen aquí
img = plt.imread("lenna.png")

# Muestra la imagen leída
plt.imshow(img)
plt.title("Imagen Original")
plt.axis('off')
plt.show()

# El núcleo de revolución debe ser filas impares, columnas impares
fil = np.array([[-1, -1, -1, 0, 1],
                [-1, -1, 0, 1, 1],
                [-1, 0, 1, 1, 1]])

res = convolve(img, fil, 'fill')
print("img shape :" + str(img.shape))

# Muestra la imagen después de la convolución
plt.imshow(res)
plt.title("Imagen con Filtro Aplicado")
plt.axis('off')
plt.show()
print("res shape :" + str(res.shape))

# Guarda la imagen resultante
plt.imsave("res.jpg", res)
