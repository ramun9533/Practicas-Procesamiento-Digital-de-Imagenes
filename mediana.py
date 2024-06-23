import cv2
# Leer la imagen
img = cv2.imread('metal-slug-code.jpg')
# Aplicar el filtro de mediana
filtered_img = cv2.medianBlur(img, 5)
# Mostrar la imagen filtrada
cv2.imshow('Filtered Image&#39', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()