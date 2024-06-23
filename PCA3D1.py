import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generación de datos de ejemplo (una matriz con 100 muestras y 5 características)
np.random.seed(0)
data = np.random.rand(300, 10)

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

# Colores para cada componente principal
colors = ['red', 'green', 'blue']

# Visualización de los resultados en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterar sobre cada componente principal y dibujarlo con un color diferente
for i in range(1):  # Solo iterar una vez (solo se trazan los primeros dos componentes)
    ax.scatter(principal_components[:, i], principal_components[:, i+1], principal_components[:, i+2],
               c=colors[i], label=f'Componente Principal {i+1}', s=50)

ax.set_title('PCA: Reducción a 3 Componentes Principales')
ax.set_xlabel(f'Componente Principal 1 ({explained_variance[0]:.2f} varianza explicada)')
ax.set_ylabel(f'Componente Principal 2 ({explained_variance[1]:.2f} varianza explicada)')
ax.set_zlabel(f'Componente Principal 3 ({explained_variance[2]:.2f} varianza explicada)')
ax.legend()
plt.show()

# Información adicional
print(f'Varianza explicada por cada componente principal: {explained_variance}')
print(f'Componentes principales:\n{eigenvectors_sorted[:, :3]}')
