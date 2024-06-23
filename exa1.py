import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos
x = np.array([39, 43, 21, 64, 57, 43, 38, 75, 34, 52])
y = np.array([65, 75, 52, 82, 92, 80, 73, 98, 56, 75])

# Cálculo de la pendiente y el intercepto
beta_1, beta_0 = np.polyfit(x, y, 1)

# Predicciones
y_pred = beta_0 + beta_1 * x

# Error estándar
S_e2 = np.sum((y - y_pred)**2) / (len(x) - 2)
s_beta_1 = np.sqrt(S_e2 / np.sum((x - np.mean(x))**2))

# Prueba de hipótesis
t_stat = beta_1 / s_beta_1
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=len(x) - 2))

# Imprimir resultados
print("Pendiente (beta_1):", beta_1)
print("Intercepto (beta_0):", beta_0)
print("Estadístico t:", t_stat)
print("Valor p:", p_value)

# Graficar los datos y la línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, y_pred, color='red', label=f'Regresión lineal\ny = {beta_0:.2f} + {beta_1:.2f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión lineal de los datos')
plt.legend()
plt.grid(True)
plt.show()
