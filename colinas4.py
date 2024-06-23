import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definición de la función a maximizar
def function(x, y):
    return ((x**2 + y + 11)**2 + (x + y**2 + 7)**2)

# Definición de las derivadas parciales de la función
def grad_function(x, y):
    return np.array([2 * (x*(x**2 + y -11) + (x + y**2 - 7)), 2 * ((x**2 + y -11) + y * (x + y**2 - 7))])

# Parámetros del algoritmo
learning_rate = 0.01
num_iterations = 100

# Inicialización de los valores de x e y
x = np.random.uniform(-5, 5)
y = np.random.uniform(-5, 5)

# Listas para almacenar los valores de x, y, y la función en cada iteración
x_values = [x]
y_values = [y]
function_values = [function(x, y)]

# Ascenso de colinas
for i in range(num_iterations):
    gradient = grad_function(x, y)
    x_new = x + learning_rate * gradient[0]
    y_new = y + learning_rate * gradient[1]
    
    # Imprimir los valores de x, y para verificar
    print("Iteración {}: x={}, y={}".format(i+1, x_new, y_new))
    
    # Revisar si hay desbordamiento
    if np.isnan(x_new) or np.isnan(y_new):
        print("Desbordamiento detectado en la iteración {}. Interrumpiendo el proceso.".format(i+1))
        break
    
    x = x_new
    y = y_new
    x_values.append(x)
    y_values.append(y)
    function_values.append(function(x, y))

# Visualización en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Superficie de la función
x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = function(X, Y)
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

# Trayectoria de optimización
ax.plot(x_values, y_values, function_values, marker='o', color='red', linewidth=2)  # Corrección aquí

# Punto de máximo encontrado
ax.scatter(x_values[-1], y_values[-1], function_values[-1], color='green', s=100, label='Máximo')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Valor de la función')
ax.set_title('Ascenso de Colinas en 3D')
ax.legend()
plt.show()
