import numpy as np
import matplotlib.pyplot as plt

# Definición de la función a maximizar
def function(x, y):
    return -(x**2 + y**2)

# Definición de las derivadas parciales de la función
def grad_function(x, y):
    return np.array([-2*x, -2*y])

# Parámetros del algoritmo
learning_rate = 0.1
num_iterations = 50

# Inicialización de los valores de x e y
x = np.random.uniform(-5, 5)
y = np.random.uniform(-5, 5)

# Listas para almacenar los valores de x, y, y la función en cada iteración
x_values = [x]
y_values = [y]
function_values = [function(x, y)]

# Ascenso de colinas
for _ in range(num_iterations):
    gradient = grad_function(x, y)
    x += learning_rate * gradient[0]
    y += learning_rate * gradient[1]
    x_values.append(x)
    y_values.append(y)
    function_values.append(function(x, y))

# Visualización del proceso de optimización
plt.figure(figsize=(10, 5))

# Contorno de la función
x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = function(X, Y)
plt.contour(X, Y, Z, levels=50)

# Trayectoria de optimización
plt.plot(x_values, y_values, marker='o', color='red')

# Punto de máximo encontrado
plt.scatter(x_values[-1], y_values[-1], color='green', label='Máximo')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ascenso de Colinas')
plt.legend()
plt.colorbar(label='Valor de la función')
plt.grid(True)
plt.show()
