import numpy as np

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

def dfs(image, x, y, V, neighbor_type, visited, component_id, components):
    stack = [(x, y)]
    visited.add((x, y))
    components[x, y] = component_id
    
    while stack:
        cx, cy = stack.pop()
        for nx, ny in get_neighbors(image, cx, cy, V, neighbor_type):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny))
                components[nx, ny] = component_id

def find_connected_components(image, V, neighbor_type='4'):
    filas, columnas = image.shape
    visited = set()
    components = np.zeros((filas, columnas), dtype=int)
    component_id = 0
    
    for x in range(filas):
        for y in range(columnas):
            if image[x, y] in V and (x, y) not in visited:
                component_id += 1
                dfs(image, x, y, V, neighbor_type, visited, component_id, components)
    
    return components

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

# Encontrar componentes conexas
componentes_4_A = find_connected_components(A, V, '4')
componentes_8_A = find_connected_components(A, V, '8')
componentes_m_A = find_connected_components(A, V, 'm')

componentes_4_B = find_connected_components(B, V, '4')
componentes_8_B = find_connected_components(B, V, '8')
componentes_m_B = find_connected_components(B, V, 'm')

print("Componentes conexas 4 en A:")
print(componentes_4_A)
print("Componentes conexas 8 en A:")
print(componentes_8_A)
print("Componentes conexas m en A:")
print(componentes_m_A)

print("Componentes conexas 4 en B:")
print(componentes_4_B)
print("Componentes conexas 8 en B:")
print(componentes_8_B)
print("Componentes conexas m en B:")
print(componentes_m_B)
