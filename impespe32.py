from PIL import Image

# Abre la imagen en blanco y negro
imagen = Image.open('f.jpg').convert('L')

# Reduce la resolución si es necesario
# Esto es opcional y depende de la resolución deseada

# Tamaño de la imagen
ancho, alto = imagen.size

# Abre un archivo para escribir el resultado
with open('resultado.txt', 'w') as archivo:
    for y in range(alto):
        byte = 0
        for x in range(ancho):
            # Obtiene el valor del pixel
            pixel = imagen.getpixel((x, y))
            
            # Verifica si el pixel es blanco
            if pixel > 128:
                byte |= 1 << (7 - (x % 8))
            
            # Si se completó un byte, escribe el valor en el archivo
            if (x + 1) % 8 == 0:
                archivo.write("B" + format(byte, '08b') + ", ")
                byte = 0
        # Escribe el último byte si la fila no es un múltiplo de 8
        if ancho % 8 != 0:
            archivo.write("B" + format(byte, '08b') + ", ")
        archivo.write("\n")
