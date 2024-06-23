import cv2
# Leer la imagen
img = cv2.imread('VaultBoyFO3.jpg')
# Aplicar el filtro gaussiano
filtered_img = cv2.GaussianBlur(img, (5, 5), 0)
# Mostrar la imagen filtrada
cv2.imshow('Filtered Image&#39', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()