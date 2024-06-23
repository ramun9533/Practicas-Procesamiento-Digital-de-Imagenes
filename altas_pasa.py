import numpy as np
from scipy.ndimage import convolve

def gradient_filter(image):
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    return convolve(image, kernel)

# Ejemplo de uso
image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
gradient_image = gradient_filter(image)
print(gradient_image)
