import cv2

# Función para ajustar el contraste y el brillo de una imagen
def ajustar_contraste_y_brillo(imagen, contraste, brillo):
    # Ajusta el contraste y el brillo utilizando la fórmula: nueva_imagen = alfa * imagen + beta
    nueva_imagen = cv2.convertScaleAbs(imagen, alpha=contraste, beta=brillo)
    return nueva_imagen

# Carga la imagen
imagen = cv2.imread('lenna.png')

# Ajusta el contraste y el brillo
nueva_imagen = ajustar_contraste_y_brillo(imagen, contraste=0.5, brillo=70)

# Guarda la imagen modificada
cv2.imwrite('imagen_modificada.jpg', nueva_imagen)

# Muestra la imagen original y la imagen modificada
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Modificada', nueva_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
