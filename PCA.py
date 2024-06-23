import numpy as np
import matplotlib.pyplot as plt

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

# Reducción a 2 componentes principales
principal_components = np.dot(data_scaled, eigenvectors_sorted[:, :2])

# Explicación de la variabilidad por cada componente principal
explained_variance = eigenvalues / np.sum(eigenvalues)

# Visualización de los resultados
plt.figure(figsize=(8, 6))
plt.scatter(principal_components[:, 0], principal_components[:, 1], edgecolor='k', s=50)
plt.title('PCA: Reducción a 2 Componentes Principales')
plt.xlabel(f'Componente Principal 1 ({explained_variance[0]:.2f} varianza explicada)')
plt.ylabel(f'Componente Principal 2 ({explained_variance[1]:.2f} varianza explicada)')
plt.grid(True)
plt.show()

# Información adicional
print(f'Varianza explicada por cada componente principal: {explained_variance}')
print(f'Componentes principales:\n{eigenvectors_sorted[:, :2]}')
