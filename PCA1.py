import numpy as np
import matplotlib.pyplot as plt

# Generación de datos de ejemplo (una matriz con 100 muestras y 5 características)
np.random.seed(0)
data = np.random.rand(100, 5)

# Estandarización de los datos
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data_scaled = (data - mean) / std

# Implementación de k-means desde cero
def k_means(data, k, max_iters=100):
    # Inicialización aleatoria de centroides
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    for _ in range(max_iters):
        # Asignación de puntos al centroide más cercano
        labels = np.argmin(((data[:, None] - centroids) ** 2).sum(axis=2), axis=1)
        
        # Actualización de los centroides
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # Comprobación de convergencia
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return centroids, labels

# Ejecución de k-means
centroids, labels = k_means(data_scaled, k=3)

# Obtención de los componentes principales
cov_matrix = np.cov(data_scaled, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvectors_sorted = eigenvectors[:, sorted_indices]
principal_components = np.dot(data_scaled, eigenvectors_sorted[:, :2])

# Cálculo de la varianza explicada de las componentes principales
explained_variance = eigenvalues / np.sum(eigenvalues)

# Visualización de los resultados
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.scatter(principal_components[labels == i, 0], principal_components[labels == i, 1], edgecolor='k', s=50, label=f'Grupo {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label='Centroides')
plt.title('PCA: Reducción a 2 Componentes Principales con Agrupamiento (k-means desde cero)')
plt.xlabel(f'Componente Principal 1 ({explained_variance[0]:.2f} varianza explicada)')
plt.ylabel(f'Componente Principal 2 ({explained_variance[1]:.2f} varianza explicada)')
plt.grid(True)
plt.legend()
plt.show()
