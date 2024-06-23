import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generación de datos de ejemplo (una matriz con 100 muestras y 5 características)
np.random.seed(0)
data = np.random.rand(100, 5)

# Estandarización de los datos
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data_scaled = (data - mean) / std

# Cálculo de la matriz de covarianza
cov_matrix = np.cov(data_scaled, rowvar=False)

# Obtención de los autovalores y autovectores
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Ordenar los autovectores por autovalores descendentes
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvectors_sorted = eigenvectors[:, sorted_indices]

# Reducción a 3 componentes principales
principal_components = np.dot(data_scaled, eigenvectors_sorted[:, :3])

# Explicación de la variabilidad por cada componente principal
explained_variance = eigenvalues / np.sum(eigenvalues)

# Visualización de los resultados en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(principal_components[:, 0], principal_components[:, 1], principal_components[:, 2],
                     c='blue', s=50)
ax.set_title('PCA: Reducción a 3 Componentes Principales')
ax.set_xlabel(f'Componente Principal 1 ({explained_variance[0]:.2f} varianza explicada)')
ax.set_ylabel(f'Componente Principal 2 ({explained_variance[1]:.2f} varianza explicada)')
ax.set_zlabel(f'Componente Principal 3 ({explained_variance[2]:.2f} varianza explicada)')
plt.show()

# Información adicional
print(f'Varianza explicada por cada componente principal: {explained_variance}')
print(f'Componentes principales:\n{eigenvectors_sorted[:, :3]}')
