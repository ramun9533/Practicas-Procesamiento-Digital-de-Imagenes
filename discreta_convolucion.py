import numpy as np
from scipy.signal import convolve2d

# Ejemplo de convolución discreta
def apply_convolution(image, kernel):
    return convolve2d(image, kernel, mode='same', boundary='wrap')

image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
convoluted_image = apply_convolution(image, kernel)
print(convoluted_image)
