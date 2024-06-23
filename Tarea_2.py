import numpy as np

def is_connected(image, x, y, V, neighbor_type='4'):
    filas, columnas = image.shape
    vecinos_conectados = []
    
    if neighbor_type == '4':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-vecinos
    elif neighbor_type == '8':
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 8-vecinos
    elif neighbor_type == 'm':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # m-vecinos inicialmente como 4-vecinos
    else:
        raise ValueError("neighbor_type must be '4', '8' or 'm'")
    
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < filas and 0 <= new_y < columnas and image[new_x, new_y] in V:
            vecinos_conectados.append((new_x, new_y))
    
    if neighbor_type == 'm':
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            diag_x, diag_y = x + dx, y + dy
            if 0 <= diag_x < filas and 0 <= diag_y < columnas:
                if image[diag_x, diag_y] in V and (image[x, diag_y] in V or image[diag_x, y] in V):
                    vecinos_conectados.append((diag_x, diag_y))
    
    return vecinos_conectados

def load_image_as_array(image_matrix):
    return np.array(image_matrix)

def check_connectivity(image, V, neighbor_type='4'):
    filas, columnas = image.shape
    connectivity_matrix = np.zeros((filas, columnas), dtype=bool)
    
    for x in range(filas):
        for y in range(columnas):
            if image[x, y] in V:
                neighbors = is_connected(image, x, y, V, neighbor_type)
                if neighbors:
                    connectivity_matrix[x, y] = True
    
    return connectivity_matrix

# Definiciones de las matrices de ejemplo
A = np.array([
    [255, 120, 240],
    [80, 100, 200],
    [60, 225, 80]
])

B = np.array([
    [120, 200, 110, 80],
    [80, 100, 200, 100],
    [60, 120, 225, 80],
    [255, 100, 50, 50]
])

# Definición del conjunto V
V = set(range(0, 129))

# Verificación de conectividad
conectividad_4_A = check_connectivity(A, V, '4')
conectividad_8_A = check_connectivity(A, V, '8')
conectividad_m_A = check_connectivity(A, V, 'm')

conectividad_4_B = check_connectivity(B, V, '4')
conectividad_8_B = check_connectivity(B, V, '8')
conectividad_m_B = check_connectivity(B, V, 'm')

print("Conectividad 4 en A:")
print(conectividad_4_A)
print("Conectividad 8 en A:")
print(conectividad_8_A)
print("Conectividad m en A:")
print(conectividad_m_A)

print("Conectividad 4 en B:")
print(conectividad_4_B)
print("Conectividad 8 en B:")
print(conectividad_8_B)
print("Conectividad m en B:")
print(conectividad_m_B)
