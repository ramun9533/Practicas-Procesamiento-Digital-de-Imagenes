import cv2
# Leer la imagen en escala de grises
img = cv2.imread('metal-slug.jpg', 0)
# Aplicar el filtro laplaciano
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# Mostrar la imagen filtrada
cv2.imshow('Laplacian Image', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()