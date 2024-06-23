import cv2

def canny_edge_detection(image):
    return cv2.Canny(image, 100, 200)

# Leer la imagen (asegúrate de que la ruta a la imagen sea correcta)
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# Aplicar la detección de bordes Canny
edges = canny_edge_detection(image)

# Mostrar la imagen con los bordes detectados
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
