import numpy as np

def get_neighbors(image, x, y, neighbor_type='4'):
    rows, cols = image.shape
    neighbors = []
    
    if neighbor_type == '4':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-vecinos
    elif neighbor_type == '8':
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 8-vecinos
    else:
        raise ValueError("neighbor_type must be '4' or '8'")
    
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < rows and 0 <= new_y < cols:
            neighbors.append(image[new_x, new_y])
    
    return neighbors

# Ejemplo de uso
image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

x, y = 1, 1  # Coordenadas del píxel central

# Obtener 4-vecinos
neighbors_4 = get_neighbors(image, x, y, '4')
print(f'4-vecinos de ({x}, {y}): {neighbors_4}')

# Obtener 8-vecinos
neighbors_8 = get_neighbors(image, x, y, '8')
print(f'8-vecinos de ({x}, {y}): {neighbors_8}')
