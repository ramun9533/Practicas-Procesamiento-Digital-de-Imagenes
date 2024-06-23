import numpy as np
from collections import deque

def get_neighbors(image, x, y, V, neighbor_type='4'):
    filas, columnas = image.shape
    vecinos = []
    
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
            vecinos.append((new_x, new_y))
    
    if neighbor_type == 'm':
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            diag_x, diag_y = x + dx, y + dy
            if 0 <= diag_x < filas and 0 <= diag_y < columnas:
                if image[diag_x, diag_y] in V and (image[x, diag_y] in V or image[diag_x, y] in V):
                    vecinos.append((diag_x, diag_y))
    
    return vecinos

def bfs(image, start, end, V, neighbor_type):
    filas, columnas = image.shape
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        
        for nx, ny in get_neighbors(image, x, y, V, neighbor_type):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

def check_paths(image, V, neighbor_type='4'):
    filas, columnas = image.shape
    caminos = np.zeros((filas, columnas), dtype=bool)
    
    for x in range(filas):
        for y in range(columnas):
            if image[x, y] in V:
                # Aquí definimos un píxel destino arbitrario, por ejemplo (0, 0)
                if bfs(image, (x, y), (0, 0), V, neighbor_type):
                    caminos[x, y] = True
    
    return caminos

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

# Verificación de caminos
caminos_4_A = check_paths(A, V, '4')
caminos_8_A = check_paths(A, V, '8')
caminos_m_A = check_paths(A, V, 'm')

caminos_4_B = check_paths(B, V, '4')
caminos_8_B = check_paths(B, V, '8')
caminos_m_B = check_paths(B, V, 'm')

print("Caminos 4 en A:")
print(caminos_4_A)
print("Caminos 8 en A:")
print(caminos_8_A)
print("Caminos m en A:")
print(caminos_m_A)

print("Caminos 4 en B:")
print(caminos_4_B)
print("Caminos 8 en B:")
print(caminos_8_B)
print("Caminos m en B:")
print(caminos_m_B)
